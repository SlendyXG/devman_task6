password = input("Введите пароль: ")


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
	for letter in password:
	    if (letter.isalpha() == False) and (letter.isdigit() == False):
	    	return True
	return False


score = 0
functions = [is_very_long(password), has_digit(password), has_upper_letters(password), has_lower_letters(password), has_symbols(password)]
for function in functions:
	if function:
		score+=2


print('Рейтинг пароля:',score)