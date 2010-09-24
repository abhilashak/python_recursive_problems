from listops import *


def find(item,list2):
	if(null(list2)):
		return []
	elif(item == first(list2)):
		return [item]
	else:
		return find(item,rest(list2))
	
def pre(list1,ele):
	if null(list1):
		return 'not present'
	elif (first(list1) == ele):
		return 'present'
	else: 
		return pre(rest(list1),ele)

def my_append(list1,list2):
	if(null(list1)  and null(list2)):
		return []
	elif(null(list1)):
		return list2 
	elif(null(list2)):
		return list1
	else:
		return cons(first(list1),my_append(rest(list1),list2))

def rev(list1):
	if(null(list1)):
		return []
	else:
		return append( rev(rest(list1)), [first(list1)])

def inter(list1,list2):
	if(null(list1)):
		return []
	elif(null(list2)):
		return []
	else:
		return append(find(first(list1),list2),inter(rest(list1),list2)) 
def flat(list1):
	if(null(list1)):
		return []
	elif(type(first(list1)) == type([])):
		return append(flat(first(list1)),flat(rest(list1)))
	else:
		return cons(first(list1),flat(rest(list1)))
		
		 
