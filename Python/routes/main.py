from flask import Blueprint, jsonify, request
from prompts import process

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["POST", "GET"])
def home():
    return jsonify({"message": "API Flask funcionando!"})

@main_bp.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json()
    response = process(data['message'])
    return response

@main_bp.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404
