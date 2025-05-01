import pickle
from pprint import pprint
import numpy as np
import os

OUTPUT_PATH = (
        r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a\python-scripts_vs-code" +
        r"\sonstige_projekte\numerisches_python\output"
)
SOURCE_PATH = (r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a" +
               r"\python-scripts_vs-code\sonstige_projekte\numerisches_python\data")

PKL_IN_PATH = SOURCE_PATH + r"\cities_and_times.pkl"

lst = [
    [115, 230.9, 229.2, 234],
    [117, 229, 232.1, 235],
    [116, 140, 141, 142]
]
Density = np.dtype([('density', np.int32)])
Pixel = np.dtype(np.uint8)
print(Pixel)
A = np.array(lst, dtype=Pixel)
x = np.array([(393,), (337,), (256,)],
             dtype=Density)
pprint(A)
pprint(x)
print(x['density'])
print(Density.name, Density.byteorder, Density.itemsize)
dt = np.dtype([('country', np.unicode_, 25),
               ('density', 'i4'),
               ('area', 'i4'),
               ('population', 'i4')])

population_table = np.array([('Netherlands', 393, 41526, 16928800),
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
                            dtype=dt)
print(x[:4])
pprint(population_table)
s = population_table['country'][0]
print(s, type(s))
CSV_OUT = OUTPUT_PATH + r"\population_table.csv"
print(os.getcwd())

np.savetxt(CSV_OUT, population_table, fmt="%s;%d;%d;%d",
           delimiter=";")

dt = np.dtype([('country', np.unicode_, 20),
               ('density', 'i4'),
               ('area', 'i4'),
               ('population', 'i4')])
x = np.genfromtxt(CSV_OUT,
                  dtype=dt,
                  delimiter=";")

x = np.loadtxt(CSV_OUT,
               dtype=dt,
               delimiter=";")

print(population_table.dtype.names)
population_table.dtype.names = ('Land',
                                'Bevölkerungsdichte',
                                'Fläche',
                                'Bevölkerung')

lands = ['Niederlande', 'Belgien', 'Vereinigtes Königreich',
         'Deutschland', 'Liechtenstein', 'Italien', 'Schweiz',
         'Luxemburg', 'Frankreich', 'Österreich', 'Griechenland',
         'Irland', 'Schweden', 'Finnland', 'Norwegen']
population_table['Land'] = np.array(lands, dtype='<U25')

pprint(population_table)
fh = open(PKL_IN_PATH, "br")
cities_and_times = pickle.load(fh)
for i in range(5):
    print(cities_and_times[i])
time_type = np.dtype([('city', 'U30'),
                      ('day', 'U3'),
                      ('time', [('h', int), ('min', int)])])
times = np.array(cities_and_times, dtype=time_type)
pprint(times)
lst = []
for row in times:
    t = row[2]
    t = f"{t[0]:02d}:{t[1]:02d}"
    lst.append((row[0], row[1], t))
time_type = np.dtype([('city', 'U30'),
                      ('day', 'U3'),
                      ('time', 'U5')])
times2 = np.array(lst, dtype=time_type)
print(times2)

CITY_TIMES_CSV_OUT = OUTPUT_PATH + r"\cities_and_times.csv"

with open( CITY_TIMES_CSV_OUT,"w") as fh:
    for city_data in times2:
        fh.write(",".join(city_data) + "\n")
