# -*- coding: utf-8 -*-
from .Logger import Logger
from .Output import Output
from .Requests import Requests
from .Vlans import Vlans


class App:
    """
    Pulls components together and provides external access to operations
    """

    @staticmethod
    def run(vlans_file, requests_file, output_file):
        logger = Logger(verbosity=0)
        logger.log('run-verbosity', 0)
        vlans = Vlans(vlans_file, logger)
        requests = Requests(requests_file)
        output = Output(output_file)

        vlans.prepare()
        for request in requests.get():
            vlan = vlans.book(redundant=request['redundant'])
            output.write(vlan, request)
        output.save()
