def clamp(n, table):
    if n < 0:
        return len(table) - 1
    elif n > len(table) - 1:
        return 0
    else:
        return n