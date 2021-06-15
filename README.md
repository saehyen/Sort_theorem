# Sort_theorem
정렬에 대한 정리

## 선택정렬
- 시간복잡도 : O(N^2)
- 앞에서부터 차례대로 작은숫자를 정리함

## 삽입정렬
- 시간복잡도 : O(N^2)
- 순차대로 비교하면서 앞에서부터 채워넣음

## 퀵정렬
- 시간복잡도 : O(NlogN)
- 최악의 경우 : O(N^2)
- 피벗이라는 기준을 잡고 왼쪽원소와 오른쪽원소를 비교한뒤 정렬

## 계수정렬
- 시간복잡도 : O(N + K)
- 최소값이 0이고 최대수가 정해져있을때 사용 가능
- 0부터 최대값까지 리스트를 만들고 원소의 수에 해당하는 리스트의 개수를 세하리는 방식
- 실행시간의 상한

### 실행시간의 상한
O(n^2): 선택 정렬, 버블 정렬
O(n log n)
O(n): 선형 검색
O(log n): 이진 검색
O(1)


### 실행시간의 하한

Ω(n^2): 선택 정렬, 버블 정렬
Ω(n log n)
Ω(n)
Ω(log n)
Ω(1): 선형 검색, 이진 검색
