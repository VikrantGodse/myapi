import os
import json
import dj_database_url

SECRET_KEY = '@@pb_j4kf(4(uh$=3kw6l1lusyw%_p+4ba8u$p94!grmug0dtp'f'

DEBUG = False

connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
connection.update({
    'CONN_MAX_AGE': 600,
})
DATABASES = {
    "default": connection,
}

ALLOWED_HOSTS = [os.environ.get("HOST", "*"), ]
