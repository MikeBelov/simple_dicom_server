import os
import json


class Config:
    TMP_DIR = os.path.join(os.getcwd(), 'tmp')

    def __init__(self):
        if not os.path.exists(self.TMP_DIR):
            os.mkdir(self.TMP_DIR)

        file = os.path.join(os.path.dirname(__file__), 'conf.json')
        with open(file) as fp:
            data = json.load(fp)

            self.AE_TITLE = data['server']['ae title']
            self.ADDRESS = (data['server']['host'], data['server']['port'])
