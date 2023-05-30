import time

from selene import have, be
from selene.support.shared import browser

from tests.conftest import LOGIN, PASSWORD, WEB_URL_DEMOSHOP

browser.config.base_url = WEB_URL_DEMOSHOP


def test_login(demoshop_management):
    demoshop_management.open('')

    demoshop_management.element('.account').should(have.text(LOGIN))


def test_customer_info(demoshop_management):
    demoshop_management.open('customer/info')

    demoshop_management.element(f'[value="{LOGIN}"]').should(be.visible)


def test_cart(demoshop_management):
    demoshop_management.open('cart')
    demoshop_management.all('.qty-input').first.set_value('0')
    demoshop_management.all('.qty-input').second.set_value('0')
    demoshop_management.element('[name="updatecart"]').click()

    demoshop_management.open('books')
    demoshop_management.all('[value="Add to cart"]').first.click()
    time.sleep(5)
    demoshop_management.all('[value="Add to cart"]').second.click()
    time.sleep(5)

    demoshop_management.open('cart')
    demoshop_management.all('.product-name').first.should(have.text('Computing and Internet'))
    demoshop_management.all('.product-name').second.should(have.text('Fiction'))
    demoshop_management.all('[value="1"]').first.should(be.visible)
    demoshop_management.all('[value="1"]').second.should(be.visible)


def test_catalog_books(demoshop_management):
    demoshop_management.open('books')

    demoshop_management.element('.page-title').should(have.text('Books'))
