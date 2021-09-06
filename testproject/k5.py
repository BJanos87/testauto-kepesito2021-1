# Beimportálom és beállítom a használandó webdriver-t (Google Chrome)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

# A weboldal elérésének letárolása egy változóba
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

# Oldal megnyitása
driver.get(URL)

# A változókba lokátorok segítségével letárolom a használandó web-element-eket
cells = driver.find_elements_by_xpath("html/body/div/div/div/table/tbody[@id='bingo-body']/tr/td")
number_list = driver.find_elements_by_xpath("html/body/div/div/div[3]/ol/li")
bingo_text = driver.find_element_by_id("messages")
spin_btn = driver.find_element_by_id("spin")


# TC01
# Applikáció helyes megjelenésének ellenőrzése
def test_tc01():
    try:
        assert len(cells) == 25
        assert len(number_list) == 75
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített karakter nem megfelelő", e))


# TC02
# Applikáció helyes működésének ellenőrzése
def test_tc02():
    try:
        while bingo_text.is_displayed() is False:
            spin_btn.click()
            if bingo_text.is_displayed() is True:
                break
        assert bingo_text.text == "BINGO"
    except AssertionError as e:
        pytest.fail(print("Az oldalon megjelenített karakter nem megfelelő", e))

# A megnyitott böngésző bezárásra kerül
# driver.close()
