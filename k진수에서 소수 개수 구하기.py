def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    
    changedN = ""
    while n:
        changedN += str(n%k)
        n //=k
    
    
    splited_changedN = changedN[::-1].split('0')
    
    for splited_num in splited_changedN:
        if splited_num and is_prime(int(splited_num)):
            answer += 1
    
    return answer
