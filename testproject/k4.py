# Beimportálom és beállítom a használandó webdriver-t (Google Chrome)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

# A weboldal elérésének letárolása egy változóba
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

# Oldal megnyitása
driver.get(URL)

# A változókba lokátorok segítségével letárolom a használandó web-element-eket
op_table = driver.find_element_by_xpath("html/body/div/div/p[3]")
char = driver.find_element_by_id("chr")
operator = driver.find_element_by_id("op")
number = driver.find_element_by_id("num")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")

# Használandó teszt adatok
test_data = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


# TC01
# Műveleti tábla ellenőrzés
def test_tc01():
    try:
        assert op_table.text == test_data
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített karakter nem megfelelő", e))


# TC02
# Megjelenített adatok ellenőrzése
def test_tc02():
    try:
        assert char.text in test_data
        assert operator.text == "+" or "-"
        assert number.text.isdigit() is True
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített adatok nem megfelelőek", e))


# TC03
# Megfelelő működés ellenőrzése
def test_tc03():
    try:
        submit_btn.click()
        time.sleep(0.5)
        if operator.text == "+":
            char_numb = test_data.find(char.text) + int(number.text)
            assert (test_data[char_numb]) == result.text
        else:
            char_numb = test_data.find(char.text) - int(number.text)
            assert (test_data[char_numb]) == result.text
    except AssertionError as e:
        pytest.fail(print("Az oldal működése nem megfelelő", e))

# A megnyitott böngésző bezárásra kerül
# driver.close()
