# импортируем библиотеку для вызова исключения
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    # предполагаем, что кнопка добавления в корзину есть на странице
    button_is_present = True
    #если кнопка добавления в корзину с указанным селектором найдена - тест пройден,
    try:
        browser.find_element_by_css_selector('button.btn-add-to-basket')
    # если кнопки нет - вызывается исключение, тогда наличие кнопки указываем как False.
    except NoSuchElementException:
        button_is_present = False
    # Через assert записываем информативное сообщение если тест Fail
    assert button_is_present == True, f"Button 'Add to basket' not found"

