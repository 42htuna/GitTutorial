import cevirici

rakam = input("Rakam giriniz : ")

if rakam.find(",") == -1 or rakam.find(".") == -1:
    rakam = rakam+".00"

if rakam.find(",") != -1:
    a = rakam.split(',')
else:
    a = rakam.split('.')
   
lira = cevirici.Cevirici(a[0][:36]).yaz
kurus = cevirici.Cevirici(a[1][:2]).yaz

print("Yalnız : %s TL %s KR'dir." %(lira, kurus))
