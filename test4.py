d1 = [5, 2, 9, 6]
def square(array): 
     """ This function returns each component of an array squared"""
     l = len(array)
     if l==1:
        array = [array[0]*array[0]]
	return array
     first = [array[0]]
     rest = array[1:l]
     sq = [array[0]*array[0]]
     array = sq + square(rest)
     return array

if __name__ == "__main__":
	print square.__doc__	
	print square(d1)
