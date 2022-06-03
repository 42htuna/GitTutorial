class UsKok:

    """Bir sayının üssünü veya kökünü almak için yazılmış basit bir uygulama"""

    name="Hakan"
    surname="Tuna"
    version="1.0.0"
    mail="42htuna@gmail.com"

    def __init__(self, deger):
        self.deger=deger
    
    def yazDeger(self):
        return self.deger

    def author(cls):
        ns="{} {}".format(cls.name, cls.surname)
        return ns
        
    @property
    def direkHesapla(self):
        a=int(input("Pay :"))
        b=int(input("Payda :"))
        return round(self.deger**(a/b),14)
        
    @staticmethod
    def degerGirHesapla(n):
        a=int(input("Pay :"))
        b=int(input("Payda :"))
        return round(n**(a/b),14)
    
giris=UsKok(81)
