from flask import Blueprint, request, jsonify
from utils.currency import get_price_in_currency

pricing_bp = Blueprint("pricing", __name__)

@pricing_bp.route("/pricing", methods=["GET"])
def pricing():
    country = request.args.get("country", "US")
    base_price = 10  
    result = get_price_in_currency(base_price, country)
    return jsonify(result)
