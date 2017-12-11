# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

from pytest import fixture

from shinydisco.Interface import Interface
from shinydisco.Requests import Requests


@fixture
def requests(mocker):
    mocker.patch.object(Interface, 'read')
    return Requests('requests_filepath')


def test_requests_init(requests):
    assert Interface.read.call_count == 1
    assert isinstance(requests.interface, Interface)


def test_requests_get(requests):
    requests.interface = MagicMock()
    assert requests.get() == requests.interface.data
