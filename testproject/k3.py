# Beimportálom és beállítom a használandó webdriver-t (Google Chrome)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

# A weboldal elérésének letárolása egy változóba
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

# Oldal megnyitása
driver.get(URL)

# A változókba lokátorok segítségével letárolom a használandó web-element-eket
input_field = driver.find_element_by_id("title")
error_msg = driver.find_element_by_xpath("html/body/form/span")

# Használandó teszt adatok
test_data = ["abcd1234", "teszt233@", "abcd"]
error_msg_text = {"msg_1": "Only a-z and 0-9 characters allewed.",
                  "msg_2": "Title should be at least 8 characters; you entered 4."
                  }


# TC01
# Input mező kitöltése valid adattal
def test_tc01():
    try:
        input_field.send_keys(test_data[0])
        time.sleep(0.5)
        assert error_msg.text == ""
        input_field.clear()
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített üzenet nem megfelelő", e))


# TC02
# Input mező kitöltése invalid adattal
def test_tc02():
    try:
        input_field.send_keys(test_data[1])
        time.sleep(0.5)
        assert error_msg.text == error_msg_text["msg_1"]
        input_field.clear()
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített üzenet nem megfelelő", e))


# TC03
# Input mező kitöltése invalid adattal
def test_tc03():
    try:
        input_field.send_keys(test_data[2])
        time.sleep(0.5)
        assert error_msg.text == error_msg_text["msg_2"]
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített üzenet nem megfelelő", e))


# A megnyitott böngésző bezárásra kerül
# driver.close()
