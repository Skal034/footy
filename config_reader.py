
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

AGE_MIN = config.getint('Players_Config', 'AGE_MIN', fallback=16)
AGE_MAX = config.getint('Players_Config', 'AGE_MAX', fallback=40)
MIN_BASE_RATING = config.getint('Players_Config', 'MIN_BASE_RATING', fallback=40)
MAX_BASE_RATING = config.getint('Players_Config', 'MAX_BASE_RATING', fallback=95)
TEAM_STRENGTH_VARIANCE = config.getint('Leagues_Config', 'TEAM_STRENGTH_VARIANCE', fallback=3)
PLAYER_STRENGTH_VARIANCE = config.getint('Leagues_Config', 'PLAYER_STRENGTH_VARIANCE', fallback=8)
NATIONALITY_LAMBDA = config.getfloat('Leagues_Config', 'NATIONALITY_LAMBDA', fallback=0.7)