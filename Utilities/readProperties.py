import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        email = config.get('commonInfo', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'password')
        return password