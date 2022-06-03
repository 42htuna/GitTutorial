import random

dizi = ["X", "O"]
oyuncu1 = random.choice(dizi)

def oyunKimBaslar():

    sayi = random.randint(0, 10)
    sayac = 3

    while (True):
        sayiGirdi = int(input("Başlayanı Belirlemek İçin 1-10 Arası Sayı Giriniz!: "))
        if (sayiGirdi == sayi):
            print("Tebrikler! Sayıyı Bildiniz. İlk Başlayacak Oyuncu1!")
            break
        elif (sayiGirdi > sayi):
            print("Daha küçük sayı giriniz!", sayac, "canınız kaldı!")
            sayac -= 1
        elif (sayiGirdi < sayi):
            print("Daha büyük bir sayı giriniz!", sayac, "canınız kaldı!")
            sayac -= 1
        if sayac == 0:
            print("\n", "Canınız Kalmadı. Üzgünüm Kaybettiniz. İlk Başlayacak Oyuncu2!")
            break


def yaziTura():

    kura = ["Y", "T"]
    kuraSecim = random.choice(kura)

    oyuncu1Sor = input("Yazıysa: Y, Turaysa: T  --> ")
    if kuraSecim == kura[0] and oyuncu1Sor == "Y":
        print("Oyuncu 1 Başlar!")

    elif kuraSecim == kura[0] and oyuncu1Sor == "T":
        print("Oyuncu 2 Başlar!")

    elif kuraSecim == kura[1] and oyuncu1Sor == "Y":
        print("Oyuncu 2 Başlar!")

    elif kuraSecim == kura[1] and oyuncu1Sor == "T":
        print("Oyuncu 1 Başlar!")


def oyunBaslamaSecim():
    oyuncuFikir = input("Oyuna Baslamak İçin Yapılacak Kura Şeklini Seçiniz!: Sayı Tutma = 1, Yazı-Tura = 0 -->")
    if oyuncuFikir == "1":
        oyunKimBaslar()
    else:
        yaziTura()
oyunBaslamaSecim()


def oyuncuAtama():

    if oyuncu1 == dizi[0]:
        oyuncu2 = dizi[1]
    else:
        oyuncu2 = dizi[0]

    oyuncu1Secim = oyuncu1
    oyuncu2Secim = oyuncu2

    def oyunBilgisi():
        print("\t".expandtabs(12), "Oyun Bilgisi-->\n")
        print("\t".expandtabs(8), "Oyuncu 1 Bu Oyunda", oyuncu1Secim, "dir.")
        print("\t".expandtabs(8), "Oyuncu 2 Bu Oyunda", oyuncu2Secim, "dir.")

    oyunBilgisi()
oyuncuAtama()


def oyunAlani():
    oyunAlanim = [["___", "___", "___",],
                ["___", "___", "___"],
                ["___", "___", "___"]]

    print("\n"*2, "\t".expandtabs(7),"Tic-Tac-Toe is Starting...\n")

    for i in oyunAlanim:
        print("\t".expandtabs(14), *i, end="\n"*2)

    kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]]

    x_durumu = []
    o_durumu = []

    sira = 1
    while True:
        if sira % 2 == 0:
            isaret = "X".center(3)
        else:
            isaret = "O".center(3)

        print()
        print("İŞARET: {}\n".format(isaret))

        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break

        y = input("soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break

        try:
            if not(int(x) or int(y) in range(1, 4)):
                print("Hata!")
                continue
        except:
            print("1 ile 3 arasında değer giriniz!")
            continue

        x = int(x) - 1
        y = int(y) - 1

        print("\n" * 15)

        if oyunAlanim[x][y] == "___":
            oyunAlanim[x][y] = isaret
            if isaret == "X".center(3):
                x_durumu += [[x, y]]
            elif isaret == "O".center(3):
                o_durumu += [[x, y]]
            sira += 1
        else:
            print("\nORASI DOLU! TEKRAR DENEYİN\n")

        for i in oyunAlanim:
            print("\t".expandtabs(14), *i, end="\n" * 2)

        for i in kazanma_olcutleri:
            o = [z for z in i if z in o_durumu]
            x = [z for z in i if z in x_durumu]
            if len(o) == len(i):
                print("O KAZANDI!")
                quit()
            if len(x) == len(i):
                print("X KAZANDI!")
                quit()
        if len(x_durumu) + len(o_durumu) == 9:
            print("oyun bitti")
            quit()
oyunAlani()

