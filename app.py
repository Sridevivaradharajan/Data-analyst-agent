from flask import Flask, request, jsonify
from services.data_cleaner import clean_data
from services.analytics import analyze_data
from services.sentiment import sentiment_analysis
from services.report import generate_report
from utils.file_utils import load_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
    <h1>Agent AI Analytics Engine</h1>
    <p>Status: Running</p>
    <ul>
        <li>POST /process – Data Cleaning</li>
        <li>POST /analyze – Statistical Analysis</li>
        <li>POST /sentiment – Sentiment Analysis</li>
        <li>POST /report – Generate Report</li>
    </ul>
    """

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/process", methods=["POST"])
def process_data():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    df = load_file(file)
    result = clean_data(df)
    return jsonify(result)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    df = load_file(file)
    result = analyze_data(df)
    return jsonify(result)

@app.route("/sentiment", methods=["POST"])
def sentiment():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_analysis(text)
    return jsonify(result)

@app.route("/report", methods=["POST"])
def report():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    df = load_file(file)
    output = generate_report(df)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
