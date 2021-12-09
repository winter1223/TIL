# pandas
## pandas 불러들이기
시작은 무조건 

import numpy as np
import pandas as pd

판다스란?
파이썬에서 사용할 수 있는 데이터 전처리용 패키지 입니다.

엑셀처럼 파일을 다룰수 있게 하는 도구
아주 큰 파일도 처리가능

## Series
1차원 구조를 표현
 
series = pd.Series( [10, 20, 30, 40] ) 
(#여기서 Series는 calss 말하는 것 
판다스 내부에 class가 정의되어 있다)
series
=>
0    10
1    20
2    30
3    40
dtype: int64
(#왼쪽 인덱스 번호 오른쪽이 값
마지막에 타입도 같이 나옴=dtype: int64)

*인덱스와 함께 표현되서 2차원 처럼 보이지만, 1차원 입니다

display( series.ndim )
display( series.shape )
=>1
(4,)

## DataFrame
2차원 구조
여러개의 시리즈가 모여서 하나의 데이터프레임이 됩니다.

weight = pd.DataFrame([
  [76.4, 'kg'],
  [75.7, 'kg'],
  [76, 'kg'],
  [76.2, 'kg']
])
weight

=>
(행)  0   	1   (<=여기가 열)
0	76.4	kg
1	75.7	kg
2	76.0	kg
3	76.2	kg
이런식으로 표로 도출됨

display( weight.ndim )
display( weight.shape )
2
(4, 2)

## 파일 읽어오기
판다스는 read_csv라는 기능으로 파일을 읽어올 수 있습니다.
CSV(Comma Seperated Value)
텍스트가 콤마로 구분된 형태로 되어있는 파일
엑셀, CSV, ... 등의 다양한 파일 형태를 읽어서 데이터 프레임 형태로 자동으로 변환을 해줍니다.
rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/data/weight_log.csv')
rawData
이런식으로 가져옴

## 데이터 프레임 사용하기
- 출력
* head
자료의 제일 앞 자료 출력(==DataFrame.head())

상위 5개의 자료를 출력 한다면
DataFrame.head(n=5)
rawData.head()

* tail
자료의 맨 끝 자료 출력(==DataFrame.tail())

하위 5개의 자료를 출력
DataFrame.tail(n=5)
rawData.tail()

그리고
파라미터를 통해서 출력 갯수를 제한할 수 있음
rawData.head(2)
rawData.tail(2) 이런식으로

## 데이터의 요약된 정보
rawData.info()

다 info하고 싶다면
rawData.describe(include='all')

## 인덱싱(색인)
넘파이의 배열 인덱스와 유사
판다스의 데이터프레임은 기본적으로 열우선 인덱스 입니다.

* 열(column) 인덱싱
  데이터 프레임은 행을 선택하지 않고, 시리즈를 선택하는 방향으로 인덱스를 합니다. 
rawData['몸무게']

* 배열 인덱스 지원합니다. 
col = ['이름', '몸무게', '측정일']
rawData[ col ]

* 행(row) 인덱싱
loc
iloc

** loc **
rawData.head(1)
첫 번째 행의 내용 출력 후
rawData.loc[0]
행 인덱스가 가능하고 해당 행을 시리즈 형태로 반환
(선택된 행도 시리즈가 됩니다. )
type(rawData.loc[0])

-  슬라이스도 가능합니다. 
판다스의 슬라이스는 마지막 인덱스에 대해서 포함한 것
rawData.loc[0:3]
행에 대해서 배열 인덱싱
rawData.loc[[1, 3, 5]]

- 행, 열 인덱싱
rawData.loc[0, '몸무게']
물론 배열 인덱스와 함께 사용할 수 있습니다. 
rawData.loc[0, ['이름', '몸무게']]
rawData.loc[[1, 3, 5], ['이름', '몸무게']]

슬라이스와 함께 사용
rawData.loc[0:3, ['이름', '몸무게']]
rawData.loc[0:3, '이름':'몸무게']

** iloc **
iloc를 사용하면 컬럼 인덱스에 정수를 사용할 수 있습니다.
rawData.iloc[0:3, 1:4]

## 조건 검색
불리언 인덱스의 활용
rawData['지점'] == '여의도'
불리언 시리즈가 반환 됩니다.
반환된 불리언 시리즈(배열)를 인덱스로 활용

## 다중조건
and, or, not
판다스는 &(앰퍼샌드), |(파이프라인), ~(틸드) 문자를 사용해서 표현 합니다.

괄호를 이용해서 정확하게 표현 해주시는게 좋습니다
서초구 지점의 최현경 담당자의 자료만 검색한다면
rawData[ (rawData['지점'] == '서초구') & (rawData['담당'] == '최현경') ]
이거도 가능 rawData[ (rawData['지점'] == '서초구') & ((rawData['담당'] == '최현경') | (rawData['담당'] == '김현경')) 

## 문자열 처리
isin은 리스트를 파라미터로 갖습니다. 
리스트 내의 값들 중에서 하나라도 존재하면 True, 그렇지 않으면 False
rawData[ (rawData['지점'] == '서초구') & (rawData['담당'].isin(['김현경', '최현경'])) ]

* contains는 문자열 내에서 특정 문자열이 존재하면 True, 그렇지 않으면, False
rawData[ ~(rawData['담당'].str.contains('김')) ]
rawData[ (rawData['담당'].str.contains('김')) ]

* startswith는 문자열 내에서 특정 문자열로 시작하는 경우 True, 그렇지 않으면, False
rawData[ rawData['담당'].str.startswith('김') ]

## 결측치
결측치가 있으면 분석을 제대로 수행할 수 없기 때문에 어떻게든 처리를 해줘야만 합니다.
결측치를 채우든가, 지우든가
결측치를 채우는 여러가지 방법
= 평균, 중앙값 등으로 대체하는 경우
책에서나 할 수 있는 얘기들이고, 실제로도 유용한가?

- 결측치를 확인하는 방법
#결측치의 개수
rawData['몸무게'].isnull()
or
rawData['몸무게'].isna()

-  True는 1과 같기 때문에, True를 모두 더하면 결측치의 개수가 됩니다. 
rawData['몸무게'].isna().sum()

- 결측치만 확인하고 싶은 경우
rawData[ rawData['몸무게'].isna() ]
- 결측치를 제외하고 확인하고 싶은 경우 
rawData[ ~rawData['몸무게'].isna() ]

조건에 맞는 자료들 중에서 내가 원하는 컬럼만 확인
rawData.loc[ rawData['몸무게'].isna(), '이름']
rawData.loc[ rawData['몸무게'].isna(),  ['지점', '담당', '측정일']]

## 이상치(outlier)
특별히 크거나, 작은 값
얼마나 크거나, 작아야 이상치라고 할 수 있는가 그런거 없음
술자가 알아서 정해야함
rawData['몸무게'].describe()

이상치를 찾는 경우가 아니라면, 이상치는 제거하고 분석을 진행 합니다.

특정 값을 넘어가는 자료를 이상치로 판단
rawData[ rawData['몸무게'] > 76.15 ]

4분위수를 이용한 방법
display( rawData['몸무게'].quantile(0.25) )
display( rawData['몸무게'].quantile(0.50) )
display( rawData['몸무게'].quantile(0.75) )
display( rawData['몸무게'].quantile(0.99) )

이상치를 제거하는 방법
low = rawData['몸무게'].quantile(0.01)
high = rawData['몸무게'].quantile(0.99)
rawData[ (rawData['몸무게'] < high) & (rawData['몸무게'] > low) ]

## 중복 데이터 검사
duplicated를 이용해서 중복된 자료를 검사

rawData.duplicated(subset=['지점'])

rawData[ rawData.duplicated(subset=['지점'], keep=False) ]

## 통계분석
판다스에서 제공하는 통계관련된 기능들
=   pivot(엑셀에서 사용하는 피봇(평균?) 기능과 동일함)
    crosstab
    그룹화

지점별 몸무게 평균
pd.pivot_table( rawData, index='지점', values='몸무게')
지점별 담당자별 몸무게의 평균
pd.pivot_table( rawData, index=['지점', '담당'], values='몸무게')


지점별 몸무게 총합
pd.pivot_table( rawData, index='지점', values='몸무게', aggfunc=np.sum)

#그룹 객체를 반환
그룹화를 통한 통계적 수치
rawData.groupby(['지점'])

그룹화를 통한 지점별 몸무게 평균
rawData.groupby(['지점'])['몸무게'].mean()

지점별 담당별 몸무게 평균
rawData.groupby(['지점', '담당'])[['몸무게']].mean()

컬럼별로 집계를 다르게 하고 싶다면
rawData.groupby('지점').agg({
  '몸무게': 'mean', '담당': 'count'
})

## 데이터 프레임 조작하기
추가, 수정, 삭제
