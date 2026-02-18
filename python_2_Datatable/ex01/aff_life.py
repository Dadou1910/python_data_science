from load_csv import load

import matplotlib.pyplot as plt
import numpy as np


def show_graph():
    """Creates a graph from a loaded cvs file"""
    try:
        file = load("../life_expectancy_years.csv")
        if file is None:
            return
        france = file[file["country"] == "France"]
        years = france.columns[1:].astype(int)
        values = france.iloc[0, 1:].astype(float)

        plt.plot(years, values)
        plt.xticks(np.arange(min(years), max(years)+1, 40))
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except (TypeError, ValueError, EOFError, KeyboardInterrupt) as e:
        print(type(e), __name__, e)


def main():
    show_graph()


if __name__ == '__main__':
    main()
