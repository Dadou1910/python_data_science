from load_csv import load


try:
    print(load("../population_total.csv"))
except (TypeError, FileNotFoundError, ValueError) as e:
    print(type(e), __name__, e)
