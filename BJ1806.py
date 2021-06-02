#내가 쓴 답변 -> 시간 초과
import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
Mcnt = N
a = 0
while a < N:
    dp = 0
    cnt = 0
    for i in range(a, len(arr)):
        dp += arr[i]
        cnt += 1
        if dp >= S:
            Mcnt = min(cnt, Mcnt)
    a += 1
print(Mcnt)
# 모든 저렇게 하면 모든 부분합을 구하기 때문에 비효율적이고 시간도 많이 걸림!
# 연속된 S보다 큰 값만 도출 할 수 있도록 하는 방법이 필요함(그리고 최대한 부분합 원소의 개수도 적게)

#참조용
import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))
Mcnt = N+1
sum = [0] * (N + 1)
for i in range(1, N + 1):
    sum[i] = sum[i-1] + arr[i-1]
start = 0
end = 1
while start != N:
    if sum[end]-sum[start] >= S:
        if Mcnt > end - start:
            Mcnt = end- start
        start += 1
    else:
        if end != N:
            end += 1
        else:
            start += 1
if Mcnt != N+1:
    print(Mcnt)
else:
    print(0)


# 첫째로 부분합을 나타내는 것으로, sum(i) -> 0부터 i번째 까지의 숫자를 더한 값이 나타나는 리스트 생성
# 이때 부분합은 sum(N) - sum(M) 을 통해서 arr[N:M]에 해당하는 값을 찾을 수 있음
# 투 포인트라는 것이 중요함!
# start와 end의 값을 설정하여 두 값이 N까지 갈 때까지만 실행 시켜도 원하는 답이 나오도록 함!
