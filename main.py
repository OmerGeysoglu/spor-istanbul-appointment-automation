from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os

# driver options for heroku
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
ser = Service("CHROMEDRIVER_PATH")
chrome_options.add_argument("--headless")
# increase window size to make buttons visible
chrome_options.add_argument("window-size=1200x600")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=ser, options=chrome_options)

driver.get("https://online.spor.istanbul/")

# pop-up close
driver.find_element(By.XPATH,"//button[normalize-space()='Kapat']").click()
#Login
driver.find_element(By.XPATH,"//a[contains(text(),'Üye Giriş')]").click()

#forms
tc_input = driver.find_element(By.CSS_SELECTOR,"#txtTCPasaport")
tc_input.send_keys("TC_NUMBER")
pass_input = driver.find_element(By.CSS_SELECTOR,"#txtSifre")
pass_input.send_keys("YOUR_PASS")

driver.find_element(By.CSS_SELECTOR,"#btnGirisYap").click()
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

my_sessions = driver.find_element(By.XPATH,"//div[contains(@class,'page-header-menu')]//div[contains(@class,'container-fluid')]//div[contains(@class,'')]//ul[contains(@class,'nav navbar-nav')]//li//a[contains(@href,'uyespor.aspx')][contains(text(),'Seanslarım')]")
my_sessions.click()
pick_sessions_btn = driver.find_element(By.CSS_SELECTOR,"#pageContent_rptListe_lbtnSeansSecim_0")
pick_sessions_btn.click()


from twilio.rest import Client
account_sid = 'YOUR_SID'
auth_token = 'YOUR_TOKEN'

def send_message():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:YOUR_SENDER_TWILIO_NUMBER',
    body='There are available sessions!',
    to='whatsapp:YOUR_PHONE_NUMBER'
    )
    print(message.sid)


available_sessions = driver.find_elements(By.XPATH,"//div[@class='form-group']//span[contains(text(),'Başlangıç')]/following-sibling::label[contains(text(),'Yer')]")
print(available_sessions)

if(len(available_sessions)>0):
    send_message()


    
