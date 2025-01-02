from flask import Flask, render_template, request, redirect

app = Flask(__name__)

subject = "Python"

group_name = "1y_16_11_05_24"

students = [
    {"name": "Sophia f", "gender": "female", "age": 15},
    {"name": "Semen", "gender": "male", "age": 13},
    {"name": "Illya", "gender": "male", "age": 15},
    {"name": "Vlad", "gender": "male", "age": 16},
    {"name": "Vova", "gender": "male", "age": 15},
    {"name": "Rostyslav", "gender": "male", "age": 14},
]


# id list(email password)
users_dict = {}


@app.route("/", methods=["GET"])
def index():
    # for stud in students:
    #     stud["name"] = stud["name"].upper()
    # students.sort(key=lambda element: element["age"])
    context = {
        "title": "GoIteens",
        "subject": subject,
        "group_name": group_name,
        "students": students,
    }
    return render_template("index.html", students=students)

@app.route("/resume")
def get_resume():
    return render_template("./resume.html")

@app.route('/students', methods=['GET', 'POST'])
def students():
    min_grade = request.form.get("min_grade", 0)
    return render_template("students.html", min_grade=min_grade)

@app.route("/users", methods=["GET"])
def get_users():
    return users_dict


@app.route("/signin", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_email = request.form["user-email"]
        user_password = request.form["user-password"]

        print(
            "user_email тут на бекенді отримав з фронтенд: ", user_email, user_password
        )

        users_dict.update({len(users_dict): (user_email, user_password)})

        return redirect("/users")
    return render_template("./login.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("./error.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
