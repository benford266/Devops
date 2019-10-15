text = "map"

table = str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")

print(text.translate(table))