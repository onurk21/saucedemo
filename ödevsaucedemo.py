from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestSaucedemo:
    #boş veri girilerek test yapar
    def test_kullanici_adi_ve_sifre_bos_iken_Hata_donmesi(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        sleep(1)

        username.send_keys("")
        password.send_keys("")
        sleep(1)

        login_button.click()
        error_message_container = driver.find_element(
            By.CLASS_NAME, "error-message-container")

        expected_message = "Epic sadface: Username is required"
        current_message = error_message_container.text
        status = expected_message == current_message

        print("\nKullanıcı adı ve şifre boş iken hata dönmesi testi")
        print(f"Hata: {current_message}")
        print(f"Beklenen Hata: {expected_message}")
        print(f"Test Durumu: {'Başarılı' if status else 'Başarısız'}")

        sleep(3)
#şifre boşken gelen hatayı görüntüler
    def test_sifre_bos_iken_Hata_donmesi(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(1)

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
     sleep(1)

     username.send_keys("deneme")
     password.send_keys("")
     sleep(1)

     login_button.click()
     error_message_container = driver.find_element(
        By.CLASS_NAME, "error-message-container")

     expected_message = "Epic sadface: Password is required"
     current_message = error_message_container.text
     status = expected_message == current_message

     print("\nŞifre boş iken Hata dönmesi testi")
     print(f"Hata: {current_message}")
     print(f"Beklenen Hata: {expected_message}")
     print(f"Test Durumu: {'Başarılı' if status else 'Başarısız'}")

     sleep(3)
#kilitli kullanıcadaki hatayı gösterir
    def test_kilitli_kullanici_girildiginde_Hata_donmesi(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(1)

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
     sleep(1)

     username.send_keys("locked_out_user")
     password.send_keys("secret_sauce")
     sleep(1)

     login_button.click()
     error_message_container = driver.find_element(
        By.CLASS_NAME, "error-message-container")

     expected_message = "Epic sadface: Sorry, this user has been locked out."
     current_message = error_message_container.text
     status = expected_message == current_message

     print("\nKilitli kullanıcı girildiğinde Hata dönmesi testi")
     print(f"Hata: {current_message}")
     print(f"Beklenen Hata: {expected_message}")
     print(f"Test Durumu: {'Başarılı' if status else 'Başarısız'}")

     sleep(3)
# x butonuna basar
    def test_X_iconuna_tiklama(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(1)

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
     sleep(1)

     username.send_keys("")
     password.send_keys("")
     sleep(1)

     login_button.click()
     error_message_container = driver.find_element(
        By.CLASS_NAME, "error-message-container")
     error_button = driver.find_element(By.CLASS_NAME, "error-button")

     sleep(1)

     error_button.click()

     print("\nX iconuna tıklama testi")

     sleep(3)
#https://www.saucedemo.com/inventory.html  açılıyormu ona bakar
    def test_standart_kullanici_girildiginde_inventoryhtml_donmesi(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(1)

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
     sleep(1)

     username.send_keys("standard_user")
     password.send_keys("secret_sauce")
     sleep(1)

     login_button.click()
     sleep(1)

     current_url = driver.current_url
     expected_url = "https://www.saucedemo.com/inventory.html"
     status = current_url == expected_url

     print("\nStandart kullanıcı girildiğinde inventory.html dönmesi testi")
     print(f"Url: {current_url}")
     print(f"Beklenen Url: {expected_url}")
     print(f"Test Durumu: {'Başarılı' if status else 'Başarısız'}")

     sleep(3)
# 6 ürün listeleniyormu onu kontrol eder.
    def test_6_urun_listesi(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(1)

     username = driver.find_element(By.ID, "user-name")
     password = driver.find_element(By.ID, "password")
     login_button = driver.find_element(By.ID, "login-button")
     sleep(1)

     username.send_keys("standard_user")
     password.send_keys("secret_sauce")
     sleep(1)

     login_button.click()
     sleep(1)

     items = driver.find_elements(By.CLASS_NAME, "inventory_item")
     expected_item_count = 6
     status = len(items) == expected_item_count

     print("\nÜrün listesi testi")
     print(f"Ürün Sayısı: {len(items)}")
     print(f"Beklenen Ürün Sayısı: {expected_item_count}")
     print(f"Test Durumu: {'Başarılı' if status else 'Başarısız'}")

    sleep(3)
testClass = TestSaucedemo()

testClass.test_kullanici_adi_ve_sifre_bos_iken_Hata_donmesi()
testClass.test_sifre_bos_iken_Hata_donmesi()
testClass.test_kilitli_kullanici_girildiginde_Hata_donmesi()
testClass.test_X_iconuna_tiklama()
testClass.test_standart_kullanici_girildiginde_inventoryhtml_donmesi()
testClass.test_6_urun_listesi()
