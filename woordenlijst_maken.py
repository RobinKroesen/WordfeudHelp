woorden = open("Woordenlijst.txt", "r")

woorden_lijst = woorden.read().split('\n')

letters = "abcdefghijklmnopqrstuvwxyz"

for woord in woorden_lijst:
    for letter in woord:
        if letter not in letters:
            woorden_lijst.remove(woord)
            break

nieuwe_lijst = open("Woorden.txt", "w")
for woord in woorden_lijst:
    nieuwe_lijst.write(woord + "\n")
nieuwe_lijst.close()
