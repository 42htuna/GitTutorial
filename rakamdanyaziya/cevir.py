import cevirici

rakam = input("Rakamı giriniz : ")
   
if rakam.find(",") != -1:
    a = rakam.split(',')

elif rakam.find(".") != -1:
    a = rakam.split('.')
    
else:
    if rakam == "":
        rakam = "0"
    rakam = rakam+".00"
    a = rakam.split('.')

if len(a[1])%2 == 1:
    a[1] = a[1]+"0"

lira = cevirici.Cevirici(a[0][:36]).yaz
kurus = cevirici.Cevirici(a[1][:2]).yaz

print("Yalnız : %s TL %s KR'dir." %(lira, kurus))
