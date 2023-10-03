
from math import gcd
def solution(arrayA, arrayB):
  # 최대공약수의 약수들 중에서 반대쪽 array의 것들이 안나눠지는 것들 중 최대 값
    def divisor_list(array, gcd_num):
        max_num = 0
        divisor_list = [i for i in range(2, int(gcd_num ** (1/2)) + 1 ) if gcd_num % i == 0] + [gcd_num]
        for divisor in divisor_list:
            if all((e % divisor != 0 for e in array)):
                max_num = divisor
        return max_num
        
    A_gcd = arrayA[0]
    for i in range(1, len(arrayA)):
        A_gcd = gcd(A_gcd, arrayA[i])
    A_gcd = divisor_list(arrayB, A_gcd)
    
    
    B_gcd = arrayB[0]
    for i in range(1, len(arrayB)):
        B_gcd = gcd(B_gcd, arrayB[i])
    B_gcd = divisor_list(arrayA, B_gcd)
    
    
    return max(A_gcd, B_gcd)
