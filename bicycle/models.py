from util.dataset import Dataset
import pandas as pd

class Bicyclemodel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        pass

    def preprocese(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def create_train(self):
        pass

    def create_label(self):
        pass