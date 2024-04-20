import pytest
from television import Television


def test_tv_initialization():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_tv_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_tv_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = Mute"


def test_tv_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"


def test_tv_channel_down():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_tv_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_tv_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True,Channel = 0, Volume = 0"
