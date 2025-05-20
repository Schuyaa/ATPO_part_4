import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math
from selenium.common.exceptions import NoAlertPresentException

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")

@pytest.fixture
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_argument(f'--lang={language}')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

def solve_quiz_and_get_code(browser):
    """Авто-решение алёрта с промо-квестом."""
    try:
        alert = browser.switch_to.alert
    except NoAlertPresentException:
        return  # алёрта нет — ничего не делаем

    alert_text = alert.text
    # парсим `x` из строки вида "x = 123"
    x_str = alert_text.split("x =")[-1].split()[0]
    answer = str(math.log(abs(12 * math.sin(float(x_str)))))

    alert.send_keys(answer)
    alert.accept()

    # второй алёрт с кодом
    try:
        alert = browser.switch_to.alert
        print(f"Promo code: {alert.text}")
        alert.accept()
    except NoAlertPresentException:
        pass