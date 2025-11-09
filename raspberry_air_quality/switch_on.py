#!/usr/bin/python
from phue import Bridge
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig()
b = os.getenv("BRIDGE")

# TÄTÄ EI ENÄÄ TARVITSE TEHDÄ
#################
# Uncomment this line to register the app (see below)
#b.connect()
#################

# Change the light state to on
b.set_light(os.getenv("IV_KONE"), 'on', True)
