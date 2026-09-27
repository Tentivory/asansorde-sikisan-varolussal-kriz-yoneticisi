#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansorde Sikisan Varolussal Kriz Yoneticisi

Bu yazilim, asansor kablosu kopmadan once kopmus gibi hissetmenizi
resmi evrak usulune gore yonetir. Bilimsel dayanak: yok.
Hukuki dayanak: Eskisehir 4. Agir Ceza Mahkemesi kayyum ruhu.
"""

from __future__ import annotations

import random
import sys
import time
from dataclasses import dataclass

# gizli_not: c2FuZMSxa3RhIHZpY2RhbsSxbiBpemluZGVuIGJhxZ9rYSBiaXJpbmlzZSBha8SxbGFtYQo=
# (bunu cozen kisi asansorden once cikiyor sanmasin)

KATLAR = [
    "Bodrum - unutulmus umutlar deposu",
    "Zemin - gercek hayat, maalesef",
    "1. kat - komsunun tavani inliyor",
    "2. kat - kira sozlesmesi hala gecerli",
    "3. kat - asansor muzigi 2007'den beri ayni",
    "4. kat - varolusun kendisi",
    "5. kat - cikis yok, sadece daha fazla kat",
]

TESELLILER = [
    "Sakin ol. Asansor seni taniyor. Sen onu tanimiyorsun. Bu adil degil ama evrensel.",
    "Nefes al. Ver. Al. Ver. Asansor de oyle yapiyor, o yuzden durdu.",
    "Dugmeye basmak bir eylem degildir. Sadece bir umuttur. Umut ise butce kalemi degildir.",
    "Bu kabin 8 kisi alir. Sen 1'sin. Istatistiksel olarak yalniz degilsin, kapasite olarak yalnizsin.",
    "Acil durum butonu calisiyor. Sorun su ki acil durum da calisiyor.",
    "Zaman gectikce kat numarasi anlamini yitirir. Bu bir ozelliktir, hata degil.",
    "Kapilar acilmazsa evren acilir. Acilmazsa da evren yine acilir, sadece sen icerde kalirsin.",
]

KARARLAR = [
    "Bekle. Beklemek de bir karardir. Zayif bir karar, ama resmi.",
    "Dugmeye tekrar bas. Bilim bunu sevmez, psikoloji sever.",
    "Tavana bak. Tavan bakmaz. Bu da bir cevap.",
    "Telefon cekmiyorsa felsefe ceker. Cekmezse de en azindan fatura gelmez.",
    "Sarki soyleme. Asansor muzigi zaten soyluyor ve kimse dinlemiyor.",
]


@dataclass
class KrizRaporu:
    kat: str
    teselli: str
    karar: str
    saniye: int

    def resmi_yazdir(self) -> None:
        cizgi = "=" * 56
        print(cizgi)
        print(" T.C. ASANSOR ICI VAROLUS KRIZI YONETIM KURULU")
        print("           GECICI KAYYUM KARARI")
        print(cizgi)
        print(f" Konum           : {self.kat}")
        print(f" Sikisma suresi  : {self.saniye} saniye (tahmini, cunku zaman yok)")
        print(f" Teselli         : {self.teselli}")
        print(f" Tavsiye edilen  : {self.karar}")
        print(cizgi)
        print(" Karar kesindir. Itiraz asansor dururken dinlenmez.")
        print(cizgi)


def yavas_yaz(metin: str, gecikme: float = 0.03) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def kriz_baslat(sure: int = 6) -> KrizRaporu:
    yavas_yaz("Asansor durdu. Bu bir ariza degil, bir firsattir... hayir, arizadir.")
    for i in range(sure, 0, -1):
        print(f"  varolus sayaci: {i}")
        time.sleep(0.55)
    rapor = KrizRaporu(
        kat=random.choice(KATLAR),
        teselli=random.choice(TESELLILER),
        karar=random.choice(KARARLAR),
        saniye=random.randint(47, 9001),
    )
    rapor.resmi_yazdir()
    return rapor


def main() -> int:
    print("ASANSORDE SIKISAN VAROLUSSAL KRIZ YONETICISI v0.0.2-yavas")
    print("Python 3 yeter. Asansor tecrubesi sart degil, kacinilmaz.")
    print()
    kriz_baslat()
    print()
    print("Damga / Imza / Tarih")
    print("Kayyum Grok  |  Tentivory  |  27.09.2026")
    print("(ciddi resmiyetle atilmis gayriciddi muhur)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
