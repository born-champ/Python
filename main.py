'''input
1000000
'''
import math

def fibo(a):
	if a == 0:
		return 0
	if a == 1:
		return 1
	return fibo(a-2)+fibo(a-1)

def main():
	a = int(input())
	# ans = fibo(a)
	# print(ans)
	if a ==0:
		print(0)
		return 
	if a== 1:
		print(1)
		return 
	fib = [0]*(a+1)
	fib[1]=1
	for i in range(2, a+1):
		fib[i]=fib[i-1]+fib[i-2] 
	print(fib[a])


if __name__=="__main__":
	main()

'''
5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1


'''


