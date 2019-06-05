import pymongo

client = pymongo.MongoClient(
    "mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.c4e

db.posts.insert_one({
    "title":"Đây là một cái title trống nhé",
    "author":"Awkward Bunny",
    "content":"Make it simple but significant"
})