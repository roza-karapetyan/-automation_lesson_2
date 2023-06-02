def is_year_leap (n):
    if (n % 4 == 0):
        print("год ", n,":", True)
    else:
        print("год ", n,":", False)


is_year_leap (2021)