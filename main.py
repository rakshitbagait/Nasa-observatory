from flask import Flask , request,render_template , url_for, request

import os 
import requests
from dotenv import load_dotenv
load_dotenv()
Api_key = os.getenv("API_KEY")

app = Flask(__name__)
@app.route("/")
def home():
    apod_api = f"https://api.nasa.gov/planetary/apod"
    params = {'api_key':Api_key}
    response = requests.get(apod_api,params=params).json()
    show_video =False
    media_type = response["media_type"]
    if media_type == "video":
        show_video = True
    elif media_type== "image":
        show_video = False
    return render_template("index.html", apod = response,media_type=show_video)
@app.route("/search", methods= ["POST","GET"])
def search():
        filtered_items = []
        query = request.args.get('search-box','').strip()
        if query:
            search_url = f"https://images-api.nasa.gov/search?q={query}"
            response = requests.get(search_url).json()
            items = response.get('collection',{}).get('items',[])
           
            for item in items :
                if item.get("links"):
                    filtered_items.append(item)

    # print(filtered_items)        
        else:
            filtered_items =[]

        return render_template("results.html",results=filtered_items)
if __name__ == "__main__":
    app.run(debug=True)