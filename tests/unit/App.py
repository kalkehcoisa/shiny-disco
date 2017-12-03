# -*- coding: utf-8 -*-
from shinydisco.App import App


def test_app_run():
    assert App.run('requests.csv', 'vlans.csv') is None
