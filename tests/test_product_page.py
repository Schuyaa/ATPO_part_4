import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

# Параметризованный список ссылок: одна из них с багом
promo_links = [
    f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" 
    if n != 7 else 
    pytest.param(
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}",
        marks=pytest.mark.xfail(reason="Known bug on promo offer7")
    )
    for n in range(10)
]

@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_correct_product_name_in_message(product_name)
    page.should_be_correct_product_price_in_message(product_price)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):#открытие корзины
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text()