from stock_prices_and_news import *
# import pytest


def test_fetch_prices():
    # current price
    assert isinstance(fetch_prices("NVDA")["current_price"], float) == True
    assert isinstance(fetch_prices("AMD")["current_price"], float) == True
    assert isinstance(fetch_prices("MSFT")["current_price"], float) == True
    assert isinstance(fetch_prices("DSADASFDASFSDFA")["current_price"], float) == False
    # price change
    assert isinstance(fetch_prices("NVDA")["price_change"], float) == True
    assert isinstance(fetch_prices("NdasVDAaadasdasdad")["price_change"], float) == False
    # percent change
    assert isinstance(fetch_prices("NVDA")["percent_change"], float) == True
    assert isinstance(fetch_prices("NdasVDAaadasdasdad")["percent_change"], float) == False


def test_get_market_status():
    assert get_market_status()["is_open"] in (True, False)
    if get_market_status()["is_open"]:
        assert get_market_status()["status"] in ("pre-market", "regular", "post-market")
    elif not get_market_status()["is_open"]:
        assert get_market_status()["status"] == "Closed"


def test_get_full_name():
    assert get_full_name("NVDA") == "NVIDIA Corp"


def test_get_image():
    assert get_image("this is not a valid url...", width=100, height=100) is None

