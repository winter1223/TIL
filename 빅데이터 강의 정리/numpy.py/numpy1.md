# numpy?
##수치 해석용 모듈을 말함
###머신러닝이나 데이터 분석을 위해 만들어 진 것이 아님
분야를 가리지 않고 사용되어 머신러닝,딥러닝에 많이 사용됨.
Numpy = np

## 지원하는 type
- array(배열)
  주로 통계분석, ML/DL에서 사용
  파이썬의 리스트와 다름!

- matrix
  수학적 계산 필요할 때 사용

- **배열**
  ndim 배열의 차원
  shape 배열의 크기를 말함
  여기서 크기란 원소의 갯수와 동일함
  1차원 배열의 경우 행,열 인 배열
  튜플로 표현됨(배열의 모양이)

  - 1차원 배열
    파이썬의 리스트와 거의 동일
    '''
    arr1D =  np.array([1,2,3,4])
    리스트를 원소로 하는 배열 객체 정도로 이해하면됨
    
    * 배열 차원 확인(배열(자료)의 차원 확인 꼭 해야함
                        차원이 다르면 알고리즘 동작 못함)
        arr1D.ndim (=ndim n디멘셔널)
    * 배열의 크기모양 확인
        arr1D.shape
 - 2차원 배열
  자료의 대부분 2차원 형태, 주로 다루는 배열임
  리스트와 동일하게 배열의 원소로 배열의 갖는 배열
  '''
  arr2D = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
  arr2D

## 배열의 특징
* 인덱싱, 슬라이싱(*****)
  - 팬시 인덱싱
  - 배열의 타입
  - 넘파이에서만 정의 되는 타입
  
  * 배열의 인덱싱, 슬라이싱
    list와 기본개념은 동일
    (1차원 배열은 list와 거의 동일)
    display(arr1D)
    display(arr1D[0])
    display(arr1D[1])
    display(arr1D[-1])

  *배열도 이터레이블 객체임
  그래서 반복문 사용 가능함(대신 리스트에서 제공되는 것 말고 ex) 메소드,소트,리버스 등)
  for x in arr1D:
  print(x)

  * 내장함수는 사용 가능함
    display(min(arr1D))
    display(max(arr1D))

### 2차원 배열의 인덱싱과 슬라이싱
- 인덱싱 = 리스트와 마찬가지로 행, 열 표현
   array[행, 열]
- 슬라이스 = 행, 열을 각 각 정의 할 수 있음
   * array[행시작 :행끝 , 열시작: 열끝]
  
  * 2차원 배열의 인덱스
    display(arr2D)
    display(arr2D[0.0])
    display(arr2D[0.1])
    display(arr2D[2.1])                   
                                    =>      1
    array( [[1,2,3],                        2
            [4,5,6],                        8
            [7,8,9]])

    * 배열은 행 우선 인덱스 제공
        display(arr2D[0]) (여기서 숫자 0이 행번호임)
        display(arr2D[0,]) (이렇게 열에 공백넣어도 행 기준으로)
        
        display(arr2D[:,1])
        => array([1,2,3])
    
    * 열만 인덱싱 못함, 슬라이스를 잘 활용해야함
        display(arr2D[:,1])
        array([2,5,8])

    * 슬라이스 잘 활용시 행, 열 동시에 슬라이스 가능함
        display(arr2D)
        display(arr2D[1:,1:])

#행이든 열이든 0부터 시
#arrN[1,3:6]에서
#앞부분 1은 두번째줄에 있는 
#3:6은 ** 시작점:끝점+1 ** 의 숫자니까
#4,5,6 그러니까 3,4,5번째 자리에 있는 숫자가 나오는 거지용
        
  * 팬시 인덱싱
    인덱스로 배열을 사용


    ** 불리언 배열:불리언(True,False)로 이루어진 배열
     *정수 배열: 정수로 된 배열

     **불리언 인덱스
    - 배열에서 True에 해당하는 값만 선택
      불리언 배열을 조건에 부합하는 값만 선택

      display(arr1D)
      arr1D [np.array(True,False,False,False)]
      array([1,2,3,4,])
      (여기서 2,3,4는 False니까 빼고)
      => array([1])

    - 배열에서 조건에 맞는 값만 검색
      display(arr1D > 2)
      display(arr1D[arr1D>2])
      array[F,T,F,T]
      => array([2,4])

    *정수배열
      배열에서 원하는 인덱스 배열로 생성
      중복선택이 가능함!
      배열 크기, 인덱스 배열 크기 달라도 노상관
      display( arr1D )
      idx = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1])
      arr1D[ idx ]
      =>array([1, 2, 3, 4])
        array([2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4,
        4, 3, 2, 2, 2])

## 배열의 타입

리스트= 여러개의 타입을 원소로 가질 수 있음

