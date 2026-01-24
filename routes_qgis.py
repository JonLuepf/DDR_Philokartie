import csv, collections, pathvalidate
from pathlib import Path

output_folder = Path("./Routes")
output_folder.mkdir(parents=True, exist_ok=True)
def generate_kml(data):
    placemarks = ""
    for row in data:
        if row["Absendeort Koordinaten"] and row["Empfangsort Koordinaten"]:
            start_coordinate_lat = row["Absendeort Koordinaten"].split(",")[0]
            start_coordinate_long = row["Absendeort Koordinaten"].split(",")[1]
            start_coordinate = f"{start_coordinate_long},{start_coordinate_lat}"
            end_coordinate_lat = row["Empfangsort Koordinaten"].split(",")[0]
            end_coordinate_long = row["Empfangsort Koordinaten"].split(",")[1]
            end_coordinate = f"{end_coordinate_long},{end_coordinate_lat}"
            coordinates = f"{start_coordinate} {end_coordinate}"
            placemark = f"""  <Placemark>
	            <Style><LineStyle><color>ff0000ff</color></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>
                <MultiGeometry><LineString><coordinates>{coordinates}</coordinates></LineString></MultiGeometry>
                </Placemark>"""      
            placemarks = placemarks + placemark + "\n"
            xml = f"""<?xml version="1.0" encoding="utf-8" ?>
            <kml xmlns="http://www.opengis.net/kml/2.2">
            <Document id="root_doc">
            <Schema name="test" id="test">
            	<SimpleField name="id" type="float"></SimpleField>
            </Schema>
            <Folder><name>test</name>
            {placemarks}
            </Folder>
            </Document></kml>"""
    if placemarks == "":
        return ""
    else:
        return xml
with open("Postkarten.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    data = [row for row in csv_reader]

data_grouped = collections.defaultdict(list)
for item in data:
    data_grouped[item['Absendeort']].append(item)
for start_place in data_grouped:
        xml = generate_kml(data_grouped[start_place])
        if xml != "":
            with open(output_folder / f"Absendeort_{pathvalidate.sanitize_filename(start_place)}.kml", "w") as f:
                f.write(xml)
data_grouped = collections.defaultdict(list)
for item in data:
    data_grouped[item['Empfangsort']].append(item)
for end_place in data_grouped:
        xml = generate_kml(data_grouped[end_place])
        if xml != "":
            with open(output_folder / f"Empfangsort_{pathvalidate.sanitize_filename(end_place)}.kml", "w") as f:
                f.write(xml)