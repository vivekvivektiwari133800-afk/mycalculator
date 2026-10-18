from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

foods = [
    {"name": "Pizza", "price": 199},
    {"name": "Burger", "price": 99},
    {"name": "French Fries", "price": 79},
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My Food Shop</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        .food { padding: 15px; margin: 10px; border: 1px solid #ddd; }
        button { padding: 8px 15px; }
    </style>
</head>
<body>
    <h1>🍔 vivek food shop</h1>

    {% for food in foods %}
    <div class="food">
        <h2>{{ food.name }}</h2>
        <p>₹{{ food.price }}</p>
    </div>
    {% endfor %}

    <hr>

    <h2>Admin Panel</h2>

    <form method="POST" action="/add">
        <input name="name" placeholder="Food name" required>
        <input name="price" type="number" placeholder="Price" required>
        <button type="submit">Add Food</button>
    </form>

    <h3>Delete Food</h3>

    {% for food in foods %}
    <form method="POST" action="/delete">
        <input type="hidden" name="name" value="{{ food.name }}">
        <button type="submit">Delete {{ food.name }}</button>
    </form>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, foods=foods)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    price = int(request.form["price"])

    foods.append({
        "name": name,
        "price": price
    })

    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]

    foods[:] = [food for food in foods if food["name"] != name]

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)