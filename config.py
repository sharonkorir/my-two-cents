import os

class Config:
    """
    General configurations parent class
    """
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon:12345678@localhost/my_two_cents'
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://< your heroku url here>'
    pass
    
  
    
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