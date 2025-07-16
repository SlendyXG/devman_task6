def is_very_long(password):
    result = len(password) > 12
    return result


def has_digit(password):
    return any(digit.isdigit() for digit in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isalpha() and not letter.isdigit() for letter in password)


def main():
    password = input("Введите пароль: ")
    score = 0
    functions = [
        is_very_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password),
    ]
    for function in functions:
        if function:
            score+=2
    print('Рейтинг пароля:', score)


if __name__ == '__main__':
    main()
