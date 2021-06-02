a = list(input())
stack = []
for i in a:
    if i == ")": #()이 만나면 2로 변하도록, 그 안에 숫자가 있다면 그것을 곱한 값으로
        t = 0
        while len(stack) != 0:
            top = stack.pop(-1)
            if top == "(":
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2*t) # 괄호 안에 숫자가 있을 경우에
                break
            elif top == "[": # 1. 괄호와 중괄호가 교차하지 못한다는 특성!
                print(0)
                exit(0)
            else:
                t = t + int(top) # 괄호에 묶여 있는 숫자들을 모두 더하는 과정
    elif i == ']':
        t = 0
        while len(stack) != 0:
            top = stack.pop(-1)
            if top == "[":
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3 * t)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                t = t + int(top)
    else:
        stack.append(i)

c = 0
for j in stack:
    if j == "(" or j == "[": # 2. 괄호가 한 쌍을 이루어야 한다는 특성을 활용!
        print(0)
        exit(0)
    else:
        c += j # 괄호로 묶여 있지 않는 숫자들의 합
print(c)

# 이 문제는 스택을 이용하여 괄호가 서로 쌍을 맞추도록 하는 특성과 -> 많이 쓰임
# 괄호가 만났을 경우에 숫자로 변하고, 스택에 넣은 이후 더하는 것인지 혹은 곱하는 것인지 생각해볼 필요가 있음!
# 결론은 스택을 활용하여 문제 해결!
