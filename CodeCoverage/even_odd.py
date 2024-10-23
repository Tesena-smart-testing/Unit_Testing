def check_number(number):
    if number == 0:
        return "zero"
    elif number > 0:
        if number % 2 == 0:
            return "positive even"
        else:
            return "positive odd"
    else:
        if number % 2 == 0:
            return "negative even"
        else:
            return "negative odd"

