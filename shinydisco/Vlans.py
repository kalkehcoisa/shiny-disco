# -*- coding: utf-8 -*-
from .Interface import Interface


class Vlans:

    def __init__(self, vlans_file):
        self.interface = Interface(vlans_file)

    @staticmethod
    def _order(vlan):
        return (int(vlan['vlan_id']), int(vlan['device_id']))

    @staticmethod
    def _filter(port):
        return lambda vlan: vlan['primary_port'] == port

    def prepare(self):
        """
        Prepares vlans, so that they are arranged by booking order. This means
        they will be ordered by vlan and device id, with primary ports
        separated from secondary ones.
        """
        data = sorted(self.interface.data, key=Vlans._order)
        self.primary_vlans = [i for i in filter(Vlans._filter('1'), data)]
        self.secondary_vlans = [i for i in filter(Vlans._filter('0'), data)]

    def book(self, *, redundant=False):
        """
        Books a vlan, removing it from the available ones.
        In case of redudancy, a secondary vlan and the matching primary vlan
        will be removed.
        """
        if redundant:
            secondary = self.secondary_vlans.pop(0)
            secondary['primary_port'] = '1'
            self.primary_vlans.remove(secondary)
            return secondary
        return self.primary_vlans.pop(0)
