import pandas as pd

# Transfer all the csv data to variables.
path = "Simulations\\model15ScalarControl\\openCircuit\\T1FullSpeed\\"

Isa = pd.read_csv(path + "isa.csv")
Isb = pd.read_csv(path + "isb.csv")
Isc = pd.read_csv(path + "isc.csv")
Te = pd.read_csv(path + "Te.csv")
time = pd.read_csv(path + "time.csv")
Vab = pd.read_csv(path + "Vab.csv")
wm = pd.read_csv(path + "wm.csv")