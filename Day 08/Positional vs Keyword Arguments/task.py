def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


user_name = input("What's your name? ")
user_location = input("What's your location? ")
greet_with(user_name,user_location)
greet_with(name=user_name,location=user_location)