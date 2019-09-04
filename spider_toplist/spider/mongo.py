from pymongo import MongoClient
from spider.settings import MONGODB_DATABASES as DATABASES

class Mongo:
    def __init__(self):
        self.__host = DATABASES['host']
        self.__port = DATABASES['port']
        self.__name = DATABASES['database']
        self.__user = DATABASES['username']
        self.__password = DATABASES['password']
        self.__max_pool_size = 10000

    def conn(self):
        print(self.__host, self.__port, self.__password, self.__user, self.__name)
        conn_str = f'mongodb://{self.__user}:{self.__password}@localhost:27017/'
        connection = MongoClient(conn_str, maxPoolSize=self.__max_pool_size, tz_aware=True)
        c = connection[self.__name]
        return c


m = Mongo().conn()

