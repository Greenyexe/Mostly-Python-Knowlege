a = "0110"
b= 1
while b < 10:
  c = a[:len(a)//2][::-1]
  d = a[len(a)//2:][::-1]
  e = c+d
  a = a+e
  b += 1

print(a)