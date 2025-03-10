#!/usr/bin/env python3
from typing import Type, TypeVar
import readline
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

    if not input:
        params = read_params_stdin()

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


def read_params_stdin() -> tuple[float, float, float]:
    a = read_param_stdin("a", float)
    b = read_param_stdin("b", float)
    c = read_param_stdin("c", float)
    return (a, b, c)


T = TypeVar("T")


def read_param_stdin(name, param_type: Type[T]) -> T:
    while True:
        try:
            param = param_type(input(f"{name} = "))
            return param
        except ValueError:
            click.echo("Value is invalid! Try again")


if __name__ == '__main__':
    equation_solver()
