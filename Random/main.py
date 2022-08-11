import random as rand

move=rand.randint(1,99)

print(move)

if move <= 33:
    print("Schere")

if move > 33 and move <= 66:
    print("Stein")
    
if move > 66:
    print("Papier")