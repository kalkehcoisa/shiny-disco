# -*- coding: utf-8 -*-
import click

from .App import App


class Cli:

    @staticmethod
    @click.command()
    @click.argument('vlans', required=False)
    @click.argument('requests', required=False)
    @click.argument('output', required=False)
    def main(vlans, requests, output):
        """
        Runs the app, passing vlans and requests filenames from the cli.
        """
        kwargs = {}
        if vlans:
            kwargs['vlans_file'] = vlans
        if requests:
            kwargs['requests_file'] = requests
        if output:
            kwargs['output_file'] = output
        App.run(**kwargs)
