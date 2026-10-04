import csv
import io
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if "csvFile" not in request.files:
            return {"error": "File missing!"}, 400

        file = request.files["csvFile"]
    
        if file.filename == "":
            return {"error" : "No Selected file"}, 400

        if file and file.filename.endswith(".csv"):
            try:
                stream = io.StringIO(file.stream.read().decode("UTF-8"))
    
                reader = csv.DictReader(stream)
                data_structure = [row for row in reader]
                print(data_structure[0])

                return{"message" : "CSV processed successfully", "row_count" : len(data_structure)}, 200
        
            except Exception as e:
                return {"error" : f"Procession failed: {str(e)}"}, 500
    else:
        return render_template("index.html")
