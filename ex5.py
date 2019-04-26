name = 'Zed A. Shaw'
age = 35  # totally a lie
height = 74  # puppies
weight = 180  # potatoes
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# converting for the do more exc.
weight_kg = weight / 0.453
height_cm = height * 2.54
rounded_kg = round(weight_kg)
rounded_cm = round(height_cm)

print(f"Let's talk about {name}.")
print(f"He's {height} puppies tall.")
print(f"That's {rounded_cm} cms tall.")
print(f"He's {weight} potatoes heavy.")
print(f"That's {rounded_kg} kilos heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

# this line is tricky, try to get it exactly right (kek)
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
