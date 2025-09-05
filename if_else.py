# if else statements
# Execute some logic or instructions if (and only IF) the condition it's met
# We can catch with an else in case that the condition doesn't match

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Greater than: a > b
# Less than or equal: a <= b
# Greater than or equal: a >= b

age = 24

if age < 100:
    if age < 21:
        print("You're a minor without access")
    else:
        print("You're young")
elif age == 100:
    print("Congratulations, you got to live 100 years!")
else:
    print("Sorry, you're getting old!")

#exercise
x = 8
y = 8
if x > y:
    print("Hello")
else:
    print("Welcome")
