# An InstagramBot made by InspectorGadget
# Everyone is free to use and distribute :D

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/']")
        login_button.click()
        time.sleep(2)
        username_element = driver.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        username_element.send_keys(self.username)
        
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if
                                 hashtag in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue
                    
        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                # driver.find_element_by_link_text("Like").click()
                like_button = lambda: driver.find_element_by_xpath('//button[contains(.,"Like")]')
                like_button().click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

username = "USERNAME"
password = "PASSWORD"

InsIG = InstagramBot(username, password)
InsIG.login()

hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
            'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
            'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
            'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
            'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

while True:
    try:
        [InsIG.like_photo(tag) for tag in hashtags]
    except Exception:
        InsIG.closeBrowser()
        time.sleep(60)
        InsIG = InstagramBot(username, password)
        InsIG.login()
