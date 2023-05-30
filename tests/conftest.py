import os
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from utils.base_session import BaseSession

load_dotenv()
API_URL_REQRES = os.getenv('API_URL_REQRES')
API_URL_DEMOSHOP = os.getenv('API_URL_DEMOSHOP')
WEB_URL_DEMOSHOP = os.getenv('WEB_URL_DEMOSHOP')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope='session')
def reqres():
    return BaseSession(API_URL_REQRES)


@pytest.fixture(scope='session')
def demosh():
    demoshop = BaseSession(API_URL_DEMOSHOP)
    demoshop.post('login', json={'Email': LOGIN, 'Password': PASSWORD}, allow_redirects=False)
    authorization_cookie = demoshop.cookies.get('NOPCOMMERCE.AUTH')
    return authorization_cookie


@pytest.fixture(scope='function')
def demoshop_management(demosh):
    browser.config.base_url = WEB_URL_DEMOSHOP
    browser.open('Themes/DefaultClean/Content/images/logo.png')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': demosh})

    yield browser

    browser.quit()
