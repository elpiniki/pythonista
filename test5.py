d = 4
def isz(number):
    """ This function returns if the number is monos or zygos"""
    m = number % 2
    if m==0: 
       return True
    return False

def isz2(number):
    return (number%2) == 0  
 
if __name__ == "__main__":
	#print isz.__doc__	
	print isz2(d)


