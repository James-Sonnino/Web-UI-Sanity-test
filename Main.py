#TODO: watch video
# add subject from picture
# pods
# page is up
# plus all the stuff in the list

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = "https://bt-anv.tls.ai"
rtsp = "rtsp://root:pass@192.168.20.230/axis-media/media.amp"


##########################################

def intro():
    print("""Welcome to the

        NNNNNNNN        NNNNNNNN               AAA                 SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT
        N:::::::N       N::::::N              A:::A              SS:::::::::::::::ST:::::::::::::::::::::T
        N::::::::N      N::::::N             A:::::A            S:::::SSSSSS::::::ST:::::::::::::::::::::T
        N:::::::::N     N::::::N            A:::::::A           S:::::S     SSSSSSST:::::TT:::::::TT:::::T
        N::::::::::N    N::::::N           A:::::::::A          S:::::S            TTTTTT  T:::::T  TTTTTT
        N:::::::::::N   N::::::N          A:::::A:::::A         S:::::S                    T:::::T        
        N:::::::N::::N  N::::::N         A:::::A A:::::A         S::::SSSS                 T:::::T        
        N::::::N N::::N N::::::N        A:::::A   A:::::A         SS::::::SSSSS            T:::::T        
        N::::::N  N::::N:::::::N       A:::::A     A:::::A          SSS::::::::SS          T:::::T        
        N::::::N   N:::::::::::N      A:::::AAAAAAAAA:::::A            SSSSSS::::S         T:::::T        
        N::::::N    N::::::::::N     A:::::::::::::::::::::A                S:::::S        T:::::T        
        N::::::N     N:::::::::N    A:::::AAAAAAAAAAAAA:::::A               S:::::S        T:::::T        
        N::::::N      N::::::::N   A:::::A             A:::::A  SSSSSSS     S:::::S      TT:::::::TT      
        N::::::N       N:::::::N  A:::::A               A:::::A S::::::SSSSSS:::::S      T:::::::::T      
        N::::::N        N::::::N A:::::A                 A:::::AS:::::::::::::::SS       T:::::::::T      
        NNNNNNNN         NNNNNNNAAAAAAA                   AAAAAAASSSSSSSSSSSSSSS         TTTTTTTTTTT      
    
    New Automated Sanity Test
    
    """)
    global url
    url = input("Please enter the URL that points to the BetterTomorrow Web UI: ")
    global rtsp
    rtsp = input("Please enter the RTSP URL: ")

##########################################

def proceed_to_unsafe_page():
    driver.get(url)
    driver.maximize_window()
    button = driver.find_element_by_id("details-button")
    button.click()
    button = driver.find_element_by_id("proceed-link")
    button.click()

##########################################

def login():
    input_bar = driver.find_element_by_name("username")
    input_bar.send_keys("AnyVisionAdmin")
    input_bar = driver.find_element_by_name("password")
    input_bar.send_keys("AVpa$$word!")
    input_bar.send_keys(Keys.ENTER)

##########################################

def watch_video():
    element = driver.find_element_by_class_name("av-track-layout")
    element.click()
    time.sleep(1)
    element = driver.find_element_by_class_name("menu-icon")
    element.click()    
    time.sleep(1)
    element = driver.find_element_by_xpath("//div[normalize-space()='Watch Video']")
    element.click()
    

##########################################

def add_camera():
    driver.get(url + "/bt/settings/device-settings")
    time.sleep(1)
    element = driver.find_element_by_xpath("//button[normalize-space()='Add Camera']")
    element.click()
    time.sleep(1)
    element = driver.find_element_by_name("title")
    element.send_keys("Test Camera added by NAST")
    time.sleep(2)
    element = driver.find_element_by_name("videoUrl")
    element.send_keys(rtsp)
    time.sleep(1)
    element = driver.find_element_by_xpath("//div[normalize-space()='Please choose an option']")
    element.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('//li[normalize-space()="Default Camera Group"]')
    element.click()
    element = driver.find_element_by_xpath("//button[normalize-space()='Finish']")
    element.click()

##########################################

def main():
    #intro()
    proceed_to_unsafe_page()
    time.sleep(0.5)
    login()
    time.sleep(7)
    watch_video()
    time.sleep(20)
    add_camera()

##########################################

main()


#driver.quit()