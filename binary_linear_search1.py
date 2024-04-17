def binary_search(liste,hedef):
     bas=0
     son=len(liste) - 1
     while bas <= son:
         ortlalama = (bas+son)//2
         if liste[ortlalama] == hedef:
             return ortlalama
         elif liste[ortlalama] < hedef:
             bas = ortlalama + 1
         else:
             son = ortlalama - 1
     return -1

liste = [1,2,3,4,5,6,7,8,9]
hedef = 8
sonuc = binary_search(liste,hedef)
if sonuc != -1:
   print("Binary  Hedef bulundu indeks",sonuc)
else:
    print("Hedef bulunamadi")    

def linear_search(liste,hedef):
    for i in range (len(liste)):
        if liste[i] == hedef:
            return i #Harf bulundu
    return -1 #harf bulunamadı

liste = [5,3,8,1,9,2]
hedef = 2
sonuc = linear_search(liste,hedef)
if sonuc != -1:
    print("Linear Sonuc bulundu indeks : ",sonuc)
else: 
    print("Sonuc bulunamadi")    