How to use these scripts:

1. Install Python.
2. Run this command on Windows: "py -m pip install collections pathvalidate pathlib". Run this command on Linux/MacOS: "python3 -m pip install collections pathvalidate pathlib".
3. Ensure there is a file in the same directory as the scripts called "Postkarten.csv" that contains the data.
4. To generate the routes for QGIS run this command on Windows: "py route_qgis.py" or this command on Linux/MacOS: "python3 route_qgis.py". This will generate the routes in the folder called Routes as KML files ready to be imported into QGIS. A QGIS project with all these files and the CSV file used to generate the routes are included in the repository.
5. After the source data is updated you may wish to newly generate the places from the "Schlagwörter" column. For this run this command on Windows: "py extract_normalize.py" or this command on Linux/MacOS: "python3 extract_normalize.py". It may be best to run this script on a CSV file only containing newly added or updated rows because this script will overwrite the columns containing the place names which will make it necessary to normalize places and re-generate the coordinates in OpenRefine before generating the routes again.

These scripts were generated for a student project at the Humboldt-Universität Berlin in the project seminar Motiv, Message, Marke (WS 2025/26) by Ben Kaden and Ira Kokoshko with data provided by Ben Kaden.
