def solution(s):
    answer = []
    tuple_lst = []
    i = 1
    while i < len(s):
        element = set()
        txt = ""
        while True:
            if s[i] == "{":
                pass
            elif s[i] == "}":
                element.add(int(txt))
                i += 2
                break
            else: # , 이거나 숫자가 나타날때
                if s[i] == ",":
                    element.add(int(txt))
                    txt = ""
                else:
                    txt += s[i]
            i += 1
        tuple_lst.append(element)

    tuple_lst.sort(key = lambda x : len(x))

    before_lst = set()
    for lst in tuple_lst:
        new_lst = lst - before_lst
        answer.append(new_lst.pop())
        before_lst = lst

    return answer
