def asal_mı(n):
    if n<2:
        return False
    for i in range(2,n,1):
        if n % i == 0:
            return False
    return True

def süper_asal_mı(n):
    if n<=0:
        return True
    
    if asal_mı(n):
        return süper_asal_mı(int(n/10))

for n in range (10000,100000,1):
    if süper_asal_mı(n):
        print(n) 
