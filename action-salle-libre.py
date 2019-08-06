#!/usr/bin/env python2
# coding: utf-8

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

import datetime
import dateutil.parser
import pytz
import json

import requests


fromtimestamp = datetime.datetime.fromtimestamp

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

HOSTNAME = "localhost"
HERMES_HOST = "{}:1883".format(HOSTNAME)



class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()



with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
