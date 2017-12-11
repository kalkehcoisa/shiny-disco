# -*- coding: utf-8 -*-
import click

from .App import App


class Cli:

    @staticmethod
    @click.command()
    @click.argument('vlans')
    @click.argument('requests')
    @click.argument('output')
    def run(vlans, requests, output):
        """
        Runs the app, passing vlans and requests filenames from the cli.
        """
        App.run(vlans, requests, output)
