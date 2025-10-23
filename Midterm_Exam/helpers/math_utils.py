def area(l, w):
    """Calculate area of a rectangle."""
    if type(l) not in [int, float] or type(w) not in [int, float]:
        return "Error: Both inputs must be numbers"
    return l * w