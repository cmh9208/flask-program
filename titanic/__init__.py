from titanic.template import Plot
from titanic.views import TitanicController
from util.common import Common
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

if __name__ == '__main__':
    api = TitanicController()
    while True:
        menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_sex()
            plot.draw_pclass()
            plot.draw_embarked()
        elif menu == "2":
            print(" ### 모델링 ### ")
            this = api.modeling('train.csv', 'test.csv')
            print(this.train.head())
            print(this.train.columns)
        elif menu == "3":
            rf = RandomForestClassifier()
            dt = DecisionTreeClassifier()
            lr = LogisticRegression()
            svc = SVC()
            print(" ### 머신러닝 ### ")
            api.learning('train.csv', 'test.csv', lr)
            #랜덤포레스트: 83.28 %
            #결정트리: 81.82 %
            #로지스틱회귀: 77.89 %
            #서포터 백터머신 80.7 %
        elif menu == "4":
            print(" ### 배포 ### ")
            df = api.submit('train.csv', 'test.csv')
        else:
            print(" ### 해당 메뉴 없음 ### ")

