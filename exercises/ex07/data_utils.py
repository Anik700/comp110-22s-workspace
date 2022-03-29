"""Dictionary related utility functions."""

__author__ = "730243145"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding='utf8')

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Creating a list from column values."""
    result: list[str] = []

    # Read each row of the first parameter 'table'
    for row in table:
        value = str(row.get(key))
        result.append(value)
    
    return result


def columnar(input: list[dict[str, str]]) -> dict[str, list[str]]:
    """Creating a dictionary from list input."""
    results: dict[str, list[str]] = {}
    keys = input[0].keys()
    for key in keys:
        results[key] = column_values(input, key)
    return results


def head(column: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """Creating a dictionary from column data."""
    results: dict[str, list[str]] = {}
    for key in column:
        first_values: list[str] = []
        i = 0
        if row < len(column[key]):
            while i < row:
                first_values.append(column[key][i])
                i += 1
            results[key] = first_values
        else: 
            return column
    return results

# New_Table: dict[str, list[str]] = {'breed': ['pug', 'corgi', 'beagle'],
#    'color': ['brown', 'blue', 'pink'],
#    'name': ['Kris', 'Kaki', 'Marc']}
# print(head(New_Table, 5))


def select(table: dict[str, list[str]], new_list: list[str]) -> dict[str, list[str]]:
    """Creating a dictionary from a dictionary and list."""
    results: dict[str, list[str]] = {}
    for key in new_list:
        results[key] = table[key]
    return results


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenating two dictionaries."""
    results: dict[str, list[str]] = {}
    for key in dict1:
        results[key] = dict1[key]
    for key in dict2:
        if key not in results.keys():
            results[key] = dict2[key]
        else:
            for i in dict2[key]:
                results[key].append(i)
    return results


def count(freq: list[str]) -> dict[str, int]:
    """A Count Function."""
    results: dict[str, int] = {}
    for item in freq:
        if item in results.keys():
            results[item] += 1
        else:
            results[item] = 1
            
    return results