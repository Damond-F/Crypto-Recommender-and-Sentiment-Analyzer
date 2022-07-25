from PyQt5 import QtCore, QtGui, QtWidgets
from scripts.newsScraper import googleNews
from scripts.ambcrypto import ambcrypto

scraper = googleNews('aave coin', 'aave')
