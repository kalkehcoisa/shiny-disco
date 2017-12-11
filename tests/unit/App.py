# -*- coding: utf-8 -*-
from shinydisco.App import App
from shinydisco.Interface import Interface
from shinydisco.Output import Output
from shinydisco.Requests import Requests
from shinydisco.Vlans import Vlans


def test_app_run(mocker):
    mocker.patch.object(Interface, 'read')
    mocker.patch.object(Output, 'write')
    mocker.patch.object(Output, 'save')
    mocker.patch.object(Requests, 'get', return_value=[{'redundant': '0'}])
    mocker.patch.object(Vlans, 'book')
    App.run('vlans.csv', 'requests.csv', 'output.csv')
    Vlans.book.assert_called_with(redundant='0')
    Output.write.assert_called_with(Vlans.book(), {'redundant': '0'})
    assert Requests.get.call_count == 1
    assert Output.save.call_count == 1
