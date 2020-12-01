import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser@clusterarasan.roinm.mongodb.net/metlife-dugout?retryWrites=true&w=majority")
db = client.test


# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         "CLIENT": {
#            "name": 'metlife-dugout',
#            "host": 'mongodb+srv://dbuser:dbuser@clusterarasan.roinm.mongodb.net/metlife-dugout?retryWrites=true&w=majority',
#            "username": 'dbuser',
#            "password": 'dbuser',
#            "authMechanism": "SCRAM-SHA-1",
#         }, 
#     }
# }

# source python_modules/bin/activate
# django-admin startproject djangoapi
# cd djangoapi
# python manage.py makemigrations
# python manage.py showmigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py startapp src
# python manage.py sqlmigrate src 0001
