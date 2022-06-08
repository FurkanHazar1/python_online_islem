kişi={}
i=0
bakiye=0
import random
def isValidTCID(value):
    value = str(value)
    if not len(value) == 11:
        return False
    if not value.isdigit():
        return False
    if int(value[0]) == 0:
        return False
    digits = [int(d) for d in str(value)]

    if not sum(digits[:10]) % 10 == digits[10]:
        return False

    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False

    return True
while True:
    islem = input("\nHesap Açmak İçin 1'i \nBakiye Sorgulamak İçin Lütfen 2'yi \nPara Yatırmak İçin 3'ü \n"
                  "Para Çekmek İçin 4'ü \nHavale İşlemi İçin 5'i Tuşlayınız\n"
                  "Devam Etmek İstemiyorsanız ENTER Tuşuna Basınız: ")
    islemler=0
    if islem=='1':
        Tc=input("\nLütfen Tc Kimlik Numaranızı Giriniz: ")
        if isValidTCID(Tc):
            isim=input("Lütfen İsminizi Giriniz: ")
            soyisim= input("Lütfen Soyisminizi Giriniz: ")
            HesapNo=str(random.randrange(10000,99999))
            kişi[HesapNo]={
                'Tc': Tc,
                'İsim':isim,
                'Soyisim':soyisim,
                'Bakiye':int(bakiye)
            }
            devam=input(f"\nHesabınız Oluşturulmuştur Sayın {kişi[HesapNo]['İsim']} {kişi[HesapNo]['Soyisim']} "
                        f"\nHesap Numaranız: {HesapNo}\nDevam Etmek İçin 1 Tuşuna Çıkış Yapmak İçin ENTER Tuşuna Basınız: ")
            if devam !='1':
                break
            else:
                continue
        else:
            print("Girdiğiniz Tc Kİmlik Numarası Geçerli Bir Numara Değildir!!"
                  " Tekrardan İşlem Ekranına Yönlendiriliyorsunuz")
            continue
    elif islem=='2':
        HesapNo=input("\nBakiyenizi Görüntülemek İçin lütfen Hesap Numaranızı Giriniz: ")
        if HesapNo in kişi:
            islem = input(f"{HesapNo} Hesap Numaralı Kişinin Hesap Bakiyesi = {kişi[HesapNo]['Bakiye']} \n "
                          f"Yapmak İstediğiniz İşlemi Seçiniz\n\n"
                          f"Para Yatırmak İçin 3'ü Tuşlayınız\n Para Çekmek İçin 4'ü Tuşlayınız\n"
                            f"Havale İşlemi İçin 5'i Tuşlayınız\nÇıkış Yapmak için ENTER Tuşuna Basınız: ")
        else:
            print("\nGirdiğiniz Hesap Numarası Sistemde Bulunmamaktadır İşlem Ekranına Yönlendiriliyorsun\n")
            continue
    if islem=='3' or islem =='4' or islem=='5' or islem=='':
        if islem=='3':
            HesapNo=input("\nLütfen Hesap Numaranızı Giriniz: ")
            if HesapNo in kişi:
                bakiye=kişi[HesapNo]['Bakiye']
                Yatirma=int(input("\nLütfen Yatırmak İstediğiniz Miktarı Giriniz: "))
                bakiye+=Yatirma
                kişi[HesapNo]['Bakiye']=bakiye
                devam=input(f"\nSayın {kişi[HesapNo]['İsim']} {kişi[HesapNo]['Soyisim']} Yatırma işleminiz Başarıyla Gerçekleşmiştir\n"
                            f"Hesap Bakiyeniz: {kişi[HesapNo]['Bakiye']}\n\n"
                            f"İşlem Ekranına Dönemk İçin 1 Tuşuna Çıkış Yapmak İçin ENTER Tuşuna Basınız: ")
                if devam!='1':
                    break
                else:
                    continue
            else:
                print("\nGirdiğiniz Hesap Numarası Sistemde Bulunmamaktadır İşlem Ekranına Yönlendiriliyorsunuz\n")
                continue
        elif islem=='4':
            HesapNo=input("Lütfen Hesap Numaranızı Giriniz: ")
            if HesapNo in kişi:
                cekme=int(input(f"Sayın {kişi[HesapNo]['İsim']} {kişi[HesapNo]['Soyisim']} Hesap Bakiyeniz = {kişi[HesapNo]['Bakiye']}\n"
                                f"Lütfen Çekmek İstediğiniz Miktarı Giriniz: "))
                if cekme<=bakiye:
                    bakiye=kişi[HesapNo]['Bakiye']
                    bakiye-=cekme
                    kişi[HesapNo]['Bakiye']=bakiye
                    print("\nprrrrrrrrrttt\n")
                    devam = input( f"\nSayın {kişi[HesapNo]['İsim']} {kişi[HesapNo]['Soyisim']} "
                                   f"Para Çekme işleminiz Başarıyla Gerçekleşmiştir\nHesap Bakiyeniz: {kişi[HesapNo]['Bakiye']}\n\n"
                        f"İşlem Ekranına Dönemk İçin 1 Tuşuna Çıkış Yapmak İçin ENTER Tuşuna Basınız: ")

                else:
                    print("\nHesabınızda Çekmek İstediğiniz Miktarda Para Bulunmamaktadır İşlem Ekranına Yönlendiriliyorsunuz\n")
                    continue
                if devam!='1':
                    break
                else:
                    continue
            else:
                print("\nGirdiğiniz Hesap Numarası Sistemde Bulunmamaktadır İşlem Ekranına Yönlendiriliyorsun\n")
                continue

        elif islem=='5':
            HesapNo=input("Lütfen Hesap Numaranızı Giriniz: ")
            if HesapNo in kişi:
                HesapNo2=input("Lütfen Havale Yapmak İstediğiniz Hesabın Hesap Numarasını Giriniz: ")
                if HesapNo2 in kişi:
                        Havale=int(input("Lütfen Havale Yapmak İstediğiniz Para Miktarını Giriniz: "))
                        if Havale<=kişi[HesapNo]['Bakiye']:
                            bakiye=kişi[HesapNo]['Bakiye']
                            bakiye-=Havale
                            kişi[HesapNo]['Bakiye']=bakiye
                            bakiye=kişi[HesapNo2]['Bakiye']
                            bakiye+=Havale
                            kişi[HesapNo2]['Bakiye']=bakiye
                            devam=input("Havale İşleminiz Başarıyla Gerçekleştirilmiştir\n"
                                  f"Hesap Bakiyeniz = {kişi[HesapNo]['Bakiye']}Tl\n"
                                  f"{kişi[HesapNo2]['İsim']}={kişi[HesapNo2]['Bakiye']}\n"
                                        f"Devam Etmek İstiyorsanız 1 Tuşuna basınız İstemiyorsanız ENTER Tusşuna Basınız: ")
                            if devam != '1':
                                break
                            else:
                                continue
                        else:
                            print("Hesabınızda Bu Miktarda Para Bulunmamaktadır İşlem Ekranına Yönlendiriliyorsunuz")
                            continue
                else:
                    print("Hatalı Hesap Numarası Girdiniz İşlem Ekranına Yölendiriliyorsunuz")
                    continue
            else:
                print("Hatalı Hesap Numarası Girdiniz İşlem Ekranına Yölendiriliyorsunuz")
                continue
        elif islem=='':
            break
    else:

        print("\nHatalı Numara Girdiniz: ")
print("ÇıKış Yapılmıştır")