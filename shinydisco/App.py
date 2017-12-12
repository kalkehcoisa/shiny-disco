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
    def run(vlans_file='vlans.csv', requests_file='requests.csv',
            output_file='output.csv', verbosity=0):
        logger = Logger(verbosity=verbosity)
        logger.log('run-verbosity', verbosity)
        vlans = Vlans(vlans_file, logger)
        requests = Requests(requests_file)
        output = Output(output_file)

        vlans.prepare()
        for request in requests.get():
            vlan = vlans.book(redundant=request['redundant'])
            output.write(vlan, request)
        output.save()
