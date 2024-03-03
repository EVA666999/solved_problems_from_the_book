def valid_pass(password):
    correct_lenght = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    is_valid = False
    if len(password) >= 7:
        correct_lenght = True
    for word in password:
        if word.isupper():
            has_uppercase = True
        if word.islower():
            has_lowercase = True
        if word.isdigit():
            has_digit = True
    if correct_lenght and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    return is_valid
    

print(valid_pass('Я1папапапап'))


def literal(my_str, delimetr):
    a = my_str.split(delimetr)
    for i in a:
        print(i)

print(literal('Я.Я.я.1.3', '.'))
print(literal('Я:Я:я:1:3', ':'))