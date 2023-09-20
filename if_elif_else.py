#Simple if, elif, else stuff. Obvious from what you can see.

aa = 35
bb = 68
addit = aa + bb

if (addit > 100):
    print("That's a big number!")
    if (addit < 200):
        print("Loser.")
elif (addit < 100):
    print("That's a small number.")
else:
    print("What?? How did you get here?")