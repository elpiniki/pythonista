def filter(f,l):
  h=l[0]
  t=l[1:len(l)]
  if len(l)==1:
    return h%2
  else:    
    return (0 + filter(f,t) if f(h) else filter(f,t))

def isz(n):
  return n%2==0








if __name__ == "__main__":
  l = [1,2,3,4]
  a = 3
  print filter(isz,l)
  print filter(lt_gen(3),l)
