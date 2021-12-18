import sys
import heapq #힙라이브러리 import해줘서 불러옴
input = sys.stdin.readline

def heapsort(interable): #리스트나 튜플처럼 이터레이블 객체가  들어왔을때     
    h = []             
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq. heappush(h, value)  
         #힙 푸시를 해서 모든 원소를 들어오게
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담음
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
##파이썬은 기본적으로 min heap이 되어서 반대로 해주려면 원소에 - 를 붙이면 max heap으로 수행됨
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
res  = heapsort(arr)
for i in range(n):
    print(res[i])


