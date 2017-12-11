# -*- coding: utf-8 -*-
class Output:

    def __init__(self, output_file):
        self.output_file = output_file
        self.data = []

    def write(self, vlan, request):
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
