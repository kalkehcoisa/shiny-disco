# -*- coding: utf-8 -*-
import os
from unittest.mock import MagicMock


from pytest import fixture


@fixture
def csv_teardown(request):
    def teardown():
        os.remove('testcsv.csv')
    request.addfinalizer(teardown)


@fixture
def logger():
    """
    Mock the logger
    """
    return MagicMock()
