import requests
from bs4 import BeautifulSoup

# Veriyi çekmek istediğiniz URL'i belirleyin
url = "https://weather.com/tr-TR/kisisel/bugun/l/TUXX0002:1:TU?Goto=Redirected"

# GET isteği gönderin
response = requests.get(url)

# Yanıtın başarılı olup olmadığını kontrol edin
if response.status_code == 200:
    # Yanıt verisini BeautifulSoup ile parse edin
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Çekmek istediğiniz elementleri belirleyin
    Yer = soup.find(class_='CurrentConditions--location--1YWj_')
    Zaman = soup.find(class_='CurrentConditions--timestamp--1ybTk')
    Sıcaklık = soup.find(class_='CurrentConditions--tempValue--MHmYY')
    Nem = soup.find(class_='WeatherDetailsListItem--wxData--kK35q')
    Basınç = soup.find(class_='Pressure--pressureWrapper--3SCLm undefined')
    Rüzgar = soup.find(class_='Wind--windWrapper--3Ly7c undefined')
    Günes_Dogus = soup.find(class_='SunriseSunset--dateValue--3H780')
    
    # Elementlerin içeriğini ekrana yazdırın
    if Yer:
        print("Yer:", Yer.text.strip())
    if Zaman:
        print("Zaman:", Zaman.text.strip())
    if Sıcaklık:
        print("Sıcaklık:", Sıcaklık.text.strip())
    if Nem:
        print("Nem:", Nem.text.strip())
    if Basınç:
        print("Basınç:", Basınç.text.strip())
    if Rüzgar:
        print("Rüzgar Hızı:", Rüzgar.text.strip())
    if Günes_Dogus:
        print("Günesin Doğuşu:", Günes_Dogus.text.strip())


    # Kullanıcıdan veri kaydetme seçeneğini sormak
    kaydet = input("Verileri kaydetmek istiyor musunuz? (E/H): ")
    if kaydet.upper() == "E":
        # Verileri dosyaya kaydetme
        with open("hava_durumu.txt", "w") as dosya:
            dosya.write("Yer: {}\n".format(Yer.text.strip()))
            dosya.write("Zaman: {}\n".format(Zaman.text.strip()))
            dosya.write("Sıcaklık: {}\n".format(Sıcaklık.text.strip()))
            dosya.write("Nem: {}\n".format(Nem.text.strip()))
            dosya.write("Basınç: {}\n".format(Basınç.text.strip()))
            dosya.write("Rüzgar Hızı: {}\n".format(Rüzgar.text.strip()))
            dosya.write("Günesin Doğuşu: {}\n".format(Günes_Dogus.text.strip()))
        print("Veriler hava_durumu.txt dosyasına kaydedildi.")
else:
    print("Hata: İstenilen bilgiler dosyaya kaydedilemedi üzgünüz")