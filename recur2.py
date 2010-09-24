from listops import *

def sqr (num)   :   return num*num

def inc(a)   :   return a + 1

def dec(a)   :   return a - 1
 
def occur(list1,num):
	if (null(list1))   :   return 0
	elif(num == first(list1))   :   return (1 + occur(rest(list1),num))
	else   :   return occur(rest(list1),num)

def powr(a,b):
	if b == 0   :   return 1
	else   :   return a * powr(a,b-1)

def fast_powr(a,b):
	if b == 0   :   return 1
	elif b == 1   :   return a
	elif b % 2 == 0   :   return sqr(fast_powr(a,b/2)) 
	else   :   return a * fast_powr(a,b-1)

def add(a,b):
	if b == 0   :   return a
	else   :   return add(a+1,b-1)

def gcd(a,b):
	if a == b   :   return a
	elif a > b   :   return gcd(a-b,b)
	elif b > a   :   return gcd(a,b-a)


def sum(a,b):
	if a > b   :  return 0
	else   :  return a + sum (a + 1,b) 

	

