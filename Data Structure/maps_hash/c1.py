def staircase(n):
    """
    Given the number of stairs and wanna see how many ways i can climbs that stairs of i can go up in 1 step and 2 , 3 steps

    Args:
       n : number of steps
    Returns:
      integer : integer will represent how much method u can go up
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
