import os
print("---SÜRELİ PC KAPATMA PROGRAMINA HOŞ GELDİNİZ---")
x=input("PC kapanma süresini dakika cinsinden giriniz : ")
y=int(x)
y*=60
y=str(y)
print("Bilgisayarınız ",x," dakika içerisinde kapanacaktır...")
os.system(
    command='shutdown -s -f -t '+y
)
