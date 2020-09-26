from flask import Flask, render_template, jsonify, request
from model import db, connect_to_db, Card

app = Flask(__name__)

@app.route("/")
def show_homepage():
    """Show the application's homepage."""

    return render_template("homepage.html")

@app.route("/cards")
def show_cards():
    """Show all trading cards."""

    return render_template("cards.html")

@app.route("/cards.json")
def get_cards_json():
    """Return a JSON response with all cards in DB."""

    cards = Card.query.all()
    cards_list = []

    for c in cards:
        cards_list.append({"skill": c.skill, "name": c.name, "imgUrl": c.image_url})


    return jsonify({"cards": cards_list})

@app.route("/add-card", methods=["POST"])
def add_card():
    """Add a new card to the DB."""

    name = request.form.get('name')
    skill = request.form.get('skill')

    new_card = Card(name=name, skill=skill)
    db.session.add(new_card)
    db.session.commit()

    return jsonify({"success": True})

@app.route("/cards-jquery")
def show_cards_jquery():
    return render_template("cards-jquery.html")



if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')