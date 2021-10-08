# This one is like your scripts with srgv.
def print_two(*argv):
    arg1, arg2 = argv
    print(f"arg1: {arg1}, arg2 {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"my name is {arg1}, my colleague's name is {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1, {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("zed","shaw")
print_two_again("Said","Naofal")
print_one("first!")
print_none()