import random

secret = random.randint(1, 9)

poizkus = 0
while True:
    poizkus += 1
    guess = int(input("Imamo nagradno vprašanje za vas. Uganite skrito število od 1 do 9: "))
    print("to je vaš " + str(poizkus) + ". poizkus")

    if guess == secret:
        print("Čestitamo, uganili ste skrito številko!")
        with open("highscore.txt", "r") as scores:
            best_score = int(scores.read())
        if poizkus < best_score:
            with open("highscore.txt, "a") as scores:
                scores.write(str(poizkus))

        break
    elif (guess == (secret -1)) or (guess == (secret + 1)):
        print("Blizu, ampak žal niste ugotovili.")
    else:
        print("Napačno, več sreče prihodnjič.")

print("konec programa!")


