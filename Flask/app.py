from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

md = pickle.load(open(r"D:\internship\LandPrice_app\Flask\price.pkl","rb"))
sc = pickle.load(open(r"D:\internship\LandPrice_app\Flask\scale.pkl","rb"))


@app.route('/')
def hello_world():
    return render_template("value.html")

@app.route('/home')
def home():
         return render_template('value.html')
     
@app.route('/value',methods = ["POST"])
def value():
    p = request.form["a"]
    q = request.form["b"]
    r = request.form["c"]
    s = request.form["d"]
    t = request.form["e"]
    u = request.form["f"]
    data = [[p,q,r,s,t,u]]
    dt=(sc.fit_transform(data))
    prd=md.predict(dt)
    return render_template("value.html",y=prd)
app.run(debug = False)