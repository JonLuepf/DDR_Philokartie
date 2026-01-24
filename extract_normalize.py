import csv

data = []
with open("Postkarten.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        keywords = row["Schlagwörter"].split("; ")
        for keyword in keywords:
            if keyword.startswith("von: "):
                start_position = keyword.replace("von: ","")
            if keyword.startswith("nach: "):
                end_position = keyword.replace("nach: ","")
            if keyword.startswith("Mensch"):
                keyword_split = keyword.split()
                for item in keyword_split:
                    if item.isnumeric():
                        people_amount = item
                if "keine" in keyword:
                    people_amount = "0"
        if "von: " in row["Schlagwörter"]:
            row["Absendeort"] = start_position
        else:
            row["Absendeort"] = "o.A."
            row["Absendeort Koordinaten"] = ""
        if "nach: " in row["Schlagwörter"]:
            row["Empfangsort"] = end_position
        else:
            row["Empfangsort"] = "o.A."
            row["Empfangsort Koordinaten"] = ""
        row["Anzahl Menschen"] = people_amount
        year = row["Jahr Motiv"]
        year = "".join(c for c in year if  c.isdecimal())
        if len(year) != 4:
            year = ""
        row["Jahr Motiv bereinigt"] = year
        data.append(row)
with open("Postkarten.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=row.keys())
    writer.writeheader()
    writer.writerows(data)