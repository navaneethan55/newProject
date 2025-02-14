reverse_string=input("user enter string you need  to reverse:")
t=""
i=len(reverse_string)-1
while(i>=0):
    t=t+reverse_string[i]
    i=i-1
print(t)
