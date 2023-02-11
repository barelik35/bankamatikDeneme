barisHesap = {
  "ad": "Barış Çelik",
  "hesapNo": "214785",
  "bakiye": 3000,
  "ekHesap": 2000
}

gunnurHesap = {
  "ad": "Günnur Çelik",
  "hesapNo": "132548",
  "bakiye": 3000,
  "ekHesap": 2000
}


def paraCek(hesap, miktar):
  print(f"Merhaba {hesap['ad']}")
  if (hesap["bakiye"] >= miktar):
    hesap["bakiye"] -= miktar
    print("Paranızı alabilirsiniz.")
  else:
    toplam = hesap["bakiye"] + hesap["ekHesap"]
    if (toplam >= miktar):
      ekHesapKullanimi = input("Ek hesap kullanmak istermisiniz ? (E/H)")
      if (ekHesapKullanimi == "E"):
        ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
        hesap["bakiye"] = 0
        hesap["ekHesap"] -= ekHesapKullanilacakMiktar
        print("Paranızı alabilirsiniz.")
      else:
        print(
          f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır."
        )
    else:
      print("Üzgünüz bakiyeniz yetersiz.")


def bakiyeSorgula(hesap):
  print(
    f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bakiye bulunmakdatır. Ek hesabınızda {hesap['ekHesap']} TL bakiye bulunmaktadır."
  )


paraCek(barisHesap, 4000)
bakiyeSorgula(barisHesap)
