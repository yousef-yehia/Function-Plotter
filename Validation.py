def validate_function_characters(func):
    valid_chars = set("0123456789xXeE+-*/^(). ")
    if not all(c in valid_chars for c in func):
        raise ValueError("Invalid characters in the function.")


def validate_min_max(min, max):
    if (min > max):
        raise ValueError("minimum value of x can't be larger than maximum value of x.")
