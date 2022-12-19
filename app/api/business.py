from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user, login_user, logout_user


businesses_routes = Blueprint('businesses', __name__)


# Get Current User Businesses
@businesses_routes.route('/')
def user_businesses():
    return ""


# Create New Business
@businesses_routes.route('/', methods=["POST"])
def create_business():
    return ""


# Get Business By Id
@businesses_routes.route('/<int:id>', methods=["GET"])
def get_business_by_id():
    return ""


# Edit A Business
@businesses_routes.route('/<int:id>', methods=["PUT"])
def edit_business():
    return ""


# Delete A Business
@businesses_routes.route('/<int:id>', methods=["DELETE"])
def delete_business():
    return ""