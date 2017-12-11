# -*- coding: utf-8 -*-
from .Interface import Interface


class Output:
    """
    Outputs processed requests to a csv file, using Interface.
    """

    def __init__(self, output_file):
        self.interface = Interface(output_file)
        self.data = []

    def write(self, vlan, request):
        """
        Logs processed requests. If the request is redundant, two items
        will be logged.
        """
        item = {
            'request_id': request['request_id'],
            'device_id': vlan['device_id'],
            'primary_port': '1',
            'vlan_id': vlan['vlan_id']
        }
        if request['redundant'] == '1':
            self.data.append(dict(item))
            self.data[-1]['primary_port'] = '0'
        self.data.append(item)

    def save(self):
        """
        Saves the output, performing the actual write.
        """
        self.interface.write(self.data)
