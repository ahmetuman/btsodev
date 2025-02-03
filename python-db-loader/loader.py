import mysql.connector
import pymongo
import redis

mysql_conn = mysql.connector.connect(
    host="sql-db",
    user="example_user",
    password="example_password",
    database="example_db"
)
cursor = mysql_conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS sample_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
cursor.execute("INSERT INTO sample_table (name) VALUES ('MySQL Verisi')")
mysql_conn.commit()
cursor.close()
mysql_conn.close()

mongo_client = pymongo.MongoClient("mongodb://nosql-db:27017/")
mongo_db = mongo_client["example_db"]
mongo_collection = mongo_db["sample_collection"]
mongo_collection.insert_one({"name": "MongoDB Verisi"})

redis_client = redis.StrictRedis(host='in-memory-db', port=6379, decode_responses=True)
redis_client.set("sample_key", "Redis Verisi")

print("Veritabanlarına eklendi.")
