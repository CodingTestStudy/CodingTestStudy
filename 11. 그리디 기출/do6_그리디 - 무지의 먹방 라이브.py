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


#정답 코드
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]