from selenium import webdriver

import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(r"C:\bin/chromedriver.exe")

    def closebrowser(self):
        self.browser.close()

    def loginToInstagram(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")

        # accepting cookies because were forced to accept cookies
        acceptcookies = browser.find_element_by_xpath(r"/html/body/div[2]/div/div/div/div[2]/button[1]")

        acceptcookies.click()

        username_textbox = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")

        password_textbox = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

        username_textbox.send_keys(self.username)
        password_textbox.send_keys(self.password)

        login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")

        login_button.click()
        time.sleep(8)

        notification_pop_up = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notification_pop_up.click()
        time.sleep(2)

    def get_hashtag_photos(self, hashtag):
        browser = self.browser
        browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        listOfPictures = []

        for scroll in range(1, 2):
            try:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.5)

                picture_links = browser.find_elements_by_tag_name("a")

                for picture in picture_links:

                    if '/p/' in picture.get_attribute('href'):
                        if picture not in listOfPictures:
                            listOfPictures.append(picture.get_attribute("href"))


            except Exception:
                continue
        return listOfPictures



    def like_hashtags_photos(self, hashtag):
        browser = self.browser
        photolinks = self.get_hashtag_photos(hashtag=hashtag)

        for photo in photolinks:
            browser.get(photo)
            time.sleep(1)
            like_button = browser.find_element_by_class_name("fr66n")
            like_button.click()


if __name__ == "__main__":

    username = "username"
    password = "password"
    hashtag = "Cars"

    Bot = InstagramBot(username=username, password=password)

    Bot.loginToInstagram()
    Bot.like_hashtags_photos(hashtag=hashtag)





