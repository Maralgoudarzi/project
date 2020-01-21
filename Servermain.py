import numpy as np
from flask import Flask, render_template, flash, request, url_for
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from werkzeug.utils import redirect
# from Model-classification import predict
from Convertor import *
import plot as plt
# import dataset.Convertor
import pickle
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
    gender=[ 'Male', 'Female']
    Nationality = ['KW', ' USA', 'Jordan', 'Iran', 'lebanon', 'SaudiArabia', 'Egypt',
                  ' Tunis', ' Morocco', 'Syria', ' Lybia', 'Palestine', 'Iraq']
    PlaceofBirth = ['KuwaIT', 'USA', 'Jordan', 'Iran', 'lebanon', 'SaudiArabia', 'Egypt',
                   'Tunis', 'Morocco', 'Syria', 'Lybia', 'Palestine', 'Iraq']
    StageID = ['lowerlevel', ' MiddleSchool', 'HighSchool']
    GradeID = ['G-01','G-02','G-03','G-04','G-05','G-06','G-07','G-08','G-09','G-10','G-11','G-12']
    SectionID = ['A','B','C']
    Topic = ['IT', 'Math', 'Arabic', 'Science', 'English', 'Quran', 'Spanish', 'French', 'Arabic',
            'History', 'Biology', 'Geology', 'Chemistry']
    Semester = ['S', 'F']
    Relation =['Father', 'Mum']
    ParentAnsweringSurvey = ['Yes', 'No']
    ParentschoolSatisfaction=['Yes', 'No']
    StudentAbsenceDays = ['Under-7', 'Above-7']



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

        error='select all field.'
    # else :
    #
    #     studentInfo[0]=convertor(request.form['gender'])
    #     studentInfo[1]=convertor(request.form['Nationality'])
    #     studentInfo[2]=convertor(request.form['PlaceofBirth'])
    #     studentInfo[3]=convertor(request.form['StageID'])
    #     studentInfo[4]=convertor(request.form['SectionID'])
    #     studentInfo[5]=convertor(request.form['Topic'])
    #     studentInfo[6]=convertor(request.form['Semester'])
    #     studentInfo[7]=convertor(request.form['ParentAnsweringSurvey'])
    #     studentInfo[8]=convertor(request.form['ParentschoolSatisfaction'])
    #     studentInfo[9]=convertor(request.form['StudentAbsenceDays'])
    #     studentInfo[10]=convertor(request.form['VisITedResources'])
    #     studentInfo[11]=convertor(request.form['AnnouncementsView'])
    #     studentInfo[12]=convertor(request.form['raisedhands'])
    #     studentInfo[13]=convertor(request.form['Discussion'])
    #     studentInfo[14]=convertor(request.form['health'])
    #     studentInfo[15]=convertor(request.form['absences'])
    #



       # return redirect (url_for ('Prediction'))

    elif request.method == 'GET':

        return render_template('Students.html', error=error,gender=gender,NationalITy =Nationality,PlaceofBirth=PlaceofBirth, StageID=StageID,
                               GradeID=GradeID,SectionID=SectionID,Topic=Topic,Semester=Semester,Relation=Relation,
                                ParentAnsweringSurvey=ParentAnsweringSurvey,ParentschoolSatisfaction=ParentschoolSatisfaction,StudentAbsenceDays=StudentAbsenceDays)

# @app.route('/Prediction')
# def prediction(student_info):
#     fi=open("knn.pkl", 'rb')
#     model=pickle.load(fi)
#
#     student_info=np.array(student_info).reshape(1, -1)
#     res=model.predict(student_info)
#
#      return render_template('Prediction.html')

if __name__ == "__main__":
   app.run()