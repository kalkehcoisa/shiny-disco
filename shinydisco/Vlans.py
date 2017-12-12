# -*- coding: utf-8 -*-
from .Interface import Interface


class Vlans:

    def __init__(self, vlans_file, logger):
        self.logger = logger
        self.interface = Interface(vlans_file)
        self.interface.read()

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

        This will also remove orphan secondary ports.
        """
        data = sorted(self.interface.data, key=Vlans._order)
        self.primary_vlans = [i for i in filter(Vlans._filter('1'), data)]
        secondary_vlans = [i for i in filter(Vlans._filter('0'), data)]
        self.secondary_vlans = []
        for item in secondary_vlans:
            vlan = dict(item)
            vlan['primary_port'] = '1'
            if vlan in self.primary_vlans:
                self.secondary_vlans.append(item)

    def book(self, *, redundant=False):
        """
        Books a vlan, removing it from the available ones.
        In case of redudancy, a secondary vlan and the matching primary vlan
        will be removed.
        """
        vlan = None
        if redundant == '1':
            vlan = self.secondary_vlans.pop(0)
            vlan['primary_port'] = '1'
            self.primary_vlans.remove(vlan)

        if vlan is None:
            vlan = self.primary_vlans.pop(0)
        args = [vlan['vlan_id'], vlan['device_id'], redundant]
        self.logger.log('book-vlan', *args)
        return vlan
