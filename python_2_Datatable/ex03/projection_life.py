from load_csv import load

import matplotlib.pyplot as plt
import pandas as pd


def plot_life_vs_gdp(year: str):
    """Plot life expectancy vs GDP per capita for a given year."""
    income = load(
        "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("../life_expectancy_years.csv")
    if income is None or life is None:
        return

    # Extract year data
    income_s = pd.to_numeric(
        income.set_index("country")[year],
        errors="coerce"
    )
    life_s = pd.to_numeric(
        life.set_index("country")[year],
        errors="coerce"
    )

    # Align countries and drop missing values
    data = pd.concat([income_s, life_s], axis=1, join="inner")
    data.columns = ["gdp", "life"]
    data = data.dropna()

    # Plot
    plt.scatter(data["gdp"], data["life"])
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    # Log scale + custom ticks
    plt.xscale("log")
    plt.xlim(300, 10000)
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.show()


def main():
    try:
        plot_life_vs_gdp("1900")
    except (KeyError, ValueError, TypeError, KeyboardInterrupt) as e:
        print(type(e).__name__, e)


if __name__ == "__main__":
    main()
