from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import IndexPageLocators, SpeedPageLocators, CarsPageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def fill_contact_form(self, name, email, message):
        self.do_clear(IndexPageLocators.NAME_FIELD)
        self.do_clear(IndexPageLocators.EMAIL_FIELD)
        self.do_clear(IndexPageLocators.MESSAGE_FIELD)
        self.do_send_keys(IndexPageLocators.NAME_FIELD, name)
        self.do_send_keys(IndexPageLocators.EMAIL_FIELD, email)
        self.do_send_keys(IndexPageLocators.MESSAGE_FIELD, message)
        self.do_submit(IndexPageLocators.MESSAGE_FIELD)

    


class IndexPage(BasePage):

    def is_title_matches(self):
        return 'Rides Shop | Home' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'WELCOME TO RIDES SHOP'
        return text in index_heading

    def is_about_link_works(self):
        self.do_click(IndexPageLocators.ABOUT_LINK)
        return 'Rides Shop | About' in self.driver.title

    def is_index_link_works(self):
        self.do_click(IndexPageLocators.INDEX_LINK)
        return 'Rides Shop | Home' in self.driver.title

    def is_contact_form_works(self):
        self.fill_contact_form('maciej', 'mj@gmail.com', 'new message')
        msg_text = self.get_element_text(IndexPageLocators.MSG_TEXT)
        return 'Thank you maciej for your message. We will reply to you as soon as possible at mj@gmail.com.' in msg_text

    def is_speed_link_works(self):
        self.do_click(IndexPageLocators.SPEED_LINK)
        return 'Rides Shop | Speed' in self.driver.title


class SpeedPage(BasePage):

    def is_title_matches(self):
        return 'Rides Shop | Speed' in self.driver.title

    def is_offers_link_works(self):
        self.do_click(SpeedPageLocators.OFFERS_LINK)
        return 'Rides Shop | Category' in self.driver.title 

    def is_car_producer_displayed_coorectly(self):
        car_producer_text = self.get_element_text(SpeedPageLocators.CAR_PRODUCER)
        return 'FERRARI' in car_producer_text

class CarsPage(BasePage):

    def is_title_matches(self):
        return 'Rides Shop | Cars' in self.driver.title

    def is_cars_heading_displayed_correctly(self):
        cars_heading = self.get_element_text(CarsPageLocators.CARS_HEADING)
        text = 'OUR LATEST OFFERS'
        return text in cars_heading

    def is_filter_form_works(self):
        self.do_clear(CarsPageLocators.PRODUCER_FIELD)
        self.do_send_keys(CarsPageLocators.PRODUCER_FIELD, 'ferrari')
        self.do_submit(CarsPageLocators.PRODUCER_FIELD)
        car_producer = self.get_element_text(CarsPageLocators.CAR_PRODUCER)
        return 'FERRARI' in car_producer

    def is_detail_link_works(self):
        self.do_click(CarsPageLocators.DETAILS_LINK)
        return 'Rides Shop | Car Detail' in self.driver.title

    def is_menu_button_works(self):
        self.do_click(CarsPageLocators.MENU_BUTTON)
        home_link_text = self.get_element_text(CarsPageLocators.HOME_LINK)
        return 'HOME' in home_link_text

    def is_home_link_works(self):
        self.do_click(CarsPageLocators.HOME_LINK)
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'WELCOME TO RIDES SHOP'
        return text in index_heading

    def is_category_link_works(self):
        self.do_click(CarsPageLocators.MENU_BUTTON)
        self.do_click(CarsPageLocators.CATEGORY_LINK)
        cat_heading = self.get_element_text(CarsPageLocators.CATEGORY_HEADING)
        return 'OUR LATEST OFFERS' in cat_heading











