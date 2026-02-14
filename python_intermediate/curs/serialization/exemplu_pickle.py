import pickle


data = {
    "a": [1, 4.5, 100, 45.34],
    "b": ("Ana are mere", "Python is cool"),
    "c": True,
}

# Important! Accesam fisiere cu modul "b" (binary)
# Pentru ca pickle salveaza datele in format binar
# f = open("data.pickle", "wb")
# pickle.dump(data, f)
# f.close()
# SAU
with open("data.pickle", "wb") as f:
    # Scriem datele in fisier
    pickle.dump(data, f)

with open("Data.pickle", "rb") as f:
    # Citim datele din fisier
    loading_data = pickle.load(f)
    print(loading_data)
