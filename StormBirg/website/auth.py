# Step 4 to store routes and pages for the website
from flask import Blueprint
# Repeatition of the work in views.py but change variable name to auth
#to show that this is a part of the app call it whatever
auth = Blueprint('views', __name__)