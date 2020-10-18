
# naloga 8.2

secret = 5
guess = None


while guess != secret:

    guess = int(input("Imamo nagradno vprašanje za vas. Uganite skrito število od 1 do 9: "))

    if guess == secret:
        print("Čestitamo, uganili ste skrito številko!")

    elif (guess == (secret -1)) or (guess == (secret + 1)):
        print("Blizu, ampak žal niste ugotovili.")
    else:
        print("Napačno, več sreče prihodnjič.")

print("konec programa!")


