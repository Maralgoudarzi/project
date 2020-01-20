import numpy as np
from flask import Flask, render_template, flash, request, url_for
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from werkzeug.utils import redirect
from Model-classification import predictFunction
from Convertor import *
import plot as plt
from dataset.Convertor import convertor

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







        return redirect (url_for ('Prediction'))

    elif request.method == 'GET':

        return render_template('Students.html', error=error,gender=gender,NationalITy =Nationality,PlaceofBirth=PlaceofBirth, StageID=StageID,
                               GradeID=GradeID,SectionID=SectionID,Topic=Topic,Semester=Semester,Relation=Relation,
                                ParentAnsweringSurvey=ParentAnsweringSurvey,ParentschoolSatisfaction=ParentschoolSatisfaction,StudentAbsenceDays=StudentAbsenceDays)

@app.route('/Model-Classification')
def predict():
   df['TotalQ'] = df['Class']
   df['TotalQ'].loc[df.TotalQ == 'Low-Level'] = 0.0
   df['TotalQ'].loc[df.TotalQ == 'Middle-Level'] = 1.0
   df['TotalQ'].loc[df.TotalQ == 'High-Level'] = 2.0

   continuous_subset = df.iloc[:, 9:13]
   continuous_subset['gender'] = np.where(df['gender'] == 'M', 1, 0)
   continuous_subset['Parent'] = np.where(df['Relation'] == 'Father', 1, 0)

   X = np.array(continuous_subset).astype('float64')
   y = np.array(df['TotalQ'])

    X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.3, random_state=0)

    knn: predict = KNeighborsClassifier(n_neighbors=23)
    knn.fit(X_train, y_train)

    return render_template('prediction.html')

if __name__ == "__main__":
   app.run()