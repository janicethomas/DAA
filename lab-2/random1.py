import random
n = 15000
fp = open(f"random_{n}.txt","w")
fp.write(str(n)+" ")  
for i in range(1,n):
    x = random.random()
    fp.write(str(int(x*n))+" ")  
x = random.random()
fp.write(str(int(x*n))+" ")  
fp.close()
