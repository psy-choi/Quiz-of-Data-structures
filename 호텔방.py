import sys
sys.setrecursionlimit(2000001)
def solution(k, room_number):
    answer = []
    room = [i for i in range(k+1)]
    
    def find(number):
        if room[number] != number:
            room[number] = find(room[number])
        else:
            room[number] = number + 1
            return number + 1
        
        return room[number]
    
    for number in room_number:
        answer.append(find(number) - 1)
    
    return answer
