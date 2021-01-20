def solution(numbers):
	answer = []
	for i in range(len(numbers)):
		for j in range(i+1, len(numbers)):
			answer.append(numbers[i]+numbers[j])
	return sorted(set(answer))



if __name__ == '__main__':
	numbers = [2,1,3,4,1]
	answer = solution(numbers)
	print(answer)
