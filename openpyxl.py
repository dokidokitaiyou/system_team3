from selenium import webdriver
import chromedriver_binary 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#バックグラウンドオプションなし
option = Options()                          # オプションを用意
option.add_argument('--headless')           # ヘッドレスモードの設定を付与
browser = webdriver.Chrome(options=option)   # Chromeを準備(optionでヘッドレスモードにしている）



#関数
def search(KEYWORD):
    
    browser.get('https://www.google.com/search')
    search_box = browser.find_elements(By.CLASS_NAME,"gLFyf")[0]
    search_box.send_keys(KEYWORD + Keys.ENTER)
    featured_snippets = browser.find_elements(By.CLASS_NAME,"LGOjhe")
    return featured_snippets

text = search("キリン")
print(text[0].text)

browser.quit()
#References:
# https://lusknote.com/542
#https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760
#https://watlab-blog.com/2019/08/18/selenium-chrome-background/