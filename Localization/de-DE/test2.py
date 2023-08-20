import os

altes_wort = "zielsuchende"
neues_wort = "zielsuchenden"
ordner_pfad = r"C://Users//David//Documents//My Games//Terraria//tModLoader//ModSources//CalamityDe//Localization//de-DE"

for ordnername, unterordner, dateien in os.walk(ordner_pfad):
    for datei in dateien:
        if datei.endswith(".hjson"):
            datei_pfad = os.path.join(ordnername, datei)
            with open(datei_pfad, "r") as f:
                inhalt = f.read()
            inhalt_neu = inhalt.replace(altes_wort, neues_wort)
            with open(datei_pfad, "w") as f:
                f.write(inhalt_neu)