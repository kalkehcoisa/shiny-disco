# -*- coding: utf-8 -*-
from click.testing import CliRunner

from pytest import fixture

from shinydisco.App import App
from shinydisco.Cli import Cli


@fixture
def app(mocker):
    mocker.patch.object(App, 'run')


@fixture
def runner(app):
    return CliRunner()


def test_cli_run(runner):
    runner.invoke(Cli.run, ['vlans.csv', 'requests.csv', 'output.csv'])
    App.run.assert_called_with('vlans.csv', 'requests.csv', 'output.csv')
