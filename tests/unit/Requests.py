# -*- coding: utf-8 -*-
from shinydisco.Interface import Interface
from shinydisco.Requests import Requests


def test_requests_init(mocker):
    mocker.patch.object(Interface, 'read')
    requests = Requests('requests_filepath')
    assert isinstance(requests.interface, Interface)
