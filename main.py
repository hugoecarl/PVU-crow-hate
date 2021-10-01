from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import ctypes
import pathlib

class SeleniumConf:           
    def __init__(self):
        self.driver = None
        
    def start(self):
        options = Options()
        #options.add_argument('--headless')
        #options.add_argument('--disable-dev-shm-usage')
        #options.add_argument('--disable-gpu')
        options.add_extension("10.1.1_0.crx")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        scriptDirectory = pathlib.Path().absolute()
        #options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
        options.add_argument("user-data-dir=C:\\Users\\hugoc\\Desktop\\nenos")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        self.driver.get("https://marketplace.plantvsundead.com/farm#/farm")
        return self.driver
        
    def enter_chat(self, tar):
        target = tar
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()
    
    def send_message(self, msg):
        string = msg
        inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
        input_box = self.driver.find_element_by_xpath(inp_xpath)
        time.sleep(3)
        input_box.send_keys(string + Keys.ENTER)


class PVUProgram:
    def __init__(self, Selenium):
        self.selenium = Selenium
        self.driver = self.selenium.start()

    def main(self):
        print("Inicializando Driver acesse conta PVU...")
        time.sleep(60)
        while True:
            self.driver.get("https://marketplace.plantvsundead.com/farm#/farm")
            print("Analisando plantação...")
            time.sleep(60)
            soup = BeautifulSoup(self.selenium.driver.page_source, "html.parser")
            land = soup.find_all("img", src='/_nuxt/img/land_3d.34549cc.svg')
            crow = soup.find_all("img", src="/_nuxt/img/crow-bede.acf7459.png")
            time_plant = soup.find_all("p", class_="tw-text-white time small")

            for i in land:
                try:
                    if i['style'] == 'display: none;':
                        print('\007')
                        ctypes.windll.user32.MessageBoxW(0, "Water", "PVU warning", 1)
                        print("Plantas precisam de água abrindo whats pra avisar...")
                        self.driver.get("https://web.whatsapp.com/")
                        time.sleep(30)
                        print("Entrando no chat...")
                        self.selenium.enter_chat('"PVU avisos"')
                        time.sleep(10) 
                        self.selenium.send_message("Águe as plantinhas brother!")
                        print("Mensagem enviada.")
                        break
                except:
                    pass 

            for i in crow:
                try:
                    if i['style'] == 'display: none;':
                        pass
                except:
                    print('\007')
                    ctypes.windll.user32.MessageBoxW(0, "Crow", "PVU warning", 1)
                    print("Corvos abrindo whats pra avisar...")
                    self.driver.get("https://web.whatsapp.com/")
                    time.sleep(30)
                    print("Entrando no chat...")
                    self.selenium.enter_chat('"PVU avisos"')
                    time.sleep(10) 
                    self.selenium.send_message("Corvos malditos na plantação!")
                    print("Mensagem enviada.")
                    break
            
            for i, j in enumerate(time_plant):
                print(f"Tempos para colheita {j.text}")
                if int(j.text.replace(':', '')) <= 3:
                    print('\007')
                    ctypes.windll.user32.MessageBoxW(0, "Harvest", "PVU warning", 1)
                    print("Hora da colheita whats pra avisar...")
                    self.driver.get("https://web.whatsapp.com/")
                    time.sleep(30)
                    print("Entrando no chat...")
                    self.selenium.enter_chat('"PVU avisos"')
                    time.sleep(5) 
                    self.selenium.send_message(
                        f"Faltam {int(j.text.replace(':', ''))} minutos para colher a planta {i}")
                    print("Mensagem enviada.")

            time.sleep(60)


if __name__=="__main__":
    selenium = SeleniumConf()
    helper = PVUProgram(selenium)
    helper.main() 