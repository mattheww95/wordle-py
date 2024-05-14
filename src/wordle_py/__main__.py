# SPDX-FileCopyrightText: 2024-present Matthew Wells <mattwells9@shaw.ca>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from wordle_py.cli import wordle_py

    sys.exit(wordle_py())
