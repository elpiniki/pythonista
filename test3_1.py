d1 = [1, 2, 3, 4, 5, 6]	
def invert(param):
     """This function inverts the contents of the array"""
     i = 1
     l = len(param)
     while i<l-3:
	head = [param[0]]
	tail = param[1:l]
	param = tail + head
	i = i + 1
	if i == l:
        	break
     return param

if __name__ == "__main__":
        invert(d1)
	print invert(d1)
	print invert.__doc__
	
	
