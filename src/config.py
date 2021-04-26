import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Activate if use Database
    # SECRET_KEY = os.getenv('SECRET_KEY', 'key_here')
    DEBUG = False
    SERVER_NAME = '0.0.0.0:6996'

class DevConfig(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:6996'
    #SQL SETTING
    #Your SQL URI Here 
    #SQL_DB_URI = 

class TestConfig(Config):
    DEBUG = True
    TESTING = True
    #SQL SETTING
    #Your SQL URI Here 
    #SQL_DB_URI = 

class ProdConfig(Config):
    DEBUG = False
    SERVER_NAME = '0.0.0.0:6996'
    #SQL SETTING
    #Your SQL URI Here 
    #SQL_DB_URI = 

config_name = dict(
    dev = DevConfig,
    test = TestConfig,
    prod = ProdConfig
)

#Activate if USE DB
#key = Config.SECRET_KEY