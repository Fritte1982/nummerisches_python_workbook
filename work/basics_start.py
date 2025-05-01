from icecream import ic

DATA_PATH = (
        r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training" +
        r"\Python-ordner-a\python-scripts_vs-code\sonstige_projekte\numerisches_python\data"
)
OUTPUT_PATH = (
        r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training" +
        r"\Python-ordner-a\python-scripts_vs-code\sonstige_projekte" +
        r"\numerisches_python\output"
)
dateiname_input = r"\bundeslaender.txt"
out_dateiname: str = r"\beispiel.txt"
out_bundeslaender: str = r"\bundeslaender2.txt"

out_datei_pfad: str = OUTPUT_PATH + out_bundeslaender
pfad_datei_in = DATA_PATH + dateiname_input

fobj = open(pfad_datei_in, encoding="UTF8")
zeilen = fobj.readlines()
ic(zeilen[:4])

with open(pfad_datei_in, encoding='utf8') as fh:
    for zeile in fh:
        ic(zeile)

fh = open(out_datei_pfad, "w", encoding="UTF8")

fh.write("1. Zeile\n")
fh.write("2. Zeile\n")
fh.close()
txt = open(out_datei_pfad, "r", encoding="utf8").read()
ic(txt)

with open(pfad_datei_in, encoding="utf8") as fh_in, \
        open(out_datei_pfad, "w", encoding="utf8") as fh_out:
    fh_in.readline()  # lesen der headerzeile
    fh_out.write("Land Flaeche Einwohner Dichte\n")
    for zeile in fh_in:
        land, flaeche, maennlich, weiblich = zeile.split()
        flaeche = float(flaeche)
        einwohner = int(maennlich) + int(weiblich)
        dichte = round(einwohner * 1000 / flaeche, 2)
        fh_out.write(land + " " + str(flaeche) + " " + str(einwohner)
                     + " " + str(dichte) + "\n")
