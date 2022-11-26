from flask import Flask, request
import os.path
import os

app = Flask("my-fist-flask-app")


@app.route("/todos", methods=["GET"])
def todos():
    file_path = "./results/todos.txt"
    if os.path.isfile(file_path):
        with open(file_path) as f:
            return f.read()
    else:
        return "TODO list does not exist yet"


@app.route("/todo", methods=["POST"])
def todo():
    file_path = "./results"
    file_name = "todos.txt"
    if os.path.isfile(file_path) == False:
        os.makedirs(file_path, exist_ok=True)
    # print(os.listdir("."))
    d = request.data.decode()
    with open(file_path + "/" + file_name, mode="a") as f:
        f.write(d + "/n")


if __name__ == "__main__":
    app.run(debug=True)
