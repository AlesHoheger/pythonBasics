
# naloga 8.2

secret = input("Imamo nagradno vprašanje za vas. Uganite skrito število od 1 do 9: ")

if secret == "5":
    print("Čestitamo, uganili ste skrito številko!")
elif (secret == "4") or (secret == "6"):
    print("Blizu, ampak žal niste ugotovili.")
else:
    print("Napačno, več sreče prihodnjič.")

