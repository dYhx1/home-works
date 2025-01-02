from flask import Flask, render_template, request, redirect

app = Flask(__name__)

subject = "Python"

group_name = "1y_16_11_05_24"

students = [
    {"name": "Sophia", "gender": "female", "age": 15, "average_score": 99},
    {"name": "Semen", "gender": "male", "age": 13, "average_score": 89},
    {"name": "Andrii", "gender": "male", "age": 17, "average_score": 49},
    {"name": "Vlad", "gender": "male", "age": 16, "average_score": 100},
    {"name": "Vova", "gender": "male", "age": 15, "average_score": 86},
    {"name": "Rostyslav", "gender": "male", "age": 14, "average_score": 85},
]

# id list(email password)
users_dict = {}


@app.route("/", methods=["GET"])
def index():
    context = {
        "title": "GoIteens",
        "subject": subject,
        "group_name": group_name,
        "students": students,
    }
    return render_template("./index.html", **context)


@app.route("/resume")
def get_resume():
    return render_template("./resume.html")


@app.route("/users", methods=["GET"])
def get_users():
    return users_dict


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "age": request.form.get("age"),
            "gender": request.form.get("gender"),
            "password": request.form.get("password")
        }
        return render_template("users.html", user=user_data)
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
