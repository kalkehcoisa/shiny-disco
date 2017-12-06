# -*- coding: utf-8 -*-


class Vlans:

    def __init__(self, primaries, secondaries):
        self.primary_vlans = primaries
        self.secondary_vlans = secondaries

    def assign(self, *, redundant=False):
        """
        Picks the first free vlan available, removing it from available ones.
        In case of redudancy, secondary vlans are also used.
        """
        primary = self.primary_vlans.pop(0)
        if redundant:
            self.secondary_vlans.pop(0)
        return primary
