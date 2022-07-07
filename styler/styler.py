def to_snake_case(given_str: str) -> str:
    result: list = []

    for char in given_str:
        if char.isupper():
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)

    return "".join(result)


def to_camel_case(given_str: str) -> str:
    if len(given_str) == 0:
        return ""

    if given_str[0] == '_':
        given_str = given_str[1:]

    result: list = []
    next_uppercase: bool = False

    for char in given_str:
        if char == '_':
            next_uppercase = True
        elif next_uppercase:
            next_uppercase = False
            result.append(char.upper())
        else:
            result.append(char)

    return "".join(result)
