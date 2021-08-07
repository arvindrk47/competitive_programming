#Read the number of test cases.

a = int(input())
for i in range(a):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	#Compute the answer
	#Complete the line below	
	ans = a%b
	print(ans)
