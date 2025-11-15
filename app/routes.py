from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SearchForm
from app.order_module import DeliveryForm, calculate_distance, calculate_cost


# Home Page
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f"Thank you for your search about: {form.search_term.data}")
        return redirect(url_for("index"))

    return render_template("index.html", title="Home", form=form)


# Search Page
@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f"Thank you for your search about: {form.search_term.data}")
        return redirect(url_for("search"))

    return render_template("search.html", title="Search", form=form)


# Contact Page (no form)
@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

#Calculator for Costs
@app.route('/order', methods=["GET", "POST"], endpoint="order")
def place_order():
    form = DeliveryForm()
    cost = None
    distance = None

    if form.validate_on_submit():
        pickup = form.pickup.data
        dropoff = form.dropoff.data

        distance = calculate_distance(pickup, dropoff)
        if distance is None:
            flash("Could not calculate distance. Please check the addresses.")
        else:
            cost = calculate_cost(distance)
            flash(f"Distance: {distance} km, Estimated delivery cost: R{cost}")
        if distance is None:
            flash("Could not calculate distance. Please check the addresses.")
        else:
            cost = calculate_cost(distance)
            flash(f"Distance: {distance} km, Estimated delivery cost: R{cost}. "
                  "This is an estimate; actual distance, delivery times, and weight may vary.")

    return render_template('order.html', title="Delivery Cost Calculator", form=form, cost=cost, distance=distance)
