def upperCase(character):
    def wrapper():
        ch = character()
        answer = ch.upper()
        return answer

    return wrapper()

@upperCase
def print1():
    hello_ = input()
    return hello_

@upperCase
def print2():
    hello_ = input()
    return hello_

@upperCase
def print3():
    hello_ = input()
    return hello_

@upperCase
def print4():
    hello_ = input()
    return hello_

print(print1, print2, print3, print4)
