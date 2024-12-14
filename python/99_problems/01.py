def last_element(items: list[str]) -> str | None:
    """ Return last item of the list
        if list empty return None
    """
    if items:
        return items[-1]

def test_01():
    assert last_element(["a", "b", "c", "d"]) == "d"
    assert last_element([]) == None

def last_pair(items):
    """ Return last two elements of the list"""
    if len(items) >= 2:
        return tuple(items[-2:])

def test_02():
    assert last_pair(["a", "b", "c", "d"]) == ("c", "d")
    assert last_pair(["a"]) == None
    assert last_pair([]) == None


