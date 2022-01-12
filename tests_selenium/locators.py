from selenium.webdriver.common.by import By

class IndexPageLocators(object):
    
    INDEX_HEADING = (By.CLASS_NAME, 'index-heading')
    ABOUT_LINK = (By.ID, 'about-link')
    INDEX_LINK = (By.CLASS_NAME, 'index-link')
    NAME_FIELD = (By.NAME, 'name')
    EMAIL_FIELD = (By.NAME, 'email')
    MESSAGE_FIELD = (By.NAME, 'message')
    MSG_TEXT = (By.CLASS_NAME, 'msg-text')
    SPEED_LINK = (By.ID, 'speed-link')

class SpeedPageLocators(object):

    OFFERS_LINK = (By.ID, 'offers-link')
    CAR_PRODUCER = (By.ID, 'car-producer')

class CarsPageLocators(object):

    CARS_HEADING = (By.CLASS_NAME, 'cars-heading')
    PRODUCER_FIELD = (By.NAME, 'producer')
    CAR_PRODUCER = (By.ID, 'car-producer')
    DETAILS_LINK = (By.ID, 'details-link')
    MENU_BUTTON = (By.LINK_TEXT, 'MENU')
    HOME_LINK = (By.LINK_TEXT, 'HOME')
    CATEGORY_LINK = (By.LINK_TEXT, 'SPEED')
    CATEGORY_HEADING = (By.CLASS_NAME, 'category-heading')



