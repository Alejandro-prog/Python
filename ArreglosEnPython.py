t = (1,2,3,4,5,6,7,8,9,10)
print(t)
t2 = [1,2,3,4,5,6,7,8,9,10]
print(t2)
print(t[0])
print(t2[4])
t[0] = 12 #No va a funcionar ya que es un tupla que no puede modificarse ni mutuarse
t2[1] = 12
