# -*- coding: utf-8 -*-


class Vlans:

    def __init__(self, primaries, secondaries):
        self.primary_vlans = primaries
        self.secondary_vlans = secondaries

    def book(self, *, redundant=False):
        """
        Books a vlan, removing it from the available ones.
        In case of redudancy, a secondary vlan and the matching primary vlan
        will be removed.
        """
        if redundant:
            secondary = self.secondary_vlans.pop(0)
            self.primary_vlans.remove(secondary)
            return secondary
        return self.primary_vlans.pop(0)
