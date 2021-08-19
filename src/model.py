from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import recall_score, f1_score, precision_score,accuracy_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import KFold
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Modeling:
    def __init__(self,tech,df):
        self.tech = tech
        self.df = df
        
        
    
    def split(self,X,y):
        X_train_y,_train,X_test,y_test = train_test_split(self.X,self.y)
        return self.X_train,self.y_train,self.X_test,self.y_test

    def model_sel(self,tech,X,y):
        if self.tech == 'log' :
            self.model = LogisticRegression()
        elif self.tech == 'rfor':
            self.model = RandomForestClassifier()
        elif self.tech == 'gbc':
            self.model = GradientBoostingClassifier()
        elif self.tech == 'kn':
            self.model = KNeighborsClassifier()
        elif self.model = 'svm':
            self.model = SVC()
        return self.model


    def fit_mod(self,model,X_train,y_train):
        return self.model.fit(self.X_train,self.y_train)

    def prediction(self, y_test):
        return self.model.predict(self.y_test)

    