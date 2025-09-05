# Ask for input - pass numbers in the terminal (int)
x = int(input("Give me your first number: "))
y = int(input("Give me your second number: "))

# Compare the numbers
if x == y:
    print("They're the same")
else: 
    print("They're different")

#shortened (do it on a single line)
print("Theyre the same") if x == y else print ("They're different")

