# İki sayılı hesaplamalar için girilen stringi string.split() komutuyla ikiye bölüp hesaplayan bir hesap
# makinesi programı:
while True:
    hesap_makinesi = input("Yapılacak işlemi giriniz: ")

    if "+" in hesap_makinesi:
        sayilar = hesap_makinesi.split("+")
        sonuc = int(sayilar[0]) + int(sayilar[1])

    elif "-" in hesap_makinesi:
        sayilar = hesap_makinesi.split("-")
        sonuc = int(sayilar[0]) - int(sayilar[1])

    elif "*" in hesap_makinesi:
        sayilar = hesap_makinesi.split("*")
        sonuc = int(sayilar[0]) * int(sayilar[1])

    elif "/" in hesap_makinesi:
        sayilar = hesap_makinesi.split("/")
        sonuc = int(sayilar[0]) / int(sayilar[1])

    else:
        print("Geçersiz işlem")
        continue

    print("Sonuç:", sonuc)

    devam = input("Yeni işlem için 'e', çıkmak için başka bir tuşa basın: ")

    if devam != "e":
        break
