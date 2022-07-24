from flask import Blueprint, render_template

from db.database import db
from db.models import EntityInformation


mod = Blueprint('stats', __name__, url_prefix='/api/stats')


@mod.route("/")
def plot_graph():
    data = db.query(EntityInformation).all()
    labels = [str(item.delivery_time) for item in data]
    values = [item.price_dollar for item in data]
    return render_template('graph.html', labels=labels, values=values)
