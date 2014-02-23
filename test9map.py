def square(number):
  return number*number

def map(f,l):
  h = l[0]
  t = l[1:len(l)]
  return ([f(h)] if len(l)==1 else ([f(h)] + map (f,t)))

def tostr(number):
  return str(number)

if __name__ == "__main__":
  l = [2,4,5,6]
  #print map(tostr,l)
  print [tostr(square(i)) for i in l]
