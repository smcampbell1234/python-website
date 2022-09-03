# flask contains all the protypes to create a website using python, such as handling requests
# import Flask class from flask library
# enter_template (from flask) accesses HTML file, stores it it python files, and displays that HTML over the request URL
# html has to be stored in folder titled 'templates'
from flask import Flask, render_template

# instantiate Flask class to create flask object named app
# __name__ variabe gets the name of the python script
app = Flask(__name__)

# decorator -- function home() will be mapped to route


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


# if script is directly executed, this app will run, if script is imported, it won't run
if __name__ == "__main__":
    app.run(debug=True)


"""
Case 1: - Script Executed
When you execute the script the name is main.
__name__ = "__main__"

Case 2: - Script Imported
When the Script is imported it's name is the file name
__name__ = "script1
"""
