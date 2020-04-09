from flask import Flask, render_template, redirect, url_for, request
from scan import FaceRecognition


app = Flask(__name__, static_url_path='/static')

@app.route("/", methods = ["GET", "POST"])
def main():
      if request.method == "POST":
         if request.files:
            img = request.files["foto"]
            name = request.form["nombre"]
            print (img, str(name))
            FaceRecognition.scan(img,str(name))

         return redirect(url_for('result'))
      return render_template("homepage.html")

@app.route('/home', methods=["GET", "POST"])
def home():
      return main()

@app.route('/result')
def result():
      return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
