import os
from pymongo import MongoClient

MONGO_URL = os.environ.get('MONGO_URL')
_connection = MongoClient(MONGO_URL)

db = _connection["sportsync"]
cachedb = _connection["sportsync_cache"]
tzdb = _connection["sportsync_tz"]
