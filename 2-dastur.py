#b='men'
#print(b)
#a='Assalomu Alaykum'
#b=input('Ismingizni kiriting hurmatli foydalanuvchi >>> ')
#print(f"{a} {b} xush kelibsiz bizning dasturimizga.")

# Istalgan soning raqamlar yig'indiisini toping 
#h=int(input("Istalgan sonni kiriting >>> "))
#k=h%10000%1000%100%10
#j=h//10000//1000//100//10
#g=h//10000%1000%100%10
#p=h//10000//1000%100%10
#t=h%10000%1000//100
#y=h%10000%1000%100//10
#r=h%10000//1000
#w=h//10000//1000%100//10


#print(f"Raqamlar yig/'indisi {k+j+g+p+t+y+r+w}") 

#print("Hayirli tong !")
#print(2+4*2)
#print('"Nexia","Tico",\'Damas\' ko\'rganlar qilar havas ')
# 5 ning 4-darajasini toping .
#print("5 ning 4-darajasi",5**4)
# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
#print("22 ni 4 ga bo'lganda qoldiq",22%4)
# Tomonlari 125 ga teng kvadratning yuzi va peremetrini toping. 
#a=125
#s=a**2
#p=4*a
#print("Tomonlari 125 ga teng kvadratning yuzi",s ,"peremetri",p)
# Diametri 12 ga teng bo'lgan doiraning yuzini toping (pi=3.14 deb oling.)
#pi=3.14
#r=6
#d=pi*r**2
#print("Diametri 12 ga teng bo'lgan doiraning yuzi",d)
# katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gigatenuzasini toping.
#import math
#x=6
#y=7
#z=x**2+y**2
#print("katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gigatenuzasi",math.sqrt(z))

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#print(kocha,"ko'chasi,",mahalla,"mahallasi,",tuman,"tumani,",viloyat,"viloyati")
#a=input("ko\'chasi ")
#b=input("mahallasi ")
#c=input("tumani ")
#d=input("viloyati ")
#print(f"{a} ko\'chasi ,{b} mahallasi ,{c} tumani ,{d} viloyati ")

#print('salom dunyo'.title())
#print('salom dunyo'.capitalize())
#print('salom dunyo'.upper())
#print('salom dunyo'.lower())
#print((f"{a} ko\'chasi").capitalize())

# 1) kiritilgan sonning kvadrati va kubini chiqarish
#g=int(input("Istalgan sonni kiriting >>> "))
#print("kiritilgan sonning kvadrati",{g**2},"va",'kubi',{g**3},'ga teng.')
# 2) foydalanuvchi yoshini kiritgan,tug'ilgan yilini topish
#h=input('Yoshingizni kiriting >>> ')
#k=2022-int(h)
#print("Sizning tug'ilgan yilingiz",k)
# 3) 2 xonnali sonni kiriting , yig'indisi,ayirmasi,ko'paytmasi,bo'linmasini topish
#y=int(input("Birinchi 2 xonali sonni kiriting. "))
#x=int(input("Ikkinchi 2 xonali sonni kiriting. "))
#print("yig'indisi,",{y+x},"ayirmasi,",{y-x},"ko'paytmasi,",{y*x},"bo'linmasi",{y/x})

# ro'yxatlar
ismlar=["anvar","inom","doston","abbos"]
ismlar.append('sherzod')
ismlar.insert(0,'elbek')
del ismlar[2]
ismlar.remove('abbos')
print('Salom',ismlar.pop(3).title(),', bugun choyxonaga boramizmi ?')

# arifmetik amallar
sonlar=[0.3,12,-5,6.4]
print(sonlar[2]+15)
print(sonlar[1]-8)
print(sonlar[1]**2)

# Tarixiy shaxslar
tarixiy_shaxslar=["Ibn Sino",'Al-Buxoriy','Amir Temur',"Bobur"]
zamonaviy_shaxslar=["Elon Mask",'Bill Gatse','Onam',"Otam"]
print(f'Men tarixiy shaxslardan {tarixiy_shaxslar.pop(1)} bilan gaplashishni istayman'+' Zamonaviy shaxslardan esa {zamonaviy_shaxslar.pop(2)}', 'va', '{zamonaviy_shaxslar.pop(3)} shaxslar bilan doimo yuzmma-yuz gaplashaman.')
















































