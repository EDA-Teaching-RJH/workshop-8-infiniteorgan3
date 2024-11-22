import csv
def write_to_csv(data: list):
    try:
        with open("data.csv", "a") as writer:
            for i in data:
                datawritten = csv.DictWriter(writer, i.keys)
                writer.write(str(datawritten))
    except AttributeError:
        print("The list you have entered is not a list of dictionaries and so is invalid.")
        
data = [
{"name": "Rupert", "age": "20", "grade": "A"},
{"name": "Emma", "age": "21", "grade": "B"},
{"name": "Charlie", "age": "19", "grade": "C"}
]
write_to_csv(data)