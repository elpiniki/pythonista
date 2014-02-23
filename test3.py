#why it does not work? 
def invert(param):
     """This function inverts the contents of the array"""
     i = 1
     l = len(param)
     while i<l:
	head = [param[0]]
	tail = param[1:l]
	param = tail + head
	i = i + 1
        break
     return param

if __name__ == "__main__":
	d1 = ["a", "dog", "plays", "with", "other", "dogs"]
	print invert.__doc__
	print invert(d1)
	
