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
    Basınc = soup.find(class_='Pressure--pressureWrapper--3SCLm undefined')
    Rüzgar = soup.find(class_='Wind--windWrapper--3Ly7c undefined')
    Günes_Dogus = soup.find(class_='SunriseSunset--dateValue--3H780')
    Hava_Kalitesi_İndexi0 = soup.find(class_='AirQuality--col--3I-4C')
    Hava_Kalitesi_İndexi1 = soup.find(class_='AirQualityText--AirQuality--2uuF7')
    Saglık_Aktiviteler = soup.find(class_='HealthActivitiesListItem--details--3xbqs')

    if Yer:
        print("Yer:", Yer.text.strip())
    if Zaman:
        print("Zaman:", Zaman.text.strip())
    if Sıcaklık:
        print("Sıcaklık:", Sıcaklık.text.strip())
    if Nem:
        print("Nem:", Nem.text.strip())
    if Basınc:
        print("Basınç:", Basınc.text.strip())
    if Rüzgar:
        print("Rüzgar Hızı:", Rüzgar.text.strip())
    if Günes_Dogus:
        print("Günesin Doğuşu:", Günes_Dogus.text.strip())
    if Hava_Kalitesi_İndexi0:
        print("Hava Kalitesi: %" + Hava_Kalitesi_İndexi0.text.strip(), end=" ")
    if Hava_Kalitesi_İndexi1:
        print("" + Hava_Kalitesi_İndexi1.text.strip())

    if Saglık_Aktiviteler:
        print("Sağlık Önerileri :", Saglık_Aktiviteler.text.strip())
else:
    print("Hava durumu verileri alınamadı. Hata kodu:", response.status_code)

with open("hava_durumu.txt", "w") as file:
    # Verileri dosyaya yazın
    if Yer:
        file.write("Yer: " + Yer.text.strip() + "\n")
    if Zaman:
        file.write("Zaman: " + Zaman.text.strip() + "\n")
    if Sıcaklık:
        file.write("Sıcaklık: " + Sıcaklık.text.strip() + "\n")
    if Nem:
        file.write("Nem: " + Nem.text.strip() + "\n")
    if Basınc:
        file.write("Basınç: " + Basınc.text.strip() + "\n")
    if Rüzgar:
        file.write("Rüzgar Hızı: " + Rüzgar.text.strip() + "\n")
    if Günes_Dogus:
        file.write("Güneşin Doğuşu: " + Günes_Dogus.text.strip() + "\n")
    if Hava_Kalitesi_İndexi0:
        file.write("Hava Kalitesi: %" + Hava_Kalitesi_İndexi0.text.strip() + " " + Hava_Kalitesi_İndexi1.text.strip() + "\n")
    if Saglık_Aktiviteler:
        file.write("Sağlık Önerileri: " + Saglık_Aktiviteler.text.strip() + "\n")
# Kullanıcıdan dosyanın kaydedilip kaydedilmeyeceğini sormak için girdi alın
cevap = input("Dosya kaydedilsin mi? (E/H): ")

# Kullanıcının cevabına göre dosyayı kaydedin veya kaydetmeyin
if cevap.lower() == "e":
    print("Dosya kaydedildi.")
else:
    print("Dosya kaydedilmedi.")
