# CodingTestStudy - FreeDeveloper
## 나동빈 - 이것이 코딩테스트이다 : 문제풀이 코드저장소

### 자주쓰이는 파이썬 코드
* 빠른 입력 코드
```python
import sys
input = sys.stdin.readline
#이후에 input()으로 사용
#입력 후 한줄개행의 경우 .rstrip() 사용
```
* 시간측정코드
```python
import time
start_time = time.time()
end_time = time.time()
print(end_time - start_time)
```
* 이중탐색코드
```python
def binary_search(array, target, start, end) :
  if start > end :
    return None

  mid = (start+end)//2

  if target == array[mid] :
    return mid
  elif target < array[mid] :
    return binary_search(array, target, start, mid-1)
  else :
    return binary_search(array, target, mid+1, end)
```


### 책내용 정리 블로그
[Tistory - 자유로운 개발자 FDEE](https://fdee.tistory.com/category/나동빈%20코딩테스트%20정리)
    
### codeup 기초문법 100제 사이트
[codeup 기초문법 100제](https://codeup.kr/problemsetsol.php?psid=23)

### 파이썬 기초문법 정리
[파이썬 기초문법 정리](https://fdee.tistory.com/entry/Phython-파이썬-기초문법-정리-codeup-기초-100제)

## Chapter3 그리디 정리
[그리디 정리](https://fdee.tistory.com/entry/Chapter3-그리디-정리)

## Chapter4 구현 정리
[구현 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter4-구현-정리)

## Chapter5 DFS, BFS 정리
[DFS, BFS 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter5-DFS-BFS-정리)

## Chapter6 정렬 정리
[정렬 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter6-정렬-정리)

## Chapter7 이진 탐색 정리
[이진 탐색 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter7-이진-탐색)

## Chapter8 다이나믹 프로그래밍 정리
[DP 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter8-다이나믹-프로그래밍-정리)
