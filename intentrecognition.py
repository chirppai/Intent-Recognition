from __future__ import unicode_literals, print_function
import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
import glob

class IntentRecognition:
    def __init__(self, name=''):
        self.name = name
    def loadntrain(self, rootpath = './datasets/*.json'):
        paths = sorted(glob.glob(rootpath))
        self.models = []
        for i,dset in enumerate(paths):
            with io.open(dset) as f:
                dataset = json.load(f)
            model = SnipsNLUEngine(config=CONFIG_EN)
            model = model.fit(dataset)
            self.models.append(model)
            print(f"{i+1}. Trained for {dset}")
        print(f"Training for {len(paths)} datasets completed")
    def predictall(self, text):
        D = []
        for model in self.models:
            D.append(model.parse(text))
        return D
    def predict(self, text):
        D = self.predictall(text=text)
        f = []
        p = 0
        for i in D:
            if i['intent']['intentName']!=None:# and i['intent']['probability']>0.5:
                if i['intent']['probability']>p:
                    f = i
                    p = i['intent']['probability']
        return f
