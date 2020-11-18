
def fibonacci(n):
    liste=[]
    if n <= 1:
        return 1
        liste.append(1)
        
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
        
n=int (input(("Kaça elemanlı?")))
liste=[]

for i in range(0,n):
        liste.append(fibonacci(i))


print(*liste,sep=" ")
    
    
    
