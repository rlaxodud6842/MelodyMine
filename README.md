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
 
## 실행방법
+ `python ./main.py`

+ 1 : Type chennel and name
+ 2 : Stop type chennel and start scraping

+ 1을 선택시 -> 채널 ID와 이름을 입력받는다.
+ 2를 선택시 -> 위 선택한 채널을 기반으로 스크랩을 시작한다.
 
## TODO
+ 여러 채널 스크랩 디버깅
+ 채널별로 폴더 만들기
