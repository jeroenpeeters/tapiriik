from pymongo import MongoClient
from tapiriik.settings import MONGO_DB_MAIN
from tapiriik.settings import MONGO_DB_CACHE
from tapiriik.settings import MONGO_DB_TZ

_connSportSync = MongoClient(MONGO_DB_MAIN)
_connCache = MongoClient(MONGO_DB_CACHE)
_connTz = MongoClient(MONGO_DB_TZ)

db = _connSportSync["sportsync"]
cachedb = _connCache["sportsync_cache"]
tzdb = _connTz["sportsync_tz"]
