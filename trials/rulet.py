import random

def rulet_spin():
    """Rulet çarkını döndürür ve rastgele bir sayı döner (0-36 arası, 00 dahil)"""
    # Rulet sayıları (0-36 ve 00)
    rulet_sayilari = ['0', '00'] + [str(i) for i in range(1, 37)]
    return random.choice(rulet_sayilari)

def bahis_yap():
    """Kullanıcıdan bahis alır"""
    print("Bahis türünü seçin: ")
    print("1. Tek sayı (1-36)")
    print("2. Kırmızı / Siyah")
    print("3. Çift / Tek")
    print("4. 1-18 / 19-36")
    
    secim = input("Seçiminizi yapın (1-4): ")
    if secim == '1':
        bahis = input("1-36 arasında bir sayı girin: ")
        while bahis not in map(str, range(1, 37)):
            print("Geçersiz sayı! 1-36 arasında bir sayı girin.")
            bahis = input("1-36 arasında bir sayı girin: ")
        return ("tek_sayi", bahis)
    elif secim == '2':
        renk = input("Kırmızı (K) veya Siyah (S) seçin: ").strip().upper()
        while renk not in ['K', 'S']:
            print("Geçersiz seçim! 'K' veya 'S' girin.")
            renk = input("Kırmızı (K) veya Siyah (S) seçin: ").strip().upper()
        return ("renk", renk)
    elif secim == '3':
        cift_tek = input("Çift (C) veya Tek (T) seçin: ").strip().upper()
        while cift_tek not in ['C', 'T']:
            print("Geçersiz seçim! 'C' veya 'T' girin.")
            cift_tek = input("Çift (C) veya Tek (T) seçin: ").strip().upper()
        return ("cift_tek", cift_tek)
    elif secim == '4':
        aralik = input("1-18 (A) veya 19-36 (B) seçin: ").strip().upper()
        while aralik not in ['A', 'B']:
            print("Geçersiz seçim! 'A' veya 'B' girin.")
            aralik = input("1-18 (A) veya 19-36 (B) seçin: ").strip().upper()
        return ("aralik", aralik)
    else:
        print("Geçersiz seçenek!")
        return bahis_yap()

def rulet_oyna():
    """Rulet oyununu başlatan ana fonksiyon"""
    print("Hoş geldiniz, rulet oyununa başlayalım!")
    
    # Kullanıcıdan bahis al
    bahis_turu, secim = bahis_yap()
    
    # Rulet çarkını döndür
    sonuc = rulet_spin()
    print(f"Rulet çarkı döndü! Sonuç: {sonuc}")
    
    # Sonucu kontrol et ve kazancı hesapla
    if bahis_turu == "tek_sayi":
        if sonuc == secim:
            print("Tebrikler! Kazandınız!")
        else:
            print("Kaybettiniz.")
    elif bahis_turu == "renk":
        # Kırmızı ve siyah sayılar (ruletteki renkler)
        # Kırmızı sayılar: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
        kirmizi = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
        if (secim == 'K' and sonuc in kirmizi) or (secim == 'S' and sonuc not in kirmizi and sonuc != '0' and sonuc != '00'):
            print("Tebrikler! Kazandınız!")
        else:
            print("Kaybettiniz.")
    elif bahis_turu == "cift_tek":
        if (secim == 'C' and int(sonuc) % 2 == 0) or (secim == 'T' and int(sonuc) % 2 != 0):
            print("Tebrikler! Kazandınız!")
        else:
            print("Kaybettiniz.")
    elif bahis_turu == "aralik":
        if (secim == 'A' and int(sonuc) in range(1, 19)) or (secim == 'B' and int(sonuc) in range(19, 37)):
            print("Tebrikler! Kazandınız!")
        else:
            print("Kaybettiniz.")
    
    print("Oyunu yeniden başlatmak ister misiniz? (E/H)")
    yeniden_baslat = input().strip().upper()
    if yeniden_baslat == 'E':
        rulet_oyna()
    else:
        print("Oyundan çıkılıyor. Görüşmek üzere!")

# Oyunu başlat
rulet_oyna()
