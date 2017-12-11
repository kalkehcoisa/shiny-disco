# -*- coding: utf-8 -*-
import os

from pytest import fixture


@fixture
def csv_teardown(request):
    def teardown():
        os.remove('testcsv.csv')
    request.addfinalizer(teardown)
