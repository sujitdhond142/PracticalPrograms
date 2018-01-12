t = int(raw_input())
while t>0:
	numbers = raw_input().split()
	s=0
	l=len(numbers)
	for i in xrange(0,l):
		s=s+int(numbers[i])
	avg=s/l
	print avg
	t-=1
