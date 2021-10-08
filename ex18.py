#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2},{arg3}")
#ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2},{arg3}")

#this just take one argument
def print_one(arg1, arg2):
    print(f"arg1: {arg1}, {arg2}")
#this one takes no arguments
def test(abc1, abc2):
    print(f"I got nothing'.", f"Cerrar, {abc1}, {abc2}")
def print_none():
    print("Cerramos")
print_two("Naofal", "Ftouh" , "SAid")
print_two_again("Naofal", "Ftouh", "Said")
print_one("First!", "Adios")
test("NAda", "de nada")
print_none()

