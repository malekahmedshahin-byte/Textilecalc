def validate_positive(value, name="Value"):
    """
    Validate that a numeric value is positive (greater than 0).

    Args:
        value: The numeric value to validate
        name (str): Name of the parameter (used in error message)

    Returns:
        value if valid

    Raises:
        TypeError: If value is not a number
        ValueError: If value is not positive
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}.")
    if value <= 0:
        raise ValueError(f"{name} must be a positive number greater than 0. Got: {value}")
    return value


def validate_percentage(value, name="Value"):
    """
    Validate that a value is a valid percentage (0 to 100 inclusive).

    Args:
        value: The numeric value to validate
        name (str): Name of the parameter

    Returns:
        value if valid

    Raises:
        ValueError: If value is not between 0 and 100
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}.")
    if not (0 <= value <= 100):
        raise ValueError(f"{name} must be between 0 and 100. Got: {value}")
    return value


def validate_non_negative(value, name="Value"):
    """
    Validate that a value is zero or positive.

    Args:
        value: The numeric value to validate
        name (str): Name of the parameter

    Returns:
        value if valid
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}.")
    if value < 0:
        raise ValueError(f"{name} must be 0 or positive. Got: {value}")
    return value
