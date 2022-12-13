from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.keys import Keys
import pickle
import os
import time
import random
from config import vk_phone, vk_password




class TikTokBot:
    def __init__(self, vk_phone, vk_password):
        self.vk_phone = vk_phone
        self.vk_password = vk_password
        options = webdriver.ChromeOptions()
        options.set_preference(
            'general.useragent.override',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition Yx 03)'
        )
        options.set_preference('dom.webdriver.enabled', False)
        self.driver = webdriver.Chrome(
            executable_path='\Bot Tik Tok\chromedriver.exe',
            options=options
        )

    def xpath_exists(self, xpath):
        '''Check xpath'''
        try:
            self.driver.find_element(By.XPATH, xpath)
            exist = True
        except NoSuchElementExeption:
            exist = False
        return exist

    def class_exists(self, class_name):
        '''Check class'''
        try:
            self.driver.find_element(By.CLASS_NAME, class_name)
            exist = True
        except NoSuchElementExeption:
            exist = False
        return exist

    def close_driver(self):
        '''Close driver'''
        driver.close()
        driver.quit()

    def get_cookies(self):
        '''Get cookies'''
        if os.path.exists(f'\Bot Tik Tok\cookies\{vk_phone}_cookies'):
            print('Cookies exist.')
            self.close_driver()
        else:
            print('No cookies')
            self.driver.get('https://www.tiktok.com/')
            time.sleep(5)

            if self.class_exists('login-button'):
                try:
                    self.driver.find_element(By.CLASS, 'login-button').click()
                    time.sleep(5)

                    # switch to iframe
                    iframe = self.driver.find_element(By.XPATH, '//iframe[@class="jsx-2873455137"]')
                    self.driver.switch_to.frame(iframe)
                    time.sleep(5)

                    if self.xpath_exists('//div[contains(text(), "VK"]'):
                        self.driver.find_element(By.XPATH, '//div[contains(text(), "VK"]').click()
                        time.sleep(5)
                    elif self.xpath_exists('//div[contains(text(), "Log in with VK"]'):
                        self.driver.find_element(By.XPATH, '//div[contains(text(), "Log in with VK"]').click()
                        time.sleep(5)

                    self.driver.switch_to.window(self.driver.window_handles[1])
                    time.sleep(3)

                    email_input = self.driver.find_element(By.NAME, 'email')
                    email_input.clear()
                    email_input.send_keys(vk_phone)
                    time.sleep(4)

                    password_input = self.driver.find_element(By.NAME, 'pass')
                    password_input.clear()
                    password_input.send_keys(vk_password, Keys.ENTER)
                    time.sleep(15)

                    self.driver.switch_to.window(self.driver.window_handles[0])

                    # cookies
                    pickle.dump(
                        self.driver.get_cookies(),
                        open(f'\Bot Tik Tok\cookies\{vk_phone}_cookies', 'wb')
                    )
                    print("You're in. Good job. Cookies saved.")
                    self.close_driver()
                except Exception as ex:
                    print(ex)
                    self.closes_driver()
            else:
                print('Something was wrong...')
                self.closes_driver()

    def set_like(self, post_url):
        '''Like on a post'''
        try:
            self.driver.get('https://www.tiktok.com/')
            time.sleep(4)
            for cookie in pickle.load(
                open('\Bot Tik Tok\cookies\{vk_phone}_cookies', 'rb')
            ):
                self.driver.add_cookie(cookie)
            time.sleep(3)
            self.driver.refresh()
            time.sleep(4)

            if not self.class_exists('login-button'):
                print('Log in successfully')
                self.driver.get(url=post_url)
                time.sleep(random.randrange(3, 7))
                item_video = self.driver.find_element(By.CLASS_NAME, 'item-video-container').click()
                time.sleep(random.randrange(3, 7))

                like_span = self.driver.find_element(By.CLASS_NAME, 'action-wrapper-v2').find_element(
                    By.CLASS_NAME, 'icons')
                if 'liked' in like_span.get_attribute('class').split():
                    print('You already liked this post')
                else:
                    like_button = self.driver.find_element(By.CLASS_NAME, 'like').click()
                    time.sleep(random.randrange(3, 7))
                    close_button = self.driver.find_element(By.CLASS_NAME, 'close').click()
                    time.sleep(random.randrange(3, 7))
                    print('You liked the post')

                self.close_driver()
            else:
                print('Bad log in')
                self.close_driver()
        except Exception as ex:
            print(ex)
            print('Check the URL')
            self.close_driver()




def main():
    tiktok_bot = TikTokBot(vk_phone=vk_phone, vk_password=vk_password)
    tiktok_bot.set_like(post_url='random url post')

    # tiktok_bot.get_cookies()

    # tiktok_auth('https://www.tiktok.com/')
    # tiktok_auth('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

if __name__ =='__main__':
    main()