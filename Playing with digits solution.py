#Playing with digits:

#My code:

def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i)**p
        p += 1
    tmp = 1
    while True:
        if tmp*n == sum:
            return tmp
        elif tmp*n > sum:
            return -1
        else:
            tmp += 1
    return -1
	
#Others code:

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1