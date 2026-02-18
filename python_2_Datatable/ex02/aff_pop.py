import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def to_millions(x):
    """Converts input into numbers in millions"""
    s = str(x)
    if s.endswith("M"):
        return float(s[:-1])
    if s.endswith("k"):
        return float(s[:-1]) / 1000
    return float(s)


def main():
    """Creates a graph comparing the total population of two countries."""
    try:
        file = load("../population_total.csv")
        if file is None:
            return

        fr = file[file["country"] == "France"]
        be = file[file["country"] == "Belgium"]

        if fr.empty or be.empty:
            print("Country not found")
            return

        years = [str(y) for y in range(1800, 2051)]

        fr_vals = fr[years].iloc[0].apply(to_millions)
        be_vals = be[years].iloc[0].apply(to_millions)

        x = list(range(1800, 2051))

        plt.plot(x, fr_vals, label="France")
        plt.plot(x, be_vals, label="Belgium")

        plt.xticks(np.arange(1800, 2051, 40))
        plt.yticks(np.arange(0, 61, 20), [f"{y}M" for y in range(0, 61, 20)])

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        plt.legend(loc="lower right")

        plt.show()

    except (KeyError, ValueError, TypeError, KeyboardInterrupt) as e:
        print(type(e).__name__, e)


if __name__ == "__main__":
    main()
