bill = float(input("What was the bill total?"))
num_of_people = int(input("how many people are splitting the bill?"))
tip = float(input("what tip % would you like to give?"))

total = bill / num_of_people * (tip / 100 + 1)
total = "{:.2f}".format(total)
print(f"You should pay ${total}")
