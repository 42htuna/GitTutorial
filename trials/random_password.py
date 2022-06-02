#Rastgele şifre üretimi
import string
from random import *

uc = string.ascii_uppercase
lc = string.ascii_lowercase
dg = string.digits
pu = string.punctuation

karakterler = uc + lc + dg + pu

rastgeleSifre =  "".join(choice(karakterler) for x in range(randint(8, 16)))

print("Rastgele şifre     : ", rastgeleSifre)


#Şifrenin sha256 hash üretimi
from passlib.hash import django_pbkdf2_sha256

h1 = django_pbkdf2_sha256.hash(rastgeleSifre)
verify1 = django_pbkdf2_sha256.verify(rastgeleSifre, h1)

print("\nDjango sha256 hash : ", h1, " --> ", verify1, "\n")


#Şifre kontrolü
def kucukharf(sifre):
    for harf in sifre:
        for kontrolharf in lc:
            if harf == kontrolharf:
                return True
    return False

def buyukharf(sifre):
    for harf in sifre:
        for kontrolharf in uc:
            if harf == kontrolharf:
                return True
    return False

def sayi(sifre):
    for harf in sifre:
        for kontrolharf in dg:
            if harf == kontrolharf:
                return True
    return False

def sembol(sifre):
    for harf in sifre:
        for kontrolharf in pu:
            if harf == kontrolharf:
                return True
    return False

def kontrol(sifre):
    kh = kucukharf(sifre)
    bh = buyukharf(sifre)
    sa = sayi(sifre)
    se = sembol(sifre)
    
    if len(sifre) <17 and len(sifre) >7:
        uzunluk = True
    else:
        uzunluk = False

    print("\nKüçük harf   : ", kh, "\nBüyük harf   : ", bh, "\nSayı         : ", sa, "\nSembol       : ", se, "\nUzunluk 8-16 : ", uzunluk, "\n")

    if kh == True and bh == True and sa == True and se == True and uzunluk == True:
        print("Şifreniz güçlü bir şifredir.\n")
    else:
        print("Şifreniz zayıf bir şifredir.\n")
        print("""
GÜÇLÜ ŞİFRE NASIL OLMALI
1- En az 1 büyük harf,
2- En az 1 küçük harf,
3- En az 1 sayı,
4- En az 1 sembol,
5- En az 8 en fazla 16 karakter içermelidir.\n
""")

kullaniciSifre = input("Şifrenizi giriniz  : ")

kontrol(kullaniciSifre)

#Şifrenin sha256 hash üretimi
from passlib.apps import django_context

h2 = django_context.hash(kullaniciSifre)
verify2 = django_context.verify(kullaniciSifre, h2)

if kullaniciSifre:
    print("Django sha256 hash : ", h2, " --> ", verify2, "\n")
