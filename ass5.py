def swap_case(function):
    def wrapper():
        str=function()
        print(str)
        return str.swapcase()
    return wrapper


@swap_case
def input_string():
    str=input("Enter input string")
    return str

print(input_string())
