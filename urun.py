from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

''''
# Driver yolu
driver_yolu = "C:\\Users\\User\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe"

# tarayıcı 
options = webdriver.ChromeOptions()

# Driver başlatma 
service = Service(driver_yolu)
browser = webdriver.Chrome(service=service, options=options)

# Kulanıcı girişleri
kitap_adi = input("Kitap adı gir: ")
yayin = input("Yayınevi gir: ")
'''
# Kulanıcı girişleri
kitap_adi = input("Kitap adı gir: ")
yayin = input("Yayınevi gir: ")
 
def yurd(kitap_adi,yayin):
    # Driver yolu
 driver_yolu = "C:\\Users\\User\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe"

 # tarayıcı 
 options = webdriver.ChromeOptions()

 # Driver başlatma 
 service = Service(driver_yolu)
 browser = webdriver.Chrome(service=service, options=options)


 # Google sayfası
 browser.get("https://www.google.com")
 print("Sayfa başlığı:", browser.title)


 # Kitapyurdu araması 
 arama = browser.find_element("name", "q")
 arama.send_keys(kitap_adi + " " + yayin + " site:kitapyurdu.com")
 time.sleep(1)
 arama.send_keys(Keys.ENTER)
 time.sleep(3)


 try:
    bkm_tik = browser.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a")
    bkm_tik.click()
 except Exception as e:
    print("Bağlantı bulunamadı:", e)
    browser.quit()
    exit()

 # Sayfa yüklenene kadar bekle
 time.sleep(2)

 # Sayfa kaynağını al ve BeautifulSoup ile işle
 bkm_sayfa = browser.page_source
 bkm_soup = BeautifulSoup(bkm_sayfa, "lxml")

 # Kitap adını al
 try:
    bkm_bilgi = bkm_soup.find("div", attrs={"class": "pr_header"})
    bkm_ad = bkm_bilgi.find("h1").text.strip()
    print("Kitap Adı:", bkm_ad)
 except Exception as e:
    print("Kitap bilgisi alınamadı:", e)
    browser.quit()
 # Fiyat bilgisini al
 try:
    bkm_sayi = bkm_soup.find("div", attrs={"class": "pr_price"})
    price_div = bkm_sayi.find("div", class_="price__item")
    price_text = price_div.text.strip()  # Tüm metni al
    price_main = price_text.split(',')[0].strip()  # Virgülden önceki kısmı al
    return price_main
 except Exception as e:
    print("Fiyat bilgisi alınamadı:", e)
    
    
def dr(kitap_adi,yayin):
 # Driver yolu
 driver_yolu = "C:\\Users\\User\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe"

# tarayıcı 
 options = webdriver.ChromeOptions()

 # Driver başlatma 
 service = Service(driver_yolu)
 browser = webdriver.Chrome(service=service, options=options)
 
  # Google sayfası
 browser.get("https://www.google.com")
 print("Sayfa başlığı:", browser.title)


 # Kitapyurdu araması 
 arama = browser.find_element("name", "q")
 arama.send_keys(kitap_adi + " " + yayin + " site:dr.com.tr")
 time.sleep(1)
 arama.send_keys(Keys.ENTER)
 time.sleep(3)


 try:
    dr_tik = browser.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a")
    dr_tik.click()
 except Exception as e:
    print("Bağlantı bulunamadı:", e)
    browser.quit()
    exit()

 # Sayfa yüklenene kadar bekle
 time.sleep(2)

 # Sayfa kaynağını al ve BeautifulSoup ile işle
 dr_sayfa = browser.page_source
 dr_soup = BeautifulSoup(dr_sayfa, "lxml")       
 
 dr_b=dr_soup.find("h1",attrs={"class":"fs-7 mb-0 js-text-prd-name"}).text
 print(dr_b)
 dr_f=dr_soup.find("span",attrs={"class":"current-price js-text-current-price"}).text
 return dr_f


def bkm(kitap_adi,yayin):
 # Driver yolu
 driver_yolu = "C:\\Users\\User\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe"

# tarayıcı 
 options = webdriver.ChromeOptions()

 # Driver başlatma 
 service = Service(driver_yolu)
 browser = webdriver.Chrome(service=service, options=options)

  # Google sayfası
 browser.get("https://www.google.com")
 print("Sayfa başlığı:", browser.title)


 # Kitapyurdu araması 
 arama = browser.find_element("name", "q")
 arama.send_keys(kitap_adi + " " + yayin + " site:bkmkitap.com")
 time.sleep(1)
 arama.send_keys(Keys.ENTER)
 time.sleep(3)


 try:
    yurd_tik = browser.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a")
    yurd_tik.click()
 except Exception as e:
    print("Bağlantı bulunamadı:", e)
    browser.quit()
    exit()

 # Sayfa yüklenene kadar bekle
 time.sleep(2)

 # Sayfa kaynağını al ve BeautifulSoup ile işle
 yurd_sayfa = browser.page_source
 yurd_soup = BeautifulSoup(yurd_sayfa, "lxml")       
 
 yurd_b=yurd_soup.find("h1",attrs={"class":"fw-bold"}).text
 print(yurd_b)
 yurd_f=yurd_soup.find("span",attrs={"class":"product-price"}).text
 return yurd_f


fbkm=bkm(kitap_adi,yayin)
fyurd=yurd(kitap_adi,yayin)
fdr=dr(kitap_adi,yayin)
print(fbkm)
print(fdr)
print(fyurd)


ucuz = f"{fdr} D&R " if fdr < fyurd and fdr < fbkm else (f"{fyurd} BKM" if fyurd < fbkm else f"{fbkm} KıTAPYURDU")

print("en ucuz:",ucuz)

