# MelodyMine

**MelodyMine**는 특정 채널을 주목하고 있다가, 새로운 영상이 올라올 경우 동영상, 음원으로 저장해주는 프로그램입니다.

## 설치방법

+ 파이썬 3.7이상이 요구됩니다.
+ 가상환경 설정
  `python3 -m venv venv` or `python -m venv venv`
+ 가상환경 활성화
  Windows: `./venv/Scripts/activate` or `cd ./venv/Scripts` AND `activate`
+ requirements 설치
    * `pip install -r requirements.txt`

## COCO128.yaml 설정
coco128.yaml을 열어서 경로설정 해주기
```
names:
  0: Aerosol
  1: Alcohol
  2: Awl
  ~~~~~~~~~~~~
  ~~~~~~~~~~~~
  29: Thinner
  30: ZippoOil
test: /tld_sample/test/ #테스트 데이터 경로
train: /tld_sample/train/ #학습 데이터 경로
val: /tld_sample/valid/ #평가 데이터 경로
```

## 학습 데이터 설정
각 폴더에 이미지랑, txt 잘 배치해놓기
```
data
  ├─test
  │  ├─images
  │  └─labels
  ├─train
  │  ├─images
  │  └─labels
  └─valid
      ├─images
      └─labels
```
