import pandas as pd

STROKE_MENUS = ["종료", #0
                "데이터구하기",#1
                "한글메타데이터",#2
                "타깃변수설정",#3
                "데이터처리",#4
                "시각화",#5
                "모델링",#6
                "학습",#7
                "예측"]#8

stroke_meta = {
    'id':'아이디',
    'gender':'성별',
    'age':'나이',
    'hypertension':'고혈압',
    'heart_disease':'심장병',
    'ever_married':'기혼여부',
    'work_type':'직종',
    'Residence_type':'거주형태',
    'avg_glucose_level':'평균혈당',
    'bmi':'체질량지수',
    'smoking_status':'흡연여부',
    'stroke':'뇌졸중'
}

stroke_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.visualize(),
    "4" : lambda t: t.compare_displ(),
    "5" : lambda t: t.find_high_cty(),
    "6" : lambda t: t.find_highest_hwy(),
    "7" : lambda t: t.which_cty_in_suv_compact(),
    "8" : lambda t: t.find_top5_hwy_in_audi(),
    "9" : lambda t: t.find_top3_avg(),
}

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''

class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
        self.my_stroke = None
    '''
    1.스펙보기
    '''
    def spec(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))
    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        print(" --- 2.Features ---")
        print(self.my_stroke.columns)
    '''
    3.타깃변수(=종속변수 dependent, y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: stroke (=뇌졸중)
    타깃 변수값: 과거에 한 번이랃 뇌졸중이 발생했으면 1, 아니면 0
    '''
    def target(self):
        print(self.my_stroke['뇌졸중'].dtype)
        print(self.my_stroke['뇌졸중'].isnull().sum())
        print(self.my_stroke['뇌졸중'].value_counts(dropna=False, normalize=True))
    '''
    4.데이터처리
    '''
    def data_processing(self):
        my = self.my_stroke
        cols = ['나이','기혼여부','체질량지수']
        print(my[cols].dtypes)
        pd.options.display.float_format = '{:.2f}'.format
        print(my[cols].describe())
        print(my['나이'] > 18)
        c =my['나이'] > 18
        print(my[c].head(3))
        print(len(my[c]))
        print(len(my[c]) / len(my[c]))
        my1 = my[c]
        print(my1.shape)
        cols1 = ['성별','고혈압','심장병',
                 '기혼여부','직종','거주형태','흡연여부']
        print(my1[cols1].isnull().sum())
        print(my1[cols1].dtypes)
        # 결측값 50%초과인 변수제거
        print(my1.isna().any()[lambda x:x])
        print(my1['체질량지수'].isnull().mean())
        cols = ['나이','평균혈당','체질량지수']
        print(my1[cols].describe())
        print(my1[cols].skew())
        print(my1[cols].kurtosis()) #80
        c1 = my1['평균혈당'] <= 232.64
        c2 = my1['체질량지수'] <=60.3
        my2 = my1[c1 & c2]
        my2.to_csv('./data/stroke.csv',index=False)
        print(my2.shape)

'''
'id':'아이디',
'gender':'성별',
'age':'나이',----------구간
'hypertension':'고혈압',
'heart_disease':'심장병',
'ever_married':'기혼여부',
'work_type':'직종',
'Residence_type':'거주형태',
'avg_glucose_level':'평균혈당',----------구간
'bmi':'체질량지수',-----------구간
'smoking_status':'흡연여부',
'stroke':'뇌졸중'}
'''