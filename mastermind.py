import random
cevap=str(random.randrange(10,98))
dogru_yer=0
yanlis_yer=0
print("Mastermind oynuna hoşgeldin!")
print("\n")
print("10 ile 98 arasında bir sayı girerek bilgisayarı yenmeye çalış!")
print("\n")
sayac=0


hile cevap[0]==cevap[1]:
    cevap=str(random.randrange(10,98))
#eğer iki basamak da aynı ise tekrar random döndürerek sayıyı farklı bir rastgele sayıya çevirdim      
denek=int(input("haydi tuttuğum sayıyı tahmin et:"))

while denek < 10 or denek >98:
    print("Beni ancak 10 ile 98 arasında bir sayı girerek yenebilirsin ")
    #burda istenildigi üzere girdiyi sadece istenen aralikta sinirlandirdim
    denek=int(input("haydi tuttuğum sayıyı tahmin et:"))

denek=str(denek)
cevap=str(cevap)
while cevap != denek :
#deneme input unun sürekli ekrana yazilmasi while döngüsü kullandim
       
    if (denek[1]==cevap[0] or denek [0]==cevap[1]):
        yanlis_yer+=1        
        print("{} adet sayin yanlis yerde".format(yanlis_yer))
        yanlis_yer=0
        denek=input("haydi tuttuğum sayıyı tahmin et:")
        sayac +=1


    elif (denek[1]==cevap[1] or denek[0]==cevap[0]):
        dogru_yer +=1
        print("Bravoo 1 basamağı tutturdun!")
        dogru_yer =0
        denek=int(input("haydi tuttuğum sayıyı tahmin et:"))
        sayac +=1

        if denek < 10 or denek >98:
            print("Beni ancak 10 ile 98 arasında bir sayı girerek yenebilirsin ")
            #burda istenildigi üzere girdiyi sadece istenen aralikta sinirlandirdim
            denek=(input("haydi tuttuğum sayıyı tahmin et:"))
        else:
            denek=str(denek)

        
    elif (denek[1]==cevap[0] and denek [0]==cevap[1]):
        yanlis_yer+=2  
        print("{} adet sayin yanlis yerde".format(yanlis_yer))
        yanlis_yer=0
        sayac +=1
        denek=int(input("haydi tuttuğum sayıyı tahmin et:"))
        if denek < 10 or denek >98:
            print("Beni ancak 10 ile 98 arasında bir sayı girerek yenebilirsin ")
            #burda istenildigi üzere girdiyi sadece istenen aralikta sinirlandirdim
            denek=input("haydi tuttuğum sayıyı tahmin et:")
        else:
            denek=str(denek)



    else :
        print("girdiğin sayı ile benim aklımdaki sayı tamamen farklı")
        denek=int(input("haydi tuttuğum sayıyı tahmin et:"))
        yanlis_yer=0
        sayac +=1
        if denek < 10 or denek >98:
            print("Beni ancak 10 ile 98 arasında bir sayı girerek yenebilirsin ")
            #burda istenildigi üzere girdiyi sadece istenen aralikta sinirlandirdim
            denek=input("haydi tuttuğum sayıyı tahmin et:")
        else:
            denek=str(denek)


if  sayac==0:
    print("Aklimi okuyabiliyorsun ! Tek seferde sayımı bulabilmen çok etkileyici!!!") 
else:
    print("Tebrikler!tuttuğum sayıya ulaştın")
    print("Skorun aşağıda")
    print("\n")
    print("Tebrikler tam {} doğru denemede buldun!".format(sayac))
   #sayaç için baştan bir kıstas konup oyun zorluğu belirlenebilir
    #mesela 10 deneme kolay 5 deneme zor 7 deneme ise normal olabilir.
