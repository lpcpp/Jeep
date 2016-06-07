def connect_db():
    from settings import DB_ADDRESS, DB_NAME, DB_PORT
    from mongoengine.connection import connect

    connect(DB_NAME, host=DB_ADDRESS, port=DB_PORT)
