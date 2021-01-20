def solution(s):
	s = s.lower()
	p = len([i for i in s if i == 'p'])
	y = len([i for i in s if i == 'y'])

	return p == y


if __name__ == '__main__':
	s = 'pPoooyY'
	print(solution(s))



# other solution

def other_solution(s):
	return s.lower().count('p') == s.lower().count('y')
