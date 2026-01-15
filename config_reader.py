
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

AGE_MIN = config.getint('Players_Config', 'AGE_MIN', fallback=16)
AGE_MAX = config.getint('Players_Config', 'AGE_MAX', fallback=40)
BASE_RATING = config.getint('Players_Config', 'BASE_RATING', fallback=40)