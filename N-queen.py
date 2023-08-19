from copy import deepcopy
cnt = 0
def back_tracking(arr, idx, n):
    global cnt
# set으로 설정해서 처음부터 되는 0-n까지의 idx를 뽑아서 실행한다. n*3+set에서 삭제하는 시간 복잡도가 걸린다.
    lst = set([i for i in range(n)])
    for k in range(idx):
        lst.discard((arr[k] - (idx - k)))
        lst.discard((arr[k] + (idx - k)))
        lst.discard(arr[k])
        # print(arr)
        # print(idx, list(lst))
    for j in list(lst):
        if idx+1 == n:
            cnt += 1
        else:
            new_arr = deepcopy(arr)
            new_arr[idx] = j
            back_tracking(new_arr, idx+1, n)
# 진행될때마다 n개의 처리를 진행하는 로직 -> 성능적 이슈가 있었다. n*n*3의 시간 복잡도가 걸린다.
        # if all((arr[k] - (idx - k)) != i and (arr[k] + (idx - k)) != i and arr[k] != i for k in range(idx)):
        #     if idx+1 == n:
        #         cnt += 1
        #     else:
        #         new_arr = deepcopy(arr)
        #         new_arr[idx] = i
        #         back_tracking(new_arr, idx+1, n)


def solution(n):
    global cnt
    answer = 0
    arr = [-1] * n
    back_tracking(arr, 0, n)

    return cnt
