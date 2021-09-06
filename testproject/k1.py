# Beimportálom és beállítom a használandó webdriver-t (Google Chrome)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

# A weboldal elérésének letárolása egy változóba
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

# Oldal megnyitása
driver.get(URL)

# A változókba lokátorok segítségével letárolom a használandó web-element-eket
input_a = driver.find_element_by_id("a")
input_b = driver.find_element_by_id("b")
submit_btn = driver.find_element_by_id("submit")
results = driver.find_element_by_id("results")
result = driver.find_element_by_id("result")


# Beviteli mezők törléséhez használt függvény
def clear_inputs():
    input_a.clear()
    input_b.clear()


# TC01
# Megfelelő megjelenítés ellenőrzése
def test_tc01():
    try:
        assert input_a.get_attribute("value") == ""
        assert input_b.get_attribute("value") == ""
        assert results.get_attribute("style") == "display: none;"
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített mezők nem megfelelőek", e))


# TC02
# Megfelelő működés ellenőrzése
def test_tc02():
    try:
        input_a.send_keys(2)
        input_b.send_keys(3)
        submit_btn.click()
        time.sleep(0.5)
        assert result.text == "10"
        clear_inputs()
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített eredmény nem megfelelő", e))


# TC03
# Megfelelő működés ellenőrzése
def test_tc03():
    try:
        submit_btn.click()
        time.sleep(0.5)
        assert result.text == "NaN"
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített eredmény nem megfelelő", e))


# A megnyitott böngésző bezárásra kerül
# driver.close()
