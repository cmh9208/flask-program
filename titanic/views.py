from titanic.models import Titanicmodel
from util.dataset import Dataset

class TitanicController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = Titanicmodel()

    def preprocess(self, train, test) -> object: # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정
        # this = model.pclass_ordinal(this) 데이터자체가 이미 ordinal
        this = model.sex_nominal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this)
        return this

    def modeling(self, train, test) -> object: # 모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this) #답안지
        this.train = model.create_train(this)# 답이 제거된 train
        self.preprocess()
        return this

    def learning(self) -> object: # 기계학습
        pass

    def submit(self) -> object: # 배포
        pass
