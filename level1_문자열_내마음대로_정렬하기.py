def solution(strings, n):

	new_strings = []
	for s in strings:
		new_strings.append(s[n]+s)

	answer = [i[1:] for i in sorted(new_strings)]
	return answer



if __name__ == '__main__':
	strings = ['abce', 'abcd','cdx']
	n = 2
	print(solution(strings, n))


# other solution

def other_solution(strings, n):
	return sorted(strings, key = lambda x:x[n]+x[:])
