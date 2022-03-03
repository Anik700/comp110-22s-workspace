"""Here is my Dictionary."""
__author__ = "730243145"


# invert function defined
def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverting The Dictionary."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result.keys():
            raise KeyError
        result[a[key]] = key
    return result


# Fav_color function defined
def favorite_color(a: dict[str, str]) -> str:
    """Favorite Color Generator."""
    result: dict[str, int] = {}
    for key in a:
        if a[key] in result.keys():
            result[a[key]] += 1
        else:
            result[a[key]] = 1
    print(result)
    mode = ""
    count = 0
    for key in result:
        if result[key] > count:
            mode = key
            count = result[key]
    
    return mode


# count functiond defined
def count(x: list[str]) -> dict[str, int]:
    """Counting Dictionary Values."""
    result: dict[str, int] = {}
    for item in x:
        if item in result.keys():
            result[item] += 1
        else:
            result[item] = 1
    return result

    