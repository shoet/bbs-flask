
class BaseConfig:
    FLASK_ENV = 'development'
    

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'


config = {
    'development': BaseConfig,
    'production': ProductionConfig,
}