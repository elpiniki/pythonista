d1 = [4, 4]
def morzbin(array): 
     """ This function returns 0 if all zygoi, and 1 if at least one monos"""
     l = len(array)
     if l==1:
	m = array[0]%2
	return m
     else:
     	rest = array[1:l]
     	m = array[0]%2
        if m <> 0:
	       return morzbin(rest)
        else: 
	       return 

if __name__ == "__main__":
	print morzbin.__doc__	
	print morzbin(d1)
