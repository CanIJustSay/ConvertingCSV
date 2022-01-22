import pandas as pd

df = pd.read_csv("main.csv")

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()

nMass = []
nRadius = []
gravity = []

for i in range(1, 100, 2):
    m = float(mass[i]) * 1.989e+30
    r = float(radius[i]) * 6.957e+8
    nMass.append(m)
    nRadius.append(r)
    g = (6.67 * pow(10, -11)) * m/r**2

    gravity.append(g)

newDF = pd.DataFrame({
    "Radius": nRadius,
    "Mass": nMass,
    "Gravity": gravity
})

newDF.to_csv("completeCSV.csv")