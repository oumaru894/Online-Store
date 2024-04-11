import os
import os.path

basdir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    #os.environ.get("SQLALCHEMY QUERY") or 
    DEBUG = False
    SECRET_KEY="g\xc5\x12\xb7\\\x91v\xec]\x9e4\xb2\\\x90\x14\x00\xd0T\x8b\x1c\x88]}\x12"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basdir, "items.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXTENTIONS = True