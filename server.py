from flask import Flask, render_template, request, redirect
import os
import csv


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name= None):
    return render_template(page_name)


@app.route('/submit_post', methods=['POST', 'GET'])
def submeit_post():
    if request.method == "POST":
        try:
            data= request.form.to_dict()
            with open("database.csv","a+",) as database:
                csv_writer = csv.writer(database,quotechar = '"', quoting= csv.QUOTE_MINIMAL)
                csv_writer.writerow([data['email'],data['subject'],data['message']])
            return redirect("thankyou.html")
        except:
            return "did not save to Database"
    else:
        return "something went wrong"


if __name__ == "__main__":
    app.run(debug=True)