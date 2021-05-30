#As I said the first line you are importing the (Flask class object) from the flask library.
from flask import Flask, render_template  
import movies_tra

#you are instantiating that class that object.
#This here is a special variable that will get as value the name of the python script.
# __name__="__main__"
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")   #deve existir um folder de nome templates com o arq. index.html 

if __name__ == "__main__":
  app.run(debug=True)
