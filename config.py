import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    FLASK_DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    if os.environ.get('DATABASE_TYPE').lower() == 'mysql':
        _DATABASE = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD'),
            host=os.environ.get('DATABASE_HOST'),
            port=os.environ.get('DATABASE_PORT'),
            database=os.environ.get('DATABASE_NAME')
            )
    elif os.environ.get('DATABASE_TYPE').lower() == 'sqlite':
        _DATABASE = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_DATABASE_URI = _DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('MAIL_ADDRESS')]

    POSTS_PER_PAGE = 15
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    LANGUAGES = ['en', 'es', 'fr', 'id', 'ru', 'ja']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
