import numpy as np
from own_package import path_attributes as pa
import pickle as pkl

OUTPUT_DIR = pa.OUTPUT_DIR

Pixel = np.dtype(np.uint8)
print(Pixel)

lst = [ [115, 230.9, 229.2, 234],
[117, 229, 232.1, 235],
[116, 140, 141, 142] ]

A = np.array(lst, dtype=Pixel)
print(A)

Density = np.dtype([("density", np.int32)]) # Spalte erzeuge (für Tabelle 'Bundeslaender')
x = np.array([(393,),(337,),(256,)], dtype=Density)   # array mit der Spalte density als dtype
print(x)
print(repr(x))
print(x["density"])

laender_dtype = np.dtype([
    ("country", "O"),   # O für Objekt speichert ohne präfix b, im Gegenteil zu 'S20'
    ("density", "i4"),
    ("area", "i4"),
    ("population", "i4")
])

population_table = np.array([
('Netherlands', 393, 41526, 16928800),
('Belgium', 337, 30510, 11007020),
('United Kingdom', 256, 243610, 62262000),
('Germany', 233, 357021, 81799600),
('Liechtenstein', 205, 160, 32842),
('Italy', 192, 301230, 59715625),
('Switzerland', 177, 41290, 7301994),
('Luxembourg', 173, 2586, 512000),
('France', 111, 547030, 63601002),
('Austria', 97, 83858, 8169929),
('Greece', 81, 131940, 11606813),
('Ireland', 65, 70280, 4581269),
('Sweden', 20, 449964, 9515744),
('Finland', 16, 338424, 5410233),
('Norway', 13, 385252, 5033675)],
dtype=laender_dtype)

print(population_table['density'])
print(population_table['country'])
print(population_table['area'][2:5])

population_table_path = OUTPUT_DIR / "population_table_b.csv"

np.savetxt(population_table_path, population_table,fmt="%s;%d;%d;%d", delimiter=";")

dtype_populatio_tbl = np.dtype([
    ("country", "U20"),
    ("density",'i4'),
    ("area", "i4"),
    ("population", "i4")
])

popul = np.genfromtxt(population_table_path, dtype=dtype_populatio_tbl, delimiter=";")
popul_tbl = np.loadtxt(population_table_path, dtype=dtype_populatio_tbl, delimiter=";")
deutsche_spaltennamen = ('Land',
'Bevölkerungsdichte',
'Fläche',
'Bevölkerung')
popul_tbl.dtype.names = deutsche_spaltennamen
print(popul_tbl["Land"])

deutsche_laendernamen = ['Niederlande', 'Belgien', 'Vereinigtes Königreich',
'Deutschland', 'Liechtenstein', 'Italien', 'Schweiz',
'Luxemburg', 'Frankreich', 'Österreich', 'Griechenland',
'Irland', 'Schweden', 'Finnland', 'Norwegen']

popul_tbl["Land"] = np.array(deutsche_laendernamen, dtype='U20')
print(popul_tbl)

cities_and_times_in = pa.SOURCE_DIR / "cities_and_times.pkl"
cities_and_times_out = pa.OUTPUT_DIR / "cities_and_times_b.csv"


fh = open(cities_and_times_in, "rb")
cities_and_times = pkl.load(fh)
for i in range(5):
    print(cities_and_times[i])

time_type = np.dtype([
    ("city", "U30"),
    ("day", "U3"),
    ("time", [("h", int), ("min", int)])
])

times = np.array(cities_and_times, dtype=time_type)
print(times[:4])

lst = []
for row in times:
    t = row[2]
    t = f"{t[0]:02d}:{t[1]:02d}"
    lst.append((row[0], row[1], t))

time_type = np.dtype([
    ('city', 'U30'),
    ('day', 'U3'),
    ('time', 'U5')])

times2  = np.array(lst, dtype=time_type)
print( times2[:10])

with open(cities_and_times_out, "w", encoding="utf-8") as f:
    for city_data in times2:
        f.write(",".join(city_data) +"\n")