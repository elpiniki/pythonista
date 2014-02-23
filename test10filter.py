def filter(f,l):
  h=l[0]
  t=l[1:len(l)]
  if len(l)==1:
    return [h] if f(h) else []
  else:
    return ([h] + filter(f,t) if f(h) else filter(f,t))

def isz(n):
  return n%2==0

def lt_gen(cutoff):
  ide = "cutoff value" + str(cutoff)
  def lt(n):
    print ide
    return n>cutoff
  return lt

if __name__ == "__main__":
  l = [1,2,3,4]
  a = 3
  print filter(isz,l)
  print filter(lt_gen(3),l)
