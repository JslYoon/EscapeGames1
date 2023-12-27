from sqlalchemy import select, insert
from werkzeug.security import generate_password_hash

from flask import Blueprint, jsonify, request, Response
users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["GET"])
def get_all_users():
    
    return jsonify([{"id": "itsa me", "username": "Mario"}])