def greetings(name="noble stranger"):Add commentMore actions
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)