
import os
import torch
import numpy as np
from datasets import load_dataset
from transformers import (
    AutoImageProcessor,
    AutoModelForImageClassification,
    TrainingArguments,
    Trainer
)
from torchvision.transforms import (
    RandomResizedCrop,
    Compose,
    Normalize,
    ToTensor,
    RandomHorizontalFlip
)
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def main():
    print("=" * 60)
    print("Vision Transformer (ViT) Fine-tuning — Local Dataset Version")
    print("=" * 60)

    # ---------------------------------------------------------------------
    # 1. 로컬 데이터셋 로드
    # ---------------------------------------------------------------------
    print("\n[1단계] 로컬 이미지 데이터셋 로드 중...")

    data_dir = r"C:\python_src\7.Multimodal\datasets"  # ★ 네 로컬 경로

    # imagefolder 사용
    dataset = load_dataset("imagefolder", data_dir=data_dir)    # load_dataset 할 때 'json', 'csv' 하듯이 'imagefolder' 라는 키워드 명칭

    # 자동으로 split 없음 → 직접 split
    dataset = dataset["train"].train_test_split(test_size=0.2, seed=42)

    train_dataset = dataset["train"]
    test_dataset = dataset["test"]

    # 클래스 이름 추출
    class_names = train_dataset.features["label"].names
    print(f" 클래스: {class_names}")
    print(f" 훈련 샘플 수: {len(train_dataset)}")
    print(f" 테스트 샘플 수: {len(test_dataset)}")

    # ---------------------------------------------------------------------
    # 2. 이미지 프로세서 로드
    # ---------------------------------------------------------------------
    print("\n[2단계] 이미지 프로세서 로드 중...")

    checkpoint = "google/vit-base-patch16-224"
    image_processor = AutoImageProcessor.from_pretrained(checkpoint)   # vit 모델이 학습될 때 사용한 이미지 전처리 규칙을 불러온다

    normalize = Normalize(                      # 프리트레인 mean/std를 그대로 따라함
        mean=image_processor.image_mean,
        std=image_processor.image_std
    )

    size = (    # 사진 크기를 지정하여 저장
        image_processor.size["shortest_edge"]
        if "shortest_edge" in image_processor.size
        else (image_processor.size["height"], image_processor.size["width"])
    )
        # if 모델이 shortest_edge 방식이면:
        #    한쪽 짧은 변이 224가 되게 resize
        # else:
        #    height, width를 정확히 224×224로 조정

    # ---------------------------------------------------------------------
    # 3. Transform 정의
    # ---------------------------------------------------------------------
    print("\n[3단계] 이미지 변환 파이프라인 설정 중...")

    train_transforms = Compose([
        RandomResizedCrop(size),
        RandomHorizontalFlip(p=0.5),
        ToTensor(),
        normalize,
    ])

    val_transforms = Compose([
        RandomResizedCrop(size),
        ToTensor(),
        normalize,
    ])

    def preprocess_train(examples):
        examples["pixel_values"] = [
            train_transforms(img.convert("RGB")) for img in examples["image"]
        ]
        return examples

    def preprocess_val(examples):
        examples["pixel_values"] = [
            val_transforms(img.convert("RGB")) for img in examples["image"]
        ]
        return examples

    # transform 적용
    train_dataset = train_dataset.with_transform(preprocess_train)
    test_dataset = test_dataset.with_transform(preprocess_val)

    # ---------------------------------------------------------------------
    # 4. 모델 로드
    # ---------------------------------------------------------------------
    print("\n[4단계] 모델 로드 중...")

    label2id = {name: i for i, name in enumerate(class_names)}
    id2label = {i: name for i, name in enumerate(class_names)}

    model = AutoModelForImageClassification.from_pretrained(
        checkpoint,
        num_labels=len(class_names),
        id2label=id2label,
        label2id=label2id,
        ignore_mismatched_sizes=True,
    )

    print(f" 모델 불러오기 완료 (클래스 {len(class_names)}개)")

    # ---------------------------------------------------------------------
    # 5. 평가 메트릭
    # ---------------------------------------------------------------------
    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=1)

        acc = accuracy_score(labels, preds)
        precision, recall, f1, _ = precision_recall_fscore_support(
            labels, preds, average='weighted'
        )
        return {
            "accuracy": acc,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    def collate_fn(batch):
        return {
            "pixel_values": torch.stack([x["pixel_values"] for x in batch]),
            "labels": torch.tensor([x["label"] for x in batch])
        }

    # ---------------------------------------------------------------------
    # 6. 학습 설정
    # ---------------------------------------------------------------------
    training_args = TrainingArguments(
        output_dir="./vit_local_finetuned",
        remove_unused_columns=False,
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=5e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        logging_dir='./logs',
        logging_steps=10,
        save_total_limit=2,
        seed=42,
    )

    # ---------------------------------------------------------------------
    # 7. Trainer 실행
    # ---------------------------------------------------------------------
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        data_collator=collate_fn,
        compute_metrics=compute_metrics,
    )

    print("\n=== 학습 시작 ===")

    trainer.train()

    # ---------------------------------------------------------------------
    # 8. 최종 평가
    # ---------------------------------------------------------------------
    print("\n=== 최종 평가 ===")
    eval_results = trainer.evaluate()
    print(eval_results)

    # ---------------------------------------------------------------------
    # 9. 모델 저장
    # ---------------------------------------------------------------------
    trainer.save_model("./vit_local_finetuned_final")
    print("\n모델 저장 완료: ./vit_local_finetuned_final")


if __name__ == "__main__":
    main()
