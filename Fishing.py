print("List of the fish:")
fish_strength = {"goldfish":3, "catfish":5, "salmon":7}
for key, value in fish_strength.items():
    print(key)
fishing_rod = {"red":4, "blue":8, "green":6}
print()
print("Color of the rod:")
for key, value1 in fishing_rod.items():
    print(key)
print()
while True:
    rod = input("Choose the rod you want to use: ")
    fish = input("Choose the fish you want to catch: ")
    if fishing_rod[rod] < fish_strength[fish]:
        print("Rod is broken, try using another one.")
    else:
        comment = input("You've caught a fish! Would you like to catch another?: "'\n')
        if comment.lower() == "no":
            print("\nThank you for playing!")
            break
