# -*- coding: utf-8 -*-
import click

from .App import App


class Cli:
    """
    Manages the command line, taking commands and executing the corresponding
    funcionality.
    """

    @staticmethod
    @click.command()
    @click.argument('vlans', required=False)
    @click.argument('requests', required=False)
    @click.argument('output', required=False)
    @click.option('--verbose', '-v', count=True)
    def main(vlans, requests, output, verbose):
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
        if verbose:
            kwargs['verbosity'] = verbose
        App.run(**kwargs)
