from aff_life import show_graph, load


print("TEST 1: Normal graph creation")
print("Expected: Graph window opens\n")
show_graph()


print("\n-----------------------------------")
print("TEST 2: load() with wrong type (int)")
print("Expected: Error message, no crash\n")
load(123)


print("\n-----------------------------------")
print("TEST 3:with non-existing file")
print("Expected: Error message about file\n")
load("this_file_does_not_exist.csv")
