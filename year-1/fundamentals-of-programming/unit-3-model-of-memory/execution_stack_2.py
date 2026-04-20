def one():
    print("starting function one")
    print("calling function two")
    two()

def two():
    print("starting function two")
    print("calling function three")
    three()

def three():
    print("starting function three")
    print("done")

one()