# Creating variables
name = "Luis"
age = 24
last_name = "Terrance"
found = False

# Extras so the code below runs without NameError
another_age = "26"  # string on purpose to demo int() casting
concatenation_example = "Hello, " + name + " " + last_name + "!"

print(name)
print(last_name)

# Concatenation / Casting
print("My name is: " + name + " and I'm " + str(age) + " years old")
print("Did he show up to class? " + str(found))
print(100 + int(another_age))         # 100 + 26 -> 126
print(concatenation_example)

# The f format
# f""" or f"""""""
print(f"My name is: {name}, and I'm {age} years old!")
print(f"""
My name is {name}
    and this is an example
of a triple double quoted f format
    """)

# The type() function helps us to know the data type of the variables
print(type(name))
print(type(found))
print(type(age))

# Casting
# str()  -> convert from any data type to string
# int()  -> convert string number to numeric values
# float() -> convert string number to float type

# Input function/method
# (with a tiny bit of safety so it doesn't crash on bad input)
user_text = input("Enter a new age: ").strip()

try:
    new_age = int(user_text)
except ValueError:
    print("That's not a valid integer. Defaulting new_age to 0.")
    new_age = 0

print(new_age + age)
