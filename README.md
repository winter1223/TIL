**# git**

touch 가 붙으면 새로 생성

~ = 사용자 홈 (제일 자유롭게 활용되는 폴더)

.이 파일이름 앞에 붙으면 숨김처리 됨
(window에서는 보임)

rm.(이름)  라고 입력시 tap 해주면 자동완성됨= 첫글자 쓰고 tap해도 자동완성
ex) re => readme.md 이런식으로 쓰여짐


앞에 썻던 code 쓰기 귀찮으면 자판에 위아래양옆자판 누르면 됨

mkdir =make directory
폴더 만들기
(forder= directory) 

cd (=이동)
./../.git
내위치/상위폴더/안에 파일



**## git에서 제일 많이 쓰이는 code(?)**


### 계정 설정
 $ git config --global user.'내이름'

- $ git config --global user.email'github에서 쓸 메일주소'

- $ cat ~/.gitconfig # (#입력한대로 나왔나 확인하는 법)


**### 처음에 설정법**

#### project 폴더 생성
- mkdir new_project

#### 폴더로 이동
- cd new-project

#### 꼭 생성 해야하는 파일 생성
- $ touch README.md , .gitignore (#파일을 만들고)

#### gitignore.io에 접속해 태그검색해서 필요한 내용 복붙

#### 폴더를 리포로 초기화
- $ git init (#리포하기)

#### REMDME.md , .ignore 파일 add(tracking)
- $ git add .
(add .이라고 하면 전체 add)
(git add <파일이름>해도 됨)

#### commit
- $ git commit -m 'first commit'
  
#### 원격 저장소 생성 

### 초기화 시점에 1회 입력

$ git init

 

### '작업하며 계속 입력'

$ git add filename



$ git commit -m 'massage'



### 모니터링 명령어

$ git status (# 현재 상황)

$ git log (# commit log)





랄랄랄라라라제발 쳐져줄래?

# CIL  (제목)

가장 큰 제목은 `#`+`띄어쓰기`

- 나머지 부제들은 `#`을 하나씩 늘려가면 됨



## (부제)

### 순서없는 목록

- 이건 `-`하고 `띄어쓰기` 하면  됨

 - 이건 `-`하고 `tap` 눌러주면 됨



### 순서 있는 목록

1. 이런식으로 `숫자`+ `.`해주면 됨

2. 이거도 똑같이 하고  `tap`하면 됨

  1. `tap` 하면 이렇게 됨



### 텍스트 스타일링

``이걸 써주는 거임 글자 앞뒤로

`냠냠` 이렇게 쓰면 색이 바뀜

`*`이게 앞뒤로 붙으면 글자가 기울어짐

- *냠냠*

`**`이게 앞뒤로 붙으면 글자가 두꺼워짐

- **냠냠**


 ### 코드블록

`이거 세개 써주면 됨
\```

def my_ func():

  print ('hello')

\```

이런식으로 뒤에도 `이거 세개 써주면 됨



### 표

아직잘 모르겠으나 예시로

|이름 |전화번호 | 나이|

typora에선 가능하나 vscode로는 아직 어떻게 하는지 모름
 