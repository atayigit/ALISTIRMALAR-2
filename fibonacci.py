
def fibonacci(n):
    liste=[]
    if n <= 1:
        return 1
        liste.append(1)
        
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
        
n=int (input(("Kaça elemanlı?")))
liste=["1"]
#fiboacci serisi ilk iki tane 1 le başlar bunu ekrana yansıtmak için
#listeye 1 sayısını ekledim
for i in range(1,n):
        liste.append(fibonacci(i))


print(*liste,sep=" ")
    
    
    
