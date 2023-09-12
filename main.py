import string


def check_password(password):
    length = len(password)

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, special, digits]

    score = 0

    with open('common_pass.txt', 'r', encoding='utf-8') as f:
        common = f.read().splitlines()

    if password in common:
        pass
    else:
        if length > 8:
            score += 1
        if length > 11:
            score += 1
        if length > 14:
            score += 1

        if sum(characters) > 1:
            score += 1
        if sum(characters) > 2:
            score += 1
        if sum(characters) > 3:
            score += 1

    stars = int((score/6)*10)//2

    if stars:
        print("score:", "* "*stars)

    if score == 0:
        print("your password is common")
    elif 1 <= score < 4:
        print("your password is Weak")
    elif score == 4:
        print("your password is Ok")
    elif 4 < score < 6:
        print("your password is pretty Good")
    else:
        print("your password is Excellent")
    print("################################")

    return stars


print("\nMake sure Password contains the following:\n->Upper Case(A - Z)\n->Lower Case(a - z)\n->Numbers(0 - 9)\n->Special Character(!,@,#....)")
pswd = input("Input: ")
while pswd != "exit":
    output = check_password(pswd)
    if output == 5:
        break
    print("\nMake sure Password contains the following:\n->Upper Case(A - Z)\n->Lower Case(a - z)\n->Numbers(0 - 9)\n->Special Character(!,@,#....)")
    pswd = input("Input: ")
    