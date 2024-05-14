# SPDX-FileCopyrightText: 2024-present Matthew Wells <mattwells9@shaw.ca>
#
# SPDX-License-Identifier: MIT
import click

from wordle_py.__about__ import __version__
from wordle_py.words import render, words


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="wordle-py")
def wordle_py():
    selection = words.Words()
    game = render.Renderer(selection)
    game.game_loop()
