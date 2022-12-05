from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "Faisal"


@app.route("/shit")
def shit():
    return "Faisal Alnamlah did this"


if __name__ == "__main__":
    app.run()
# app.run()
# python3 tap bottom right of pycharm IDE then add interpreter then ok
# pycharm -> preferences -> project structure of python interpreter check for flask installed and venv not excluded
# pwd to know which directory you are located in
# ls to list directories located under it
# cd to change the directory
# mkdir to make a new directory
# touch command to create a new file
# rm command to delete a file
# cd .. to navigate tp the parent folder/directory
# rm -rf to delete a directory: be careful because it can delete your whole computer

