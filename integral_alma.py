# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:10:32 2019

@author: rasim
"""

def f(x):
    return(x**2)

#başlangıç ve bitiş değerleri
x1 = int(input("Başlangıç değerini giriniz: "))
x2 = int(input("Bitiş değerini giriniz: "))

#aralığı ne kadar çok bölersek gerçek integral değerine o kadar yaklaşırız
n = int(input("Aralığın bölüneceği parça sayısını giriniz: ")) #aralık kaç parçaya bölünecek    
h = (x2-x1) / n # yükseklik

#KISA KENARDAN İNTEGRAL ALMA
integral_1 = 0

for i in range(n):
    integral_1 += f(x1+i*h) * h
    
print("Kısa kenar integral: ", integral_1) #olması gerekenden küçük sonuç verir

#UZUN KENARDAN İNTEGRAL ALMA
integral_2 = 0

for i in range(1, n+1):
    integral_2 += f(x1+i*h) * h
    
print("Uzun kenar integral: ", integral_2) #olması gerekenden büyük sonuç verir

#UZUN KISA KENAR BİRLİKTE İNTEGRAL ALMA
integral_3 = 0
for i in range(n):
    integral_3 += f(x1+h/2+i*h)*h
print("uzun-kısa kenar birlikte integral: ", integral_3)

#DAHA DOĞRU SONUÇ VEREN BİR YÖNTEM
integral_4 = 0
for i in range(n):
    integral_4 += (f(x1+i*h) + f(x1+(i+1)*h))*h/2
print("daha doğru bir sonuç veren integral: ", integral_4)