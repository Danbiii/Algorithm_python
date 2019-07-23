# programmers greedy Level1: 체육복 
'''
제한사항
- 전체 학생의 수는 2명 이상, 30명 이하
- 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없다.
- 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없다.
- 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있다.
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다. 
  이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없다.
'''

def uniform(n, lost, reserve):

    # 도난 당한 학생과 여분의 체육복이 있는 학생 "중복 학생 제외"
    # 진짜 체육복 2개인 학생
    real_reserve = [r for r in reserve if r not in lost]
    # 진짜 체육복 0개인 학생
    real_lost = [l for l in lost if l not in reserve]

    for number in real_reserve:
        # 양 옆 번호에 있는 학생(빌려줄 수 있는 학생들)
        right = number+1
        left = number-1

        if left in real_lost:
            real_lost.remove(left)
        elif right in real_lost:
            real_lost.remove(right)
    return n-len(real_lost)
    # 전체 학생에서 잃어버렸지만 여벌의 옷 조차 빌리지 못한 학생 수를 빼서 수업에 참여할 수 있는 학생 확인



if __name__ == "__main__":
    n = 5
    lost = [2,4]
    reserve = [1,3,5]
    print(uniform(n,lost,reserve))

# return 5 



