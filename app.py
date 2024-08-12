from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():


    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    outerdata = (soup.find_all("div", class_ = "widget-listing", limit = 6))
    finalnews = ""
    for data in outerdata:
        news = data.div.div.a["title"]
        finalnews += "\u2022 " + news + "\n"
    
    return render_template("index.html", News = finalnews)
   
if __name__=="__main__":
    app.run(host="0.0.0.0")
