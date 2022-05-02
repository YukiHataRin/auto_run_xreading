from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import json
import threading
import keyboard

def leave():
    global driver
    keyboard.wait("ctrl + p")
    print("程式強制結束")
    driver.quit()
    os._exit(0)

if os.path.isfile("setting.json"):  
    with open("setting.json", 'r', encoding = 'utf8') as jfile:
        jdata = json.load(jfile)
    
else:
    with open("setting.json", 'w', encoding = 'utf8') as jfile:
        jdata = dict()
        jdata['username'] = input("請輸入帳號")
        jdata['password'] = input("請輸入密碼")
        jdata['time'] = input("請輸入多少秒換一頁")
        json.dump(fp = jfile, obj = jdata, indent = 4, ensure_ascii = False)
        
threadingobj = threading.Thread(target = leave, daemon = True)
threadingobj.start()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://xreading.com/login/index.php")
time.sleep(1)
driver.find_element(by = By.NAME, value = "username").send_keys(jdata['username'])
driver.find_element(by = By.NAME, value = "password").send_keys(jdata['password'])
driver.find_element(by = By.NAME, value = "password").submit()
os.system("pause")
url = driver.current_url
status = 1
count = 0

while(status):
    if (url != driver.current_url):
        print("網址已離開閱讀網域 程式結束")
        break

    try:
        time.sleep(int(jdata['time']))

        for i in driver.find_elements(by = By.TAG_NAME, value = 'button'):
            if i.text == "Next":
                status = 1
                i.click()
                break
            
            status = 0

        count += 1
        print(f"目前翻了 {count} 頁")
        
    
    except:
        print("出現未知錯誤，程式結束")
        os._exit(0)
        count = 0

print('程式結束')
driver.quit()
os.system("pause")
