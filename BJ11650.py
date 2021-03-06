# 11650 정렬

#2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
#x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치
#xi와 yi가 주어진다.(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

#출력
#첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.


comma_list = []
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    comma_list.append((X,Y))

#sort 함수의 경우 튜플이 원소일 때 자동적으로 두번째 요소까지 고려하여 작동한다.
#이때 내림차순으로 하려면 v.sort(keyy=lambda x:-x[0]) 혹은 v.sort(keyy=lambda x:x[0], reverse=True)

comma_list.sort()
for i in range(N):
    print(comma_list[i][0], comma_list[i][1])
