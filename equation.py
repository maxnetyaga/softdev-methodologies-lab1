#!/usr/bin/env python3
from dataclasses import dataclass
from math import sqrt
from pathlib import Path

import click


@click.command()
@click.argument("input", type=Path, required=False)
def equation_solver(input: Path | None):
    """Quadratic Equation Solver

    INPUT is path to file with equation parameters.

    if INPUT isn`t present, program run in interactive mode.
    """
    params = (2, 4, 2)
    click.echo(f"Equation is: {str_equation(*params)}")

    roots = solve_equation(*params)
    click.echo(f"There are {len(roots)} roots")
    for (i, root) in enumerate(roots):
        click.echo(f"x{i+1} = {root:.1f}")




def str_equation(a: float, b: float, c: float):
    return f"({a:.1f}) x^2 + ({b:.1f}) x + ({c:.1f}) = 0"


def solve_equation(
    a: float, b: float, c: float
) -> list[float]:
    roots = []
    d = b**2 - 4*a*c

    if d == 0:
        x = (-b + sqrt(d)) / (2*a)
        roots.append(x)
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        roots.extend((x1, x2))
    
    return roots



if __name__ == '__main__':
    equation_solver()
