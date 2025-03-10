#!/usr/bin/env python3
from pathlib import Path

import click


@click.command()
@click.argument("input", type=Path, required=False)
def equation_solver(input: Path | None):
    """Quadratic Equation Solver

    INPUT is path to file with equation parameters.

    if INPUT isn`t present, program run in interactive mode.
    """
    pass

if __name__ == '__main__':
    equation_solver()