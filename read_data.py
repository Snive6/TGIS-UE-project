def read_data(filename: str):
    f = open("Datasets/" + filename, "r")
    data = [[float(n) for n in line.split(';')] for line in f]
    return data
