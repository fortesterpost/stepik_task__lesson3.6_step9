import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # прописываем параметр для браузеров, по умолчанию Chromе, если параметр не будет задан
    parser.addoption('--browser_name', action='store', default= 'chrome',
                     help="Choose browser: chrome or firefox")
    # прописываем параметр для языков
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, pl,...")

# фиктура для открытия и закрытия браузера
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # открываем браузер Chrome на языке, переданным в параметре
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # открываем браузер Firefox на языке, переданным в параметре
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
