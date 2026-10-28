import random, string


def generatecode():
    code = "".join(random.choices(string.ascii_letters+ string.digits, k=6))

    return code

code = generatecode()
print(code)