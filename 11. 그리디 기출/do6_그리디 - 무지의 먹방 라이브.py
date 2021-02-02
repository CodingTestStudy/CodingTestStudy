#do6_무지의 먹방 라이브, 316p
#그리디 유형

#1차 : 접근 실패
#우선순위큐를 사용해서 적은값부터 접근을 해야한다
def solution(food_times, k):
    answer = 0
    i = 0
    count = 0
    while True :
        #정답인 경우
        if count == k :
            answer = i+1
            break
        #차감 후 다음칸으로 이동하는 경우
        elif food_times[i] != 0 :
            food_times[i] -= 1
            count += 1
            i += 1
            i %= len(food_times)
        else :
            if max(food_times) == 0 :
                answer = -1
                break
            else :
                i += 1
                i %= len(food_times)
        
    return answer