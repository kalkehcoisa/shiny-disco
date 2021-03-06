# -*- coding: utf-8 -*-
from pytest import fixture

from shinydisco.Interface import Interface
from shinydisco.Output import Output


@fixture
def vlan():
    return {'device_id': '0', 'primary_port': '1', 'vlan_id': '0'}


@fixture
def request():
    return {'request_id': 1, 'redundant': '0'}


@fixture
def output(mocker):
    return Output('output_file')


def test_output(output):
    assert output.data == []
    assert isinstance(output.interface, Interface)


def test_output_add(output, vlan, request):
    output.write(vlan, request)
    expected = [
        {'request_id': 1, 'device_id': '0', 'primary_port': '1',
         'vlan_id': '0'}
    ]
    assert output.data == expected


def test_output_add_redundant(output, vlan, request):
    request['redundant'] = '1'
    output.write(vlan, request)
    expected = [
        {'request_id': 1, 'device_id': '0', 'primary_port': '0',
         'vlan_id': '0'},
        {'request_id': 1, 'device_id': '0', 'primary_port': '1',
         'vlan_id': '0'}
    ]
    assert output.data == expected


def test_output_save(mocker, output):
    mocker.patch.object(Interface, 'write')
    output.save()
    headers = ['request_id', 'device_id', 'primary_port', 'vlan_id']
    Interface.write.assert_called_with(headers, output.data)
