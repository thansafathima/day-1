import random

movies = ["Drishyam","Jaibhim","Dangal","Raazi","Kaithi",
          "vikram", "amaran", "Vikram", "lucifer", "Gravity"]

movie = random.choice(movies)

display = []

for i in movie:
    display.append("_")

while "_" in display:

    print(" ".join(display))

    letter = input("Enter a letter: ").lower()

    for i in range(len(movie)):
        if movie[i] == letter:
            display[i] = letter

print("\nCongratulations!")
print("Movie:", movie)
