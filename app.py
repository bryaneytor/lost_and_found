from flask import Flask, render_template, redirect, url_for, request
from scan import FaceRecognition
from threading import Thread
import os

PEOPLE_FOLDER = os.path.join('imgs')
print(PEOPLE_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


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
      img = os.path.join(app.config['UPLOAD_FOLDER'], 'found0.jpg')
      return render_template('result.html', user_image = img)

if __name__ == "__main__":
    app.run(debug=True)
