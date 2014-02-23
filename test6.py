d1 = [1,2,3,4]
def monous(array): 
     """ This function returns array with only monoys from given array"""
     l = len(array)
     if l==1:
	m = array[0]%2
        if m <> 0:
	   array = [array[0]]
	else:
	   array = []
	return array
     else:
     	first = [array[0]]
     	rest = array[1:l]
     	m = array[0]%2
        if m <> 0:
	  array = [array[0]] + monous(rest)
        else: 
	  array = [] + monous(rest)
        return array

def isz2(number):
    return (number%2) == 0

def monous2(array):
    l = len(array)
    h = array[0]
    if l==1:  
       return [] if isz2(h) else [h]
    else:
       t = array[1:l]
       return ([]+monous2(t)) if isz2(h) else ([h]+monous2(t))  

if __name__ == "__main__":
	#print monous.__doc__	
	print monous2(d1)
