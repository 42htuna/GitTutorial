print("\n\n\n... İKİ STRING DEĞERİN TOPLAMI ...")
print(("\nBirinci Sayı".ljust(19, ' ') + ": "), end='')
birinci = input()

print(("İkinci Sayı".ljust(18, ' ') + ": "), end='')
ikinci = input()

eldevar = 0
toplam = []

if len(ikinci) > len(birinci):
    birinci=birinci.rjust(len(ikinci),'0')
else:
    ikinci=ikinci.rjust(len(birinci),'0')

birinci = [i for i in birinci]
ikinci = [i for i in ikinci]

birinci.reverse()
ikinci.reverse()

for basamak in range(len(birinci)):
    topla = int(birinci[basamak]) + int(ikinci[basamak]) + eldevar

    if topla > 9:
        eldevar = 1
    else:
        eldevar = 0

    gir = [i for i in str(topla)]
    toplam.append(gir[::-1][0])

if eldevar:
    toplam.append(eldevar)

toplam.reverse()
values = ''.join(map(str, toplam))
print("\nSayıların Toplamı".ljust(19, ' ') + ": " + values + "\n")
print("".rjust(34, ':') + "\n\n\n")