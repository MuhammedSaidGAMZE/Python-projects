while True:
    print("OYUNUMUZA HOŞGELDİNİZ 10 DENEME HAKKINIZ VARDIR BAKALIM KAÇ PUAN ALICAKSINIZ ? ")
    import random
    sayi=random.randint(1,100)
    deneme_hakki = 10
    puan = 100
    while deneme_hakki > 0:
        tahmin=int(input("1 ile 100 arasında komuta göre sayı arttırın veya azaltın  :  "))
        if tahmin > sayi : 
            print("Sayıyı  en düşük 1 olmak şartıyla azaltın ")
            puan -= 10
        elif tahmin < sayi : 
            print("Sayıyı en fazla 100 olmak şartıyla arttırın ")
            puan -= 10
        else:
            print("Doğru buldunuz tebrikler!!!")
            print("Puanınız: ", puan)
            break
        deneme_hakki -= 1
        if deneme_hakki == 0:
            print("Deneme hakkınız bitti. Doğru sayı: ", sayi)

