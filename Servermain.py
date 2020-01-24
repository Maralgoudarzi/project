import numpy as np
from flask import Flask, render_template, flash, request, url_for
from werkzeug.utils import redirect
import pickle
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from visualization import get_visualization
from flask import current_app


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)


studentInfo = ["gender","NationalITy","PlaceofBirth","StageID","GradeID","SectionID","Topic","Semester",
               "Relation","raisedhands","VisITedResources","AnnouncementsView","Discussion","ParentAnsweringSurvey","ParentschoolSatisfaction","StudentAbsenceDays"]

# Route for handling the login page logic
@app.route('/')
def main():
    return render_template('index.html')




@app.route('/students', methods=['GET', 'POST'])
def dataForm():
    error = None
    gender_data = [{'name':'Female','value':0},{'name':'Male','value':1}]

    Nationality_data = [{'name':'Iran','value':1},{'name':'SaudiArabia','value':2},{'name':'USA','value':3},{'name':'Egypt','value':4},{'name':'Lybia','value':5},{'name':'lebanon','value':6},{'name':'Morocco','value':7},
                   {'name': 'Jordan', 'value': 8},{'name': 'Palestine', 'value': 9} ,{'name': 'Syria', 'value': 10},{'name': 'Tunis', 'value': 11},{'name': 'KW', 'value': 12},{'name': 'venzuela', 'value': 13},{'name': 'Iraq', 'value': 14}]

    PlaceofBirth_data = [{'name':'Iran','value':1},{'name':'SaudiArabia','value':2},{'name':'USA','value':3},{'name':'Egypt','value':4},{'name':'Lybia','value':5},{'name':'lebanon','value':6},{'name':'Morocco','value':7},
                   {'name': 'Jordan', 'value': 8},{'name': 'Palestine', 'value': 9} ,{'name': 'Syria', 'value': 10},{'name': 'Tunis', 'value': 11},{'name': 'KW', 'value': 12},{'name': 'Iraq','value': 13},{'name':'venzuela','value': 14}]

    StageID_data = [{'name':'lowerlevel','value':1},{'name':'MiddleSchool','value':2},{'name':'HighSchool','value':3}]

    GradeID_data = [{'name':'G-01','value':2},{'name':'G-04','value':4},{'name':'G-05','value':5},{'name':'G-06','value':6},{'name':'G-07','value':7},{'name':'G-08','value':8},{'name':'G-09','value':9},{'name':'G-10','value':10},{'name':'G-11','value':11},{'name':'G-12','value':12}]
    SectionID_data = [{'name':'A','value':1},{'name':'B','value':2},{'name':'C','value':3}]
    Topic_data = [{'name':'Biology','value':1},{'name':'Geology','value':2},{'name':'Quran','value':3},{'name':'Science','value':4},{'name':'Spanish','value':5},{'name':'IT','value':6},{'name':'French','value':7},
             {'name':'English','value':8},{'name':'Arabic','value':9},{'name':'Chemistry','value':10},{'name':'Math','value':11},{'name':'History','value':12}]
    Semester_data = [{'name':'S','value':0},{'name':'F','value':1}]
    Relation_data =[{'name':'Father','value':1},{'name':'Mum','value':2}]
    ParentAnsweringSurvey_data = [{'name':'Yes','value':1},{'name':'No','value':0}]
    ParentschoolSatisfaction_data=[{'name':'Yes','value':1},{'name':'No','value':0}]
    StudentAbsenceDays_data = [{'name':'Under-7','value':0},{'name':'Above-7','value':1}]



    if request.method == 'POST':

        gender = request.form['gender']
        NationalITy = request.form['NationalITy']
        PlaceofBirth = request.form['PlaceofBirth']
        StageID = request.form['StageID']
        GradeID = request.form['GradeID']
        SectionID = request.form['SectionID']
        Semester = request.form['Semester']
        Topic=request.form['Topic']
        Relation = request.form['Relation']
        ParentAnsweringSurvey = request.form['ParentAnsweringSurvey']
        ParentschoolSatisfaction = request.form['ParentschoolSatisfaction']
        StudentAbsenceDays = request.form['StudentAbsenceDays']
        VisITedResources=request.form['VisITedResources']
        AnnouncementsView=request.form['AnnouncementsView']
        raisedhands=request.form['raisedhands']
        Discussion=request.form['Discussion']

        # ToDo: check for input Errors and show to user


        error = None

        if VisITedResources == '' or int(VisITedResources) > 100 \
                or AnnouncementsView == '' or int(AnnouncementsView) > 100\
                or raisedhands == '' or int(raisedhands) > 100\
                or Discussion == '' or int(Discussion) > 100:

            error='kesafat select all field.'
            return render_template('Students.html', error=error, gender=gender_data, NationalITy=Nationality_data,
                                   PlaceofBirth=PlaceofBirth_data, StageID=StageID_data,
                                   GradeID=GradeID_data, SectionID=SectionID_data, Topic=Topic_data, Semester=Semester_data,
                                   Relation=Relation_data,
                                   ParentAnsweringSurvey=ParentAnsweringSurvey_data,
                                   ParentschoolSatisfaction=ParentschoolSatisfaction_data,
                                   StudentAbsenceDays=StudentAbsenceDays_data)

        test_data=[gender, NationalITy, PlaceofBirth, StageID, GradeID, SectionID, Topic, Semester, Relation,
                   raisedhands, VisITedResources, AnnouncementsView, Discussion, ParentAnsweringSurvey,
                   ParentschoolSatisfaction, StudentAbsenceDays]

        print(test_data)
        user_score = predict(test_data)

        print("Score:",user_score)

        vis_data =get_visualization()

        return render_template('result.html',score=user_score,vis_data=vis_data)


    else :

        return render_template('Students.html', error=error, gender=gender_data, NationalITy=Nationality_data,
                               PlaceofBirth=PlaceofBirth_data, StageID=StageID_data,
                               GradeID=GradeID_data, SectionID=SectionID_data, Topic=Topic_data, Semester=Semester_data,
                               Relation=Relation_data,
                               ParentAnsweringSurvey=ParentAnsweringSurvey_data,
                               ParentschoolSatisfaction=ParentschoolSatisfaction_data,
                               StudentAbsenceDays=StudentAbsenceDays_data)



def predict(student_info):
    #load the sklearn model from pickle file
    fi = current_app.open_resource("knn.pkl", 'rb')
    model = pickle.load(fi)

    student_info = np.array(student_info).reshape(1, -1)


    res = model.predict(student_info)
    Class = res[0]

    print("The predicted grade is:‌",Class)
    return Class



if __name__ == "__main__":
   app.run()