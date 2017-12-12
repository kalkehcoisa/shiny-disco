# -*- coding: utf-8 -*-
from pytest import fixture

from shinydisco.App import App
from shinydisco.Interface import Interface
from shinydisco.Logger import Logger
from shinydisco.Output import Output
from shinydisco.Requests import Requests
from shinydisco.Vlans import Vlans


@fixture
def app(mocker):
    mocker.patch.object(Interface, 'read')
    mocker.patch.object(Output, 'write')
    mocker.patch.object(Output, 'save')
    mocker.patch.object(Requests, 'get', return_value=[{'redundant': '0'}])
    mocker.patch.object(Vlans, 'book')
    mocker.patch.object(Vlans, 'prepare')
    return App


def test_app_run(app):
    app.run()
    Vlans.book.assert_called_with(redundant='0')
    Output.write.assert_called_with(Vlans.book(), {'redundant': '0'})
    assert Vlans.prepare.call_count == 1
    assert Requests.get.call_count == 1
    assert Output.save.call_count == 1


def test_app_run_optionals(app):
    app.run(vlans_file='vlans', requests_file='requests', output_file='output')


def test_app_run_log(mocker, app):
    mocker.patch.object(Logger, 'log')
    app.run()
    Logger.log.assert_called_with('run-verbosity', 0)
