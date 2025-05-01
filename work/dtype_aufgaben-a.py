from pprint import pprint

import numpy as np

dt = np.dtype([("ID", np.int32),
               ("Preis", np.float16)])
dt_menge = np.dtype([("Anzahl_verkaufte", np.int8)])

daten_aufgabe = [(1, 22.50),
                 (2, 220.50),
                 (3, 52.50),
                 (4, 122.50)]
menge_verkauf_dat = [3, 5, 2, 1]
array_menge = np.array(menge_verkauf_dat, dtype=dt_menge)
array_aufgabe = np.array(daten_aufgabe, dtype=dt)
pprint(array_aufgabe)
print(array_aufgabe[2][1])

erlös = array_aufgabe["Preis"] * array_menge["Anzahl_verkaufte"]
gesamt_erlös = erlös.sum()
pprint(erlös)
print(f"Der Gesamterlös ist {gesamt_erlös} Euro ")

time_type = np.dtype([('h', int),
                      ('min', int),
                      ('sec', int)
                      ])
times = np.array([(11, 38, 5),
                  (14, 56, 0),
                  (3, 9, 1)], dtype=time_type)
dt_temp = np.dtype([("Celsius",np.float_)])
new_dtype = np.dtype(times.dtype.descr + [('temperaturen', 'i4')])
temparturen = [22, 33, 15]
temparturen = np.array(temparturen, dtype=dt_temp)
extend_times = np.zeros(times.shape, dtype=new_dtype)
# times["temperature"] = temparturen["Celsius"]
for name in times.dtype.names:
    extend_times[name] = (times[name])
extend_times["temperaturen"] = temparturen["Celsius"]
print(extend_times)
