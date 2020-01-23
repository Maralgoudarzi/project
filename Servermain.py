import numpy as np
from flask import Flask, render_template, flash, request, url_for
from werkzeug.utils import redirect
import pickle
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)


studentInfo = ["gender","NationalITy","PlaceofBirth","StageID","GradeID","SectionID","Topic","Semester",
               "Relation","","raisedhands","VisITedResources","AnnouncementsView","Discussion","ParentAnsweringSurvey","ParentschoolSatisfaction","StudentAbsenceDays"]

# Route for handling the login page logic
@app.route('/')
def main():
    return render_template('index.html')




@app.route('/students', methods=['GET', 'POST'])
def dataForm():
    error = None
    gender = [{'name':'Female','value':0},{'name':'Male','value':1}]

    Nationality = [{'name':'Iran','value':1},{'name':'SaudiArabia','value':2},{'name':'USA','value':3},{'name':'Egypt','value':4},{'name':'Lybia','value':5},{'name':'lebanon','value':6},{'name':'Morocco','value':7},
                   {'name': 'Jordan', 'value': 8},{'name': 'Palestine', 'value': 9} ,{'name': 'Syria', 'value': 10},{'name': 'Tunis', 'value': 11},{'name': 'KW', 'value': 12},{'name': 'Iraq', 'value': 13},{'name': 'Iraq', 'value': 14}]

    PlaceofBirth = [{'name':'Iran','value':1},{'name':'SaudiArabia','value':2},{'name':'USA','value':3},{'name':'Egypt','value':4},{'name':'Lybia','value':5},{'name':'lebanon','value':6},{'name':'Morocco','value':7},
                   {'name': 'Jordan', 'value': 8},{'name': 'Palestine', 'value': 9} ,{'name': 'Syria', 'value': 10},{'name': 'Tunis', 'value': 11},{'name': 'KW', 'value': 12},{'name': 'Iraq', 'value': 13},{'name': 'Iraq', 'value': 14}]

    StageID = [{'name':'lowerlevel','value':1},{'name':'MiddleSchool','value':2},{'name':'HighSchool','value':3}]

    GradeID = [{'name':'G-01','value':2},{'name':'G-04','value':4},{'name':'G-05','value':5},{'name':'G-06','value':6},{'name':'G-07','value':7},{'name':'G-08','value':8},{'name':'G-09','value':9},{'name':'G-10','value':10},{'name':'G-11','value':11},{'name':'G-12','value':12}]
    SectionID = [{'name':'A','value':1},{'name':'B','value':2},{'name':'C','value':3}]
    Topic = [{'name':'Biology','value':1},{'name':'Geology','value':2},{'name':'Quran','value':3},{'name':'Science','value':4},{'name':'Spanish','value':5},{'name':'IT','value':6},{'name':'French','value':7},
             {'name':'English','value':8},{'name':'Arabic','value':9},{'name':'Chemistry','value':10},{'name':'Math','value':11},{'name':'History','value':12}]
    Semester = [{'name':'S','value':1},{'name':'F','value':1}]
    Relation =[{'name':'Father','value':1},{'name':'Mum','value':2}]
    ParentAnsweringSurvey = [{'name':'Yes','value':1},{'name':'No','value':0}]
    ParentschoolSatisfaction=[{'name':'Yes','value':1},{'name':'No','value':0}]
    StudentAbsenceDays = [{'name':'Under-7','value':0},{'name':'Above-7','value':1}]



    if request.method == 'POST':

        gender = request.form['gender']
        NationalITy = request.form['NationalITy']
        PlaceofBirth = request.form['PlaceofBirth']
        StageID = request.form['StageID']
        GradeID = request.form['GradeID']
        SectionID = request.form['SectionID']
        Topic = request.form['Topic']
        Relation = request.form['Relation']
        ParentAnsweringSurvey = request.form['ParentAnsweringSurvey']
        ParentschoolSatisfaction = request.form['ParentschoolSatisfaction']
        StudentAbsenceDays = request.form['StudentAbsenceDays']
        VisITedResources=request.form['VisITedResources']
        AnnouncementsView=request.form['AnnouncementsView']
        raisedhands=request.form['raisedhands']
        Discussion=request.form['Discussion']


        test_data = [gender,NationalITy,PlaceofBirth,StageID,GradeID,SectionID,Topic,Semester,Relation,raisedhands,VisITedResources,AnnouncementsView,Discussion,ParentAnsweringSurvey,ParentschoolSatisfaction,StudentAbsenceDays]

        user_score = predict(test_data)
        print("Score:",user_score)


        error='select all field.'
    else :

        return render_template('Students.html', error=error,gender=gender,NationalITy =Nationality,PlaceofBirth=PlaceofBirth, StageID=StageID,
                               GradeID=GradeID,SectionID=SectionID,Topic=Topic,Semester=Semester,Relation=Relation,
                                ParentAnsweringSurvey=ParentAnsweringSurvey,ParentschoolSatisfaction=ParentschoolSatisfaction,StudentAbsenceDays=StudentAbsenceDays)


# @app.route('/show_result', methods=['POST'])
# def show_result():
#
#     user_score = request.form['user_score']
#     return render_template('show_result.html',user_score=user_score)


def predict(student_info):
    #load the sklearn model from pickle file
    fi = open("knn.pkl", 'rb')
    model = pickle.load(fi)

    student_info = np.array(student_info).reshape(1, -1)


    res = model.predict(student_info)
    Class = res[0]

    print("The predicted grade is:‌",Class)
    return Class



if __name__ == "__main__":
   app.run()