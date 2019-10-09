import random
print("1-Taş")
print("2-Kağıt")
print("3-Makas")
kullanıcı = int(input("1 ile 3 arası bir sayı seçiniz : "))
pc = random.randrange(3)+1
print("Bilgisayarın seçimi : ",random.randrange(3)+1)
if (kullanıcı == 1 and pc == 2) or (kullanıcı == 2 and pc == 3) or (kullanıcı == 3 and pc == 1):
    print("Kaybettiniz")
elif (kullanıcı == 1 and pc == 3) or (kullanıcı == 2 and pc == 1) or (kullanıcı == 3 and pc == 2):
    print("Kazandınız")
elif kullanıcı == pc:
    print("Berabere")
else:
    print("Geçersiz Girdi")