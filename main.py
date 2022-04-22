from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json
import time
from config import *
from tkinter import *
import os
import sys
import UserDetails

user = setInfo()
user.printDetails()