배열은 하나만의 타입을 원소로,
생성 될 때 원소들의 타입을 보고 기본적인 자료의 타입으로 결정함
arr1D.dtype
=>dtype('int64')(여기서 64는 바이트의 크기)

python은 숫자표현의 한계가 없지만
라이브러리는 파이썬만으로 만들어있지 않음
그래서 자료의 표현에 한계 발생할 수 있음

원소의 타입여러개면 가장 큰 타입이 기본타입이 됨

arr = np.array([1,2,3,4,5,0])
display(arr)
diaplay(arr.dtype)
=> array([1.,2.,3.,4.,5.])

arr= np.array([1,2,3,4,5], dtype np.float64)(실수로 표현하고 싶을 때 이렇게 씀)
              (이거정수임)
display(arr)
display(arr.dtype)

문자열과 정수가 같이 있다면 문자열로 됨(문자열은 숫자도 표현 가능하니까)

*텐서플로우 사용하는 경우
자료의 차원과 타입에 매우 민감함*

* 넘파이에만 있고 파이썬에는 없는
  inf = 표현할 수 없는 값
  함수 수렴 안함, 발산함(inf,-inf)

 NaN (Not a Number)
 결측치 표현(비어있는 값 표현)
 값을 표현할 수 없는 경우에 사용
 (NoN은 none 절대 아니다 헷갈리지마라...)
 
 display(type(np.NaN))
 display(np.array([0]/np.array([0])))
 => float
    array([nan])

inf
display(type(np.inf))
display(np.log(0))
=>float
  -inf


## 배열 생성하는 법

초기화된 배열 0과 1만 특별히 취급
원소 전부 0 or 1인 경우 선형대수에서는 특별하게 취급함

- 0으로 초기화된 배열
  np.zeros(10,dtype = np.int) (#실수형태로 들어가는거라 .int 붙이는 거임)
  => array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

- 1으로 초기화된 배열
  np.ones(10)
 => array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

- 0과 1이 아닌 다른값으로 초기화 하고 싶은 경우
np.full(10, 5) (np.full(몇번할껀지,표기될 정수(실수쓰고싶으면 숫자에 뒤에.붙이면 됨 ex) 6.))
=>array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

## 수열 생성하는 법
range 와 같은 역할을 함

arange (#실수(소수float)에 대한 수열 가능)
np.arange(1,10)
=>array([1,2,3,4,5,6,7,8,9])

실수 쓰고 싶을땐
np.arange(1,2,0.1)
        (star,stop,step)
=>array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])

