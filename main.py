from selenium import webdriver
import time

from selenium.webdriver import Keys

chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://www.xrtoday.com/")
time.sleep(3)

article = []
b= []
link = []

# article = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/h2/a")
article = driver.find_elements_by_xpath('//div[@class="single_blog-container"]')

for i in range(len(article)):
    title = article[i].text
    href = article[i].get_attribute('href')
    b.append(title)
    link.append(href)

print(link)

# print(article[0].text)

# #Twitter bot

driver.get("https://twitter.com/i/flow/login")
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.switch_to.window(driver.window_handles[1])

description = "#nft #surrealart #psychedelic #gan #ayahuasca #localtip #pintrading #pinmail #nfs #disneylandpins #ap #strangeart #psilocybin #digitalart #5dart #discoverla #pintrader #le #awesomefriends #aiw #sanpedro #pixelart #cryptoart #music #chinesemusic #pinstagram"

time.sleep(12)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

login = driver.find_element_by_xpath('//input[@name="text"]')
login.send_keys("umang.rke333@gmail.com")
# next_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span')
login.send_keys(Keys.ENTER)
time.sleep(12)
username = login = driver.find_element_by_xpath('//input[@name="text"]')
login.send_keys("5_Umang")
login.send_keys(Keys.ENTER)
time.sleep(8)
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys("Eternitymoon01!")
password.send_keys(Keys.ENTER)
time.sleep(5)

status = driver.find_element_by_xpath('//div[@aria-label="Tweet text"]')
status_text = b[2]+ ' ' + description
if len(status_text) > 280:
    status_text = status_text[0:260]
status_text = status_text + ' ' + "Follow Back"
status.send_keys(status_text)
time.sleep(2)
status_button_tweet = driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]')
status_button_tweet.send_keys(Keys.ENTER)
print(status_text)
time.sleep(5)


driver.quit()
