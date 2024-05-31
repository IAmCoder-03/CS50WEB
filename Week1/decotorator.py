
def announce(f):
    def warrper():
        print("About to the function...")
        f() # Chay ham doi so hello()
        print("Done with the function...")
    return warrper

@announce #Doi so la ham
def hello():
    print("Hello, world!")
hello()