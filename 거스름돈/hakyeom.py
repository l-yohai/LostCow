import sys

money = int(sys.stdin.readline())

'''
동전이 무한히 많다고 가정
5원을 부터 가장 많이 거슬러 주고 남는 돈을 2원으로 거슬러준다.
모든 경우에 나눠 떨어지게 거슬러 주지 못하면 -1을 리턴
'''
max_cnt_5 = money // 5  # 5원을 가장 많이 거슬러 줬을 때 갯수


min_cnt_total = -1  # 거슬러 줄 수 없으면 -1

'''
5원의 갯수를 줄여나가면서 확인해본다.
'''
for cnt_5 in range(max_cnt_5, -1, -1):
    remain_money = money - cnt_5 * 5

    '''
    남은 돈이 2원으로 나눠 떨어지면 가장 적게 거슬러 줄 수 있는 경우
    (5원을 가장 많이 거슬러 주는 경우부터 역순으로 출발 했기 때문에)
    '''
    if remain_money % 2 == 0:
        cnt_2 = remain_money // 2
        min_cnt_total = cnt_5 + cnt_2
        break

print(min_cnt_total)
