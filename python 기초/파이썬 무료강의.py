print('hello world')
#숫자 자료형
print(5)
print(3.1)
print(1000000)
print(5+2)
print(5*5)
print(3*(3+2))
#문자열 자료형
print('배고파')
print('qo'*9)
#boolean자료형
#참,거짓
print(5>10)
print(5<10)
print(True + True)
print(not True)
print(not False)
print(not (5>10))
#변수
#애완동물 소개하기
print('집근처 길고양이 이름은 일로와입니다')
print('일로와는 3살로 추정되며, 똑똑합니다')
print('일로와는 어른일까요? True')

#이름이 바뀌었다면,..
name = '일로와'
animal = '고양이'
age = 3
telent = '똑똑'
is_adult = age >= 3
#변수를 먼저 생성해주고
print('집근처 길', str(animal),' 이름은 ',str(name) ,'입니다')
print( name +'는' + str(age) + '살로 추정되며,'+ telent +'합니다')
print( name +'는 어른일까요?' + str(is_adult))
print(str(name)+ '는 어른일까요?'+ str(is_adult))
#이렇게 했다면 변수만 바꿔도 바꾼거로 출력됨

#주석
#, 여러문장 주석 ''' ''' ,드래그 컨트롤 /

# '''변수를 이용하여 다음 문장을 출력하시오
# 변수명 station
# 변수값 '사당', 신도림', '인천공항' 순서대로 입력
# 출력문장 xx행 열차가 들어오고 있습니다.'''
a= '사당'
b= '신도림'
c= '인천공항'
print(a + '행 열차가 들어오고 있습니다.')
print(b + '행 열차가 들어오고 있습니다.')
print(c + '행 열차가 들어오고 있습니다.')

#연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2의 3승
print(5%3)#% == 나머지 구하기
print(10%3)
#몫 구하기
print(10//3)
print(10//2)
#비교연산
print(10 >= 9)
print (10<3)
print(5<=5)

print(3 == 2)
print(3+2 == 5)


#and or not
print((3>0)and (4>5))
print((3>0)&(4>5))

print((3>0) or (4>5))
print((3>0) | (4>5))

print(not 3 == 3)
print(not(1 != 1))

#간단한 수식
print(2+ 3+ 4)
print((3+4)*2)
num = 2+ 3+ 4
print(num)
num += 2 
print(num)
num *= 2
print(num)
num /= 2
print(num)
num -= 2
print(num)
num %= 2
print(num)

#숫자처리 함수
print(abs(-5))#abs =  절대값
print(pow(2, 3))
print(pow(5,2))#power pow(숫자,숫자) =  제곱한값
print(pow(4,2)) 
#(pow(5,2)) == 5 *5 = 25
#(pow(4,2)) == 4 *4 = 16

print(max(1,6))#최댓값 출력
print(min(1,6))#최소값 출력
#반올림 round
print(round(3.14))
print(round(3.8))

#math 라이브러리
from math import *
print(floor(4.56))#소수점부터내림
print(ceil(3.14))#올림
print(sqrt(16))#제곱근

#random
from random import * 

print(random()) #0.0에서 1.0 미만의 임의의 값 생성함
print(random() * 9)#0.0에서 9.0미만의 임의의 값 생성

#정수값만 뽑고싶다면
print(int(random()*10))
#값을 특정 값 부터 뽑고싶다면
print(int(random() * 45) +1)
#로또값 출력도 같음걍 6번 하면됨..
#근데 쉽게 작성하고 싶으면
print(randrange(1,46))#1~46미만값 출력

print(randint(1,45))#1~45이하값출력

''' 월 4회 스터디함 3번은 온라인 1번은 오프라인으로
아래 조건에 맞는 오프라인 모임날짜를 정해주는 프로그램 작성
1, 랜덤으로 날짜뽑아야함
2, 월별날짜는 다름을 감안하여 최소 일수인 28일 이내
3, 매월 1~3일은 스터디를 준비해야하므로 제외'''
#오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *
print( int(random() * 28) +4)
print(randrange(4,29) )
print(randint(4,28))
date = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월',( int(random() * 28) +4),'일로 선정되었습니다' )
print('오프라인 스터디 모임 날짜는 매월' + str(date) + '일로 선정되었습니다' )

m,