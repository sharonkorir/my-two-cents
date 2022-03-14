import os

#from instance.config import SECRET_KEY

class Config:
    """
    General configurations parent class
    """
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon:12345678@localhost/my_two_cents'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vytgpulhhgwdsr:31b7c0f84a14a25462ea9723db1250eddeecbf8f2de3c7f4a9f093537e8e308d@ec2-54-235-98-1.compute-1.amazonaws.com:5432/d7fj5oqcf7tu8b'
    
  
    
class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<<user>>:<<Password>>@localhost/<<db_name>>'
    pass
    
class DevConfig(Config):

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<<user>>:<<Password>>@localhost/<<db_name>>'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}