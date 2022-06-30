def to_snake_case(target_str: str) -> str:
    result = []

    for char in target_str:
        if char.isupper():
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)

    return "".join(result)
