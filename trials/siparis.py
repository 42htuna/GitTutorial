#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:08:10 2020

@author: hakan
"""

BILGI = """
How do I create a pylintrc file:
You may put it in:
/etc/pylintrc for default global configuration
~/.pylintrc for default user configuration
<your project>/pylintrc for default project
configuration (used when you'll run pylint <your project>)
wherever you want, then use pylint --rcfile=<wherever I want>
Also notice when generating the rc file, you may add option
on the command line before the
--generate-rcfile, they will be considered in the generated file.

Example :
pylint myproje.py
pylint --generate-rcfile >pylintrc
pylint myproje.py --rcfile=pylintrc

Not: Kod analizi yapar. Yazım hatasını görmezden gelmesini
isterseniz, kodunuzun satır sonuna “#pylint: disable = HATAKODU”
yazabilirsiniz. Ya da “pylintrc” dosyası içine:

[MESSAGES CONTROL]

disable=HATAKODU1,HATAKODU2

gibi yazabilirsiniz.
"""

A = 100
B = 50

class Siparis:
    """ Siparis modulu hakkinda
    bilgi girisini buraya yazabiliriz.
    siparis = Siparis('cins', miktar, fiyat)
    """
    # pylint: disable=too-many-instance-attributes
    # Bu durumda sekiz makuldur.

    kdv_orani = 18
    _kdvtoplami = []
    _aratoplam = []
    __satir_listesi = []

    liste = (["kavun",
              "karpuz",
              "cilek"], 2, 3, 4, "bes")

    def __init__(self, cins, miktar, fiyat):
        self.cins = cins
        self.miktar = float(miktar)
        self.fiyat = float(fiyat)
        self.tutar = (self.miktar * self.fiyat)
        self.kdv = (self.tutar * (self.kdv_orani / 100))
        self.toplam = (self.tutar + self.kdv)
        self.satirekle()

    def satirekle(self):
        """ satirekle fonksiyonu hakkinda
        bilgi...
        """
        self._kdvtoplami.append(self.kdv)
        self._aratoplam.append(self.tutar)
        self.satir = [self.cins,
                      self.miktar,
                      self.fiyat,
                      self.tutar,
                      self.kdv,
                      self.toplam]
        self.__satir_listesi.append(self.satir)
        self.sirano = len(self.__satir_listesi)
        print('%s- %s %s %s %s %s %s' %(self.sirano,
                                        self.cins,
                                        self.miktar,
                                        self.fiyat,
                                        self.tutar,
                                        self.kdv,
                                        self.toplam))

    @classmethod
    def satirsay(cls):
        """ satirsay fonksiyonu hakkinda
        bilgi...
        """
        cls.satir_sayisi = len(cls.__satir_listesi)
        return cls.satir_sayisi

    @classmethod
    def from_string(cls, emp_str):
        """Bu fonksiyon ile 'cins', 'miktar' ve 'fiyat' girilecektir.
        Kelime aralarina '-' isareti koyarak bu sekilde giriniz :
        from_string("cins miktar fiyat")
        """
        cins, miktar, fiyat = emp_str.split(' ')
        return cls(cins, miktar, fiyat)

    @classmethod
    def sonuc(cls):
        """ sonuc fonksiyonu hakkinda
        bilgi...
        """
        cls.kdvtoplami = 0
        cls.aratoplam = 0
        for i in range(len(cls._kdvtoplami)):
            cls.kdvtoplami += Siparis._kdvtoplami[i]
        for i in range(len(cls._aratoplam)):
            cls.aratoplam += Siparis._aratoplam[i]
        cls.geneltoplam = cls.kdvtoplami + cls.aratoplam
        atop = round(cls.aratoplam, 2)
        ktop = round(cls.kdvtoplami, 2)
        gtop = round(cls.geneltoplam, 2)
        print(atop)
        print(ktop)
        print(gtop)
        return (atop, ktop, gtop)

    @classmethod
    def giris(cls):
        """ Giris fonksiyonu hakkinda
        bilgi...
        """
        print("Siparis Programına hoşgeldiniz")
        Siparis.bilgi()
        Siparis.topla()
        sat = Siparis('Seramik', 12.96, 3.73)
        SATIR = Siparis('Bilgisayar', 3, 5) #pylint: disable = C0103
        print(SATIR.__repr__())
        print(SATIR.__str__())
        print(sat.__str__())
        Siparis.sonuc()

    @classmethod
    def demet(cls):
        """ demet fonksiyonu hakkinda
        bilgi...
        """
        cls.dem1, cls.dem2, cls.dem3, cls.dem4, cls.dem5 = cls.liste
        return (cls.dem1, cls.dem2, cls.dem3, cls.dem4, cls.dem5)

    @property
    def veri(self):
        """ veri fonksiyonu hakkinda
        bilgi...
        """
        return '{} {} {}'.format(self.cins,
                                 self.miktar,
                                 self.fiyat)

    @veri.setter
    def veri(self, value):
        if self.satir in Siparis._Siparis__satir_listesi:
            Siparis._aratoplam.remove(self.satir[3])
            Siparis._kdvtoplami.remove(self.satir[4])
            Siparis._Siparis__satir_listesi.remove(self.satir)
            cins, miktar, fiyat = value.split(' ')
            Siparis.from_string("%s %s %s" %(cins, miktar, fiyat))
            self.cins = cins
            self.miktar = float(miktar)
            self.fiyat = float(fiyat)
            tutar = (self.miktar * self.fiyat)
            kdv = (tutar * self.kdv_orani / 100)
            toplam = (tutar + kdv)
            self.satir = [cins,
                          float(miktar),
                          float(fiyat),
                          tutar,
                          kdv,
                          toplam]
            print('Veri guncellendi.')
        else:
            print('Veri güncellenemedi.')

    @veri.deleter
    def veri(self):
        if self.satir in Siparis._Siparis__satir_listesi:
            Siparis._aratoplam.remove(self.satir[3])
            Siparis._kdvtoplami.remove(self.satir[4])
            Siparis._Siparis__satir_listesi.pop()
            self.cins = None
            self.miktar = None
            self.fiyat = None
            self.satir = []
            print('Veri silindi.')
        else:
            print('Veri zaten silinmisdi.')

    @staticmethod
    def bilgi(value=BILGI):
        """ Bilgi fonksiyonu hakkinda
        bilgi girisini buraya yazabiliriz.

        Pylint ile yazım hatalarını denetleyebilirsiniz.
        """
        print(value)

    @staticmethod
    def topla():
        """ Islem fonksiyonu hakkinda
        bilgi girisini buraya yazabiliriz.
        """
        sonuc = A+B
        print(sonuc)

    def __repr__(self):
        return "Siparis('{}', '{}', {})".format(self.cins,
                                                self.miktar,
                                                self.fiyat)

    def __str__(self):
        return('%s- %s %s %s' %(self.sirano,
                                self.cins,
                                self.miktar,
                                self.fiyat))

    def __add__(self, other):
        return self.miktar + other

    def __len__(self):
        return len(self.cins)

#Run program
if __name__ == "__main__":
    Siparis.giris()
