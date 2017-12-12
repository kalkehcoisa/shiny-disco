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
    runner.invoke(Cli.main, [])
    App.run.assert_called_with()


def test_cli_run_optionals(runner):
    runner.invoke(Cli.main, ['vlans.csv', 'requests.csv', 'output.csv'])
    kwargs = {
        'vlans_file': 'vlans.csv',
        'requests_file': 'requests.csv',
        'output_file': 'output.csv'
    }
    App.run.assert_called_with(**kwargs)
