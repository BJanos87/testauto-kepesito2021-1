# Beimportálom és beállítom a használandó webdriver-t (Google Chrome)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

# A weboldal elérésének letárolása egy változóba
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

# Oldal megnyitása
driver.get(URL)

# A változókba lokátorok segítségével letárolom a használandó web-element-eket
random_color = driver.find_element_by_xpath("html/body/br./span[contains(@style, 'background-color: rgb')]")
test_color = driver.find_element_by_id("testColor")
start_btn = driver.find_element_by_id("start")
stop_btn = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")


# TC01
# Megfelelő megjelenítés ellenőrzése
def test_tc01():
    try:
        assert random_color.is_displayed() is True
        assert test_color.get_attribute("style") == ""
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített elem nem megfelelő", e))


# TC02
# Megfelelő működés ellenőrzése
def test_tc02():
    try:
        start_btn.click()
        time.sleep(3)
        stop_btn.click()
        if random_color.get_attribute("style") == test_color.get_attribute("style"):
            assert result.text == "Correct!"
        else:
            assert result.text == "Incorrect!"
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített üzenet nem megfelelő", e))


# A megnyitott böngésző bezárásra kerül
# driver.close()
