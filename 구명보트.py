# programmers greedy4 구명보트

'''
무인도에 갇힌 사람들 구하기
한번에 최대 2명씩밖에 탈수 없고 무게 제한도 있다.

제한사항
- 무인도에 갇힌 사람은 1명 이상 50,000명 이하
- 각 사람의 몸무게는 40kg 이상 240kg 이하
- 구명보트의 무게제한은 40kg 이상 240kg 이하
- 구명보트의 무게제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없다.
'''
def lifeboat(people, limit):
    answer = 0
    people = sorted(people)
    number = len(people)

    # 정렬 후, 가장 작은 수와 가장 큰 수의 합 비교
    # limit이상일 경우, 가장 큰 수보다 한단계 작은 수의 합과 비교
    # 순차적으로 비교

    small_idx = 0
    big_idx = number-1
    while(small_idx < big_idx):
        if people[small_idx]+people[big_idx] <= limit:
            answer += 1
            small_idx += 1
            big_idx -= 1
        else:
            big_idx -= 1
    return number -  answer


if __name__=="__main__":
    people = [70,50,80,50]
    limit = 100
    print(lifeboat(people, limit))

# return 3
