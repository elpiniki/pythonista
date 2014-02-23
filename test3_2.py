d1 = [1, 2, 3, 4, 5, 6]	
def invert(param):
     """This function inverts the contents of the array"""
     l = len(param)
     if l==1:
	return param
     head = [param[0]]
     tail = param[1:l]
     param = invert(tail) + head
     return param

if __name__ == "__main__":
	print invert.__doc__	
	print invert(d1)

	
	