주어진 구간에서 갯수만큼 균등한 간격으로 수열생성함
마지막원소도 포함
np.linspace(0,10,11)(#star,stop,step(구간))

display(np.linspace([1,2,100])) 
(#1-2사이 수를 100등분 할께라는 뜻,
stop의 마지막수도 꼭 포함되어 출력)

## 무작위 배열 생성법
- random
  파이썬,넘파이의 랜덤은 균등분포를 의미함

  np.random.rand(10)
  균등분호를 통해 정해진 갯수만큼 수를 생성함
  랜덤해서 실행 할 때 마다 다른 값 생성됨

  - 정수형태로 무작위 수 생성
    np.random.randint(0,10,size=10)

  - 무작위로 생성되는 수를 고정할 수 있음
    np.random.seed(100)(#들어가는 숫자에 따라 달라짐)
    np.random.rand(10)

  - 중복되지 않는 무작위 수 생성
    arr = np.arange(1,11)
    np.random.choice(arr,size=5)(#size=5개의 수를 랜덤하게 선택한다)
    *중복을 없애고싶다면
    np.random.choice(arr,size=5,replace=False)(#replace=복원추출)
    
    랜덤은 표본추출,샘플링하는 경우 주로 사용됨

## 배열의 모양
저차원 배열에서 고차원 배열로 변경
or 고차원 배열에서 저차원 배열로 변경

*변경 전 크기, 후 크기 달라지면 안됨(=자료의 갯수 일치해야함)

- 저차원 배열을 고차원 배열로
  arr1D = np.random.randint(0,10,size=4)
  arr1D
  display (arr1D.reshape(2,2))
  display (arr1D.reshape(-1,2))  (*열의 갯수(크기)를 지정하면 나머지는)
  display (arr1D.reshape(4,1))    (자동으로 계산됨)
  여기서 변경 전 후 크기 다르면 안되는게 size 말하는 거임

그래서
  arr1D = np.random.randint(0,10,size=4)
  arr1D.reshape(5,1)
이거 안됨

- 고차원의 배열을 저차원 배열로
  arr2D = np.random.randint(1,10,size=(3,3))    (#행기준으로 변경)
  arr2D

  display(arr2D.flatten(order='F'))   (#열기준으로 변경)
  (#여기서'F' 포트란오더:order가 F면 열기준으로 변경) 

  ## 넘파이를 이용한 연산
  
  기본적인 연산 
  자료의 형태 = scalar,vector,matrix

  - scalar
    - *python에서는 변하지 않는 상수(숫자)를 말함
    물리학에서는 양(volumn, magnited)을 표현하는 것
    방향 없고 물리적인 양 표현하는 것
    ex)10, [[1]]
 
  - vector
    - *python에서는 행 n개 열 1개인 형태
    - 행벡터와 열벡터가 있으나 보통 열벡터를 말함
    - ***근데 numpy에서는 1차원 배열 = 행 벡터
    물리학에서는 방향성을 가진 형태

    vector= np.random.randint(1,10,size=5)
    vector
    =>array([1, 9, 3, 4, 2])
    
    vector.reshape(-1, 1)
    =>array([[1],
          [9],
          [3],
          [4],
          [2]])

    *특별한 vector
    0 vector 와 1 vector 
    모든 원소가 0 이나 1인경우

    0 vector : 
    np.zeros((4,1))
    =>array([[0.],
              [0.],
              [0.],
              [0.]])
            
    1 vector : 
    np.ones((4,1))    
    =>array([[1.],
            [1.],
            [1.],
            [1.]])

- 행렬(Matrix)
  여러개의 벡터가 모여서 하나의 행렬됨
  
  - 행 n개 열 m개인 배열에 matrix이용함
  (여튼 행도 열도 다 여러개인 배열에 이용함)

    mat = np.random.randint(1, 10, size=(3, 5) )
    mat

   =>array([[9, 7, 6, 7, 9],
          [4, 1, 8, 7, 3],
          [7, 8, 1, 6, 4]])
          
          
## 타입이 다른 피연산자간의 연산
- 사칙연산만 다룸
- 크기가 서로 같으면 문제가 아닌데 다른경우 문제
- 다른경우에 가능하려면 브로드 캐스팅 해야함
  
  * scalar 와 vector의 연산 
    작은쪽의 크기를 큰쪽에 맞춰서 확장함(=브로드캐스팅)
    같은 위치의 값들끼리 연산함
      vector = np.random.randint(1, 10, size=(4,1))
      vector
      =>array([[1],
              [3],
              [2],
              [9]])
   스칼라를 연산하려는 벡터의 크기에 맞춰서 확장
    2 * vector
    =>array([[ 2],
            [ 6],
            [ 4],
            [18]])

  * 스칼라와 행렬의 연산
    마찬가지로 브로드캐스팅 후에 같은 위치의 값들끼리 연산
    mat = np.random.randint(1, 10, size=(3, 4)리
    mat
    =>array([[9, 9, 5, 9],
            [2, 9, 3, 1],
            [9, 6, 1, 9]])

    2 * mat
    => array([[18, 18, 10, 18],
              [ 4, 18,  6,  2],
              [18, 12,  2, 18]])

  * 벡터와 행렬의 연산
    벡터가 행렬의 크기에 맞춰서 브로드캐스팅이 가능하면 연산이 가능
    display(vector)
    display(mat)
    =>array([[1],
            [3],
            [2],
            [9]])
      array([[9, 9, 5, 9],
            [2, 9, 3, 1],
            [9, 6, 1, 9]])

            vector * mat 이거는 ValueError 됨..

      vector = np.random.randint(1, 10, size=(3,1))
      vector
      =>array([[9],
              [2],
              [3]])

      vector * mat
      =>array([[81, 81, 45, 81],
              [ 4, 18,  6,  2],
              [27, 18,  3, 27]])

  *벡터와 벡터의 연산은 브로드캐스팅이 되지 않기 때문에, 크기가 반드시 같아야 합니다.
    vec1 = np.random.randint(1, 10, size=(3, 1))
    vec2 = np.random.randint(1, 10, size=(4, 1))
    display( vec1, vec2 )

    =>array([[4],
          [8],
          [5]])
    array([[2],
          [9],
          [8],
          [5]])

    크기가 같다면, 연산이 가능합니다. 
    vec1 = np.random.randint(1, 10, size=(3, 1))
    vec2 = np.random.randint(1, 10, size=(3, 1))
    display( vec1, vec2 )
    =>array([[4],
            [7],
            [8]])
      array([[7],
            [3],
            [9]])
    
    vec1 * vec2
    =>array([[28],
            [21],
            [72]])

 행렬과 행렬의 연산
차원이 같으면, 벡터와 마찬가지로 브로드캐스팅 되지 않습니다. 
차원이 다르면, 저차원 행렬이 고차원의 행렬로 브로드캐스팅 가능하면 연산이 가능
\
같은 차원이라면, 반드시 두 행렬의 크기가 같아야 합니다. 
mat1 = np.random.randint(1, 10, size=(2, 2))
mat2 = np.random.randint(1, 10, size=(2, 2))
display( mat1, mat2 )

=>array([[6, 8],
        [8, 2]])
  array([[6, 6],
        [1, 8]])

mat1 * mat2
=>array([[36, 48],
        [ 8, 16]])