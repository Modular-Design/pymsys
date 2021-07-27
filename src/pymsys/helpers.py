
def includes(array: [], elements: []) -> bool:
    for e in elements:
        if not e in array:
            return False
    return True
