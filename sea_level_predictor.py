import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Leer datos
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Crear scatter plot (Year vs CSIRO Adjusted Sea Level)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Línea de mejor ajuste usando TODOS los datos (desde 1880)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Rango de años extendido hasta 2050
    years_all = pd.Series(range(1880, 2051))
    sea_level_all = res_all.slope * years_all + res_all.intercept

    ax.plot(years_all, sea_level_all, label="Fit 1880-2050")

    # 4. Nueva línea de mejor ajuste usando datos desde el año 2000
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )

    years_2000 = pd.Series(range(2000, 2051))
    sea_level_2000 = res_2000.slope * years_2000 + res_2000.intercept

    ax.plot(years_2000, sea_level_2000, label="Fit 2000-2050")

    # 5. Títulos y etiquetas
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # (Opcional) Si quieres, podrías mostrar la leyenda:
    # ax.legend()

    # Guardar y devolver
    plt.savefig("sea_level_plot.png")
    return ax
