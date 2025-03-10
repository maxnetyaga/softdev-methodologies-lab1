#!/usr/bin/env python3
from typing import Type, TypeVar
import readline
from math import sqrt
from pathlib import Path

import click


class InputFileFormatException(Exception):
    pass


@click.command()
@click.argument("input", type=Path, required=False)
def equation_solver(input: Path | None):
    """Quadratic Equation Solver

    INPUT is path to file with equation parameters.

    if INPUT isn`t present, program run in interactive mode.
    """

    if not input:
        params = read_params_stdin(param_type=float)
        click.echo()
    else:
        try:
            params = read_params_file(input, params_count=3, param_type=float)
        except InputFileFormatException as err:
            click.echo(err)
            return

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


T = TypeVar("T")


def read_params_stdin(param_type: Type[T]) -> tuple[T, T, T]:
    a = read_param_stdin("a", param_type)
    b = read_param_stdin("b", param_type)
    c = read_param_stdin("c", param_type)
    return (a, b, c)


def read_param_stdin(name, param_type):
    while True:
        try:
            param = param_type(input(f"{name} = "))
            return param
        except ValueError:
            click.echo("Value is invalid! Try again")


def read_params_file(
        path: Path, params_count, param_type: Type
) -> list:
    with path.open() as file:
        params = file.readline().split()

    if len(params) != params_count:
        raise InputFileFormatException(
            "Provided unexpected number of parameters")
    
    for i in range(len(params)):
        try:
            params[i] = param_type(params[i])
        except ValueError:
            raise InputFileFormatException(f"Parameter #{i+1} has wrong format")

    return params

if __name__ == '__main__':
    equation_solver()
