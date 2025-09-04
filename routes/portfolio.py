from flask import Blueprint, request, jsonify
from utils.resume_parser import parse_resume

portfolio_bp = Blueprint("portfolio", __name__)

@portfolio_bp.route("/portfolio", methods=["POST"])
def portfolio_from_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    data = parse_resume(file)
    return jsonify(data)
