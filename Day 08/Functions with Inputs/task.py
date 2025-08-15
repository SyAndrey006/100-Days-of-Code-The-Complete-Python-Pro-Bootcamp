def greet():
    print("Hello")
    print("How do u do?")
    print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do u do, {name}?")
    print(f"Isn't the weather nice today, {name}?")

user_name = input("What's your name? ")
greet_with_name(user_name)