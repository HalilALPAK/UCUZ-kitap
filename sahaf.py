from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
 
def nadir(kitap_adi,yayin):
    # Driver yolu
 driver_yolu = "C:\\Users\\User\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe"

 # tarayıcı 
 options = webdriver.ChromeOptions()

 # Driver başlatma 
 service = Service(driver_yolu)
 browser = webdriver.Chrome(service=service, options=options)


 # Google sayfası
 browser.get("https://www.google.com")
 print("Sayfa başligi:", browser.title)


 # nadir araması 
 arama = browser.find_element("name", "q")
 arama.send_keys(kitap_adi + " " + yayin + " site:kitapsahaf.net")
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
 nadir_sayfa = browser.page_source
 nadir_soup = BeautifulSoup(nadir_sayfa, "lxml")

 time.sleep(2)
  # Site içindeki arama kutusunu bul ve ilk aramayı yap
 search_box = browser.find_element(By.NAME, "q")  # Kitapyurdu'ndaki arama kutusunun 'name' değeri
 search_box.send_keys(kitap_adi)
 search_box.send_keys(Keys.ENTER)
 time.sleep(3)

 # Dropdown menüyü aç
 dropdown_button = browser.find_element(By.NAME, "sort_type")  # Tıklanabilir alanın doğru sınıf adını  kontrol edin
 #dropdown_button.click()  # Menü açılır

 time.sleep(1)  # Menü açıldıktan sonra bekleme (  gerekirse)

 # İlgili seçeneği seçme (örneğin 'Fiyata göre artan')
 option = browser.find_element(By.XPATH, "//*[@id='prd_filter']/div/select[2]/option[10]")  # XPATH doğru olmalı
 option.click()

 # Eğer tıklanabilir değilse alternatif:
 #browser.execute_script("arguments[0].click();", option)  # JavaScript ile tıklama

 time.sleep(3)
 # Fiyat bilgisini al
 try:
    # Fiyatı çekmek için doğru elementi bekleyin
    nadir_sayi = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "dy_indirimli"))
    )
    #nadir_sayi= nadir_soup.find("span", attrs={"class":"dy_indirimli"})
    #print(nadir_sayi)
    price_main = nadir_sayi.text.split(',')[0].strip()  # Virgülden önceki kısmı al
    print("aa")
 except Exception as e:
    print("Fiyat alınamadı:", e)
    
    
 # Sepet linkine tıklama
 try:
    sepet_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "cart_prd_view_865134"))
    )
    sepet_link.click()
    print("Sepete eklendi.")
 except Exception as e:
    print(f"Hata: {e}")
 
 return price_main
    
    
fnadir=nadir(kitap_adi,yayin)
print(fnadir)  

