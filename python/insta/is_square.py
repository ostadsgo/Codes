from math import sqrt 



# define a function that return `True` if n is square otherwise return `False`
def is_square(n: int) -> bool:
    """ A function that returns 'True' if `n` is square 
        Otherwise return 'False'
    n: int = a integer number
    """
    if n >= 0:
        sq = sqrt(n)
        if int(sq) == sq:
            return True
        else:
            return False
    else:
        return False

    
