from flask import Flask, request
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #warning this disables CORS policy

@app.get("/")
def home(): 
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"adrian Aguinaga"}
    return json.dumps(me)

@app.get("/footer") #Section not page
def footer():
    pageName = {"pageName":"Organika"}
    return json.dumps(pageName)
# please create an API to footer that contains the name of the page(organika)

products = []

def fix_id(obj):
    obj["_id"]= str(obj["_id"])
    return obj

@app.get("/api/products")
def read_products():
    cursor = db.catalog.find({})
    catalog = []
    for prod in cursor:
        catalog.append(fix_id(prod))

    return json.dumps(catalog)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    #products.append(item
    db.catalog.insert_one(item)
    return json.dumps(fix_id (item))

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0<=index<len(products):
         products[index]=update_item
         return json.dumps(update_item)
    else:
        return "That index does not exist"










##################################
############  COUPONS ############
##################################

# get /api/coupons -> read all
@app.get("/api/coupoons")
def get_coupons():
    cursor = db.coupons.find({})
    coupons = []
    for cp in cursor:
        coupons.append(fix_id(cp))

    return json.dumps(coupons)


# post /api/coupons -> save a coupon
@app.post("/api/coupons")
def save_coupon():
    item = request.get_json()
    #products.append(item
    db.coupons.insert_one(item)
    return json.dumps(fix_id (item))


# coupon struct:
# code - str
# discount - number



"""
{
    "code": "qwerty",
    "discount": 12
}
"""




app.run(debug=True)