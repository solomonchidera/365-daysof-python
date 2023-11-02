def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


def get_greet(name):
    return f"Hi {name}"


get = get_greet("Moniaar")
print(get)
greet("Solomon", "Chidera")
