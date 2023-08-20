import os

suchwort = "Räuberschlitzer"
ordner_pfad = r"C://Users//David//Documents//My Games//Terraria//tModLoader//ModSources//CalamityDe//Localization//de-DE"

for ordnername, unterordner, dateien in os.walk(ordner_pfad):
    for datei in dateien:
        if datei.endswith(".hjson"):
            datei_pfad = os.path.join(ordnername, datei)
            with open(datei_pfad, "r") as f:
                inhalt = f.read()
                if suchwort in inhalt:
                    print(f"Das Wort wurde in {datei_pfad} gefunden.")
