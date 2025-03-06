from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path})

@app.route("/data", methods=["GET"])
def get_data():
    file_name = request.args.get("file", "")
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    df = pd.read_csv(file_path)
    return jsonify({"columns": list(df.columns), "preview": df.head().to_dict()})

if __name__ == "__main__":
    app.run(debug=True)
