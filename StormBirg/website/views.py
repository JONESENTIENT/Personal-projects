# Step 3 to store routes and pages for the website
from flask import Blueprint

#to show that this is a part of the app call it whatever
views = Blueprint('views', __name__)

# we define our first view/blueprint
# here we specify the route for homepage
@views.route('/')
def home(): #This runs whenever the homepage opens
    return '<h1>Test</h1>' #This is what will appear

ended at 20:00