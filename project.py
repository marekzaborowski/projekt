from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time


class Facebook:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close(self):

        self.driver.close()

    def login(self):
        try:
            driver = self.driver

            #odpalenie strony startowej
            driver.get("https://www.facebook.com/")
            assert 'Facebook' in driver.title
            time.sleep(1)

            #pole z loginem i hasłem
            input_email = driver.find_element_by_xpath('//*[@id="email"]')
            input_password = driver.find_element_by_xpath('//*[@id="pass"]')

            time.sleep(1)

            #wprowadzenie emaila
            input_email.clear()
            input_email.send_keys(self.username)

            #wprowadzenie hasła
            input_password.clear()
            input_password.send_keys(self.password)
            input_password.send_keys(Keys.RETURN)

            #logowanie
            button_sing_up = driver.find_element_by_xpath('//*[@id="u_0_d"]')
            button_sing_up.click()

            time.sleep(25)

        except NoSuchElementException as e:
            print(e)
        except Exception as e:
            print(e)

    def add_post(self, message):
        try:
            driver = self.driver

            #wejście w pole tekstowe
            go_to_main_page = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/a')
            go_to_main_page.click()

            time.sleep(7)

            #wstawienie wiadomości
            add_post = driver.find_element_by_tag_name('textarea')
            add_post.send_keys(message)

            time.sleep(8)

            #dodanie wiadomości
            send_post = driver.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
            send_post.click()

            time.sleep(10)

        except NoSuchElementException as e:
            print(e)
        except Exception as e:
            print(e)

    def search_new_friend(self, name):
        try:
            driver = self.driver

            #znajduje wyniki pod daną nazwą
            driver.get('https://www.facebook.com/search/top/?q=' + name + '&epa=SEARCH_BOX')
            time.sleep(2)

            #zapis wyniku dla wglądu
            driver.save_screenshot(name + '.png')

        except NoSuchElementException as e:
            print(e)
        except Exception as e:
            print(e)

    def send_message(self, person, message):
        try:
            driver = self.driver

            #przejście do widoku wiadomości
            driver.get('https://www.facebook.com/messages/t/')

            #wyszukanie danej osoby
            look = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input')
            look.send_keys(person)

            time.sleep(10)

            #wejście w czat z daną osobą
            choose = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div/div')
            choose.click()

            time.sleep(5)

            #wpisanie wiadomości
            message_area = driver.find_element_by_css_selector('.notranslate')
            message_area.send_keys(message)
            time.sleep(5)

            #wysłanie wiadomości
            send_message = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div/a')
            send_message.click()

            time.sleep(2)

        except NoSuchElementException as e:
            print(e)
        except Exception as e:
            print(e)

if __name__ == '__main__':


    user = 'marek.zawadzki123@wp.pl'
    passw = 'Lenovo'
    konto = Facebook(username=user, password=passw)
    konto.login()
    konto.add_post('To jest 1 dzień wakacji!')

    konto.search_new_friend('Marek Zaborowski')
    konto.send_message('Mama', "Hej, pierwszy dzień za mną, mam się dobrze. Pozdrówki, całuje")
    konto.close()