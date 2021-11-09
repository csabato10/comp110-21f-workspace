"""Utility functions."""

from csv import DictReader

__author__ = "730466575"

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Returns each row of a file."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()
    return result


def column_values(filename: list[dict[str, str]], column: str) -> list[str]:
    """Returns values of a single column."""
    result: list[str] = []
    for row in filename:
        value: str = row[column]
        result.append(value)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Returns table in column format."""
    result: dict[str, list[str]] = {}
    column_names: dict[str, str] = table[0]
    for column in column_names:
        result[column] = column_values(table, column)
    return result


def head(table_values: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Table of only ceratin rows."""
    result: dict[str, list[str]] = {}
    if rows >= len(table_values):
        result = table_values
    else:
        for value in table_values:
            i: int = 0
            old_list: list[str] = table_values[value]
            new_list: list[str] = []
            while i < rows:
                new_list.append(old_list[i])
                i += 1
            result[value] = new_list
    return result


def select(table_values: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Table of only certain columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table_values[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables."""
    result: dict[str, list[str]] = {}
    for value in table_one:
        result[value] = table_one[value]
    for value in table_two:
        if value in result:
            result[value] = table_one[value] + table_two[value]
        else:
            result[value] = table_two[value]
    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Count values in a list and display in a dictionary."""
    result: dict[str, int] = {}
    for value in given_list:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result