import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://QuangAnh:Bunny4606@demo-project-qeped.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# db.foods.save({'name': 'com ga', 'price': 30})

# print(list(db.foods.find({'name':'com ga'})))
# print(db.foods.update_one({'name':'com ga'}, {'$set':{'price':70}}))

def add_food(name:str,price:int):
    """Them mot mon an
    
    Arguments:
        name {[type]} -- Ten mon an
        price {[type]} -- Gia tien
    """
    db.foods.insert_one({'name':'com bo','price':50})