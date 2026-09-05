from flask import Flask, request, render_template       #helps to create a webserver to connect it with frontend 
import pyttsx3
app = Flask(__name__)                   #helps to create  a flask method to run the webserver
@app.route("/")
def home():
    return render_template("index.html")            #helps to say when the user opens the website it will show the index.html file
@app.route("/speak", methods=["POST"])          #helps to say when the user clicks the button it will run the speak function
def speak():
    engine = pyttsx3.init()      #helps to create a pyttsx3 method to run the text to speech engine           
    text = request.form["text"]            #helps to say when the user clicks the button it will get the text from the input field
    engine.say(text)                    #helps to say the text that the user entered
    engine.runAndWait()  
    engine.stop()              #helps to say the text that the user entered
    return"", 204            #helps to say when the user clicks the button it will show the reading completed message
app.run(debug=True)                         #helps to say when the user runs the code it will run the webserver