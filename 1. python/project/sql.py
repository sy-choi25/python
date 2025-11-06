#-- 기존 테이블이 있다면 삭제
DROP TABLE IF EXISTS car_registeration;

#-- region 테이블을 참조하는 새로운 car_registeration 테이블 생성
CREATE TABLE sknfirst.car_registeration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_month DATE NOT NULL,
    
   # -- region 테이블의 id를 저장할 컬럼
    region_id INT NOT NULL, 

    total_subtotal INT DEFAULT 0,
    total_compact INT DEFAULT 0,
    total_small INT DEFAULT 0,
    total_midsize INT DEFAULT 0,
    total_large INT DEFAULT 0,
    official_subtotal INT DEFAULT 0,
    official_compact INT DEFAULT 0,
    official_small INT DEFAULT 0,
    official_midsize INT DEFAULT 0,
    official_large INT DEFAULT 0,
    private_subtotal INT DEFAULT 0,
    private_compact INT DEFAULT 0,
    private_small INT DEFAULT 0,
    private_midsize INT DEFAULT 0,
    private_large INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    #-- 외래 키(Foreign Key) 설정
    FOREIGN KEY (region_id) REFERENCES sknfirst.region(id),
    
   # -- 특정 월, 특정 지역 데이터가 중복되지 않도록 설정
    UNIQUE KEY unique_month_region (report_month, region_id)
);