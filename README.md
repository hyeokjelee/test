# Sample Data Analysis

pandas 기반 CSV 데이터 분석 프로젝트

## 📋 프로젝트 개요

`sample_data.csv` 파일에 저장된 데이터를 pandas로 분석하는 Python 스크립트입니다. 카테고리별 통계, 점수 분포, 월별 추이 등을 시각화하여 제공합니다.

## 📊 샘플 데이터 구성

| 컬럼 | 타입 | 설명 |
|------|------|------|
| id | int | 고유 식별자 |
| name | string | 이름 |
| category | string | 카테고리 (판매/관리/개발) |
| amount | int | 거래 금액 |
| date | date | 거래 일자 |
| score | int | 평가 점수 (0~100) |

## 🚀 사용 방법

### 1. 의존성 설치

```bash
pip install pandas matplotlib
```

### 2. 분석 실행

```bash
python analyze_data.py
```

## 📈 분석 항목

- **기본 통계** — 행/열 수, 수치형 열 요약 통계
- **카테고리별 분석** — 카테고리별 건수, 총액, 평균 금액, 평균 점수
- **점수 분포** — 점수 구간별 분포, 최고/최저 점수 보유자
- **월별 추이** — 월별 거래 총액 및 평균

## 📁 파일 구조

```
test/
├── README.md
├── sample_data.csv      # 분석 대상 데이터
├── analyze_data.py      # 분석 스크립트
└── .gitignore
```

## ✨ 특징

- 간단한 `pip install` 후 바로 실행 가능
- 별도 설정 파일 없이 `sample_data.csv` 하나로 동작
- 표준 출력으로 분석 결과 제공