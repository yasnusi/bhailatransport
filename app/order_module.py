# app/order_module.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

COST_PER_KM = 12.83
EXTRA_KM = 14  # Extra buffer to account for real driving distance

class DeliveryForm(FlaskForm):
    pickup = StringField("Pickup Address", validators=[DataRequired()])
    dropoff = StringField("Drop-off Address", validators=[DataRequired()])
    submit = SubmitField("Calculate Cost")

def calculate_distance(pickup_address, dropoff_address):
    """
    Calculate distance in km between two addresses using geopy.
    Adds EXTRA_KM buffer for real-world driving.
    """
    geolocator = Nominatim(user_agent="beatie_delivery_app")
    try:
        pickup_location = geolocator.geocode(pickup_address)
        dropoff_location = geolocator.geocode(dropoff_address)
        if not pickup_location or not dropoff_location:
            return None  # Address not found

        pickup_coords = (pickup_location.latitude, pickup_location.longitude)
        dropoff_coords = (dropoff_location.latitude, dropoff_location.longitude)
        distance_km = geodesic(pickup_coords, dropoff_coords).km

        # Add extra buffer
        total_distance = distance_km + EXTRA_KM
        return round(total_distance, 2)

    except Exception as e:
        print(f"Error calculating distance: {e}")
        return None

def calculate_cost(distance):
    """Calculate cost based on distance."""
    if distance is None:
        return None
    return round(distance * COST_PER_KM, 2)
