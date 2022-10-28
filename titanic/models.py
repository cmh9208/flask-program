import pandas as pd

from util.dataset import Dataset
"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
 === null 값 ===
 Age            177
 Cabin          687
 Embarked         2
"""
# 시각화를 통해 얻은 상관관계 변수들 (varuable = feature = column)는
# pclass, sex, age, fare (기준은 survived)

class Titanicmodel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return  f' Train Type: {type(b)}\n'\
                f' Train columns: {b.columns}\n'\
                f' Train head: {b.head()}\n'\
                f' Train null의 갯수: {b.isnull().sum()}\n'

    def preprocese(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod # s, getter 받을때
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) # dorp 0가로 1세로

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i,axis = 1)
            this.test = this.train.drop(i,axis = 1)
        return this

    @staticmethod
    def sex_nominal(this)-> object: #female, male
        # gender_mapping = {"male" : 0, "female" : 1}
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male" : 0, "female" : 1})
        return this

    @staticmethod
    def age_ordinal(this)-> object: # 연령대 10,20,30
        return this

    @staticmethod
    def fare_ordinal(this)-> object: # 비싼것, 보통, 저렴
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels=[1, 2, 3, 4])
        return this

    @staticmethod
    def embarked_nominal(this)-> object:
        this.train = this.train.fillna({'Embarked':'S'}) # 빈 공간이 있으면 집어넣어라 (널값 처리)
        this.test = this.test.fillna({'Embarked':'S'})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q" : 3}) #어사이먼
        return this

if __name__=="__main__":
    t = Titanicmodel()
    this = Dataset
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = Titanicmodel.embarked_nominal(this)
    print(this.train.head())
    print(this.train.tail())
    print(this.train.columns)
