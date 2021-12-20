from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)


def addToDataFrame(Question, paraPharase, Answer, df):
    df = df.append({'question' : Question, 'variations' : paraPharase, 'answer' : Answer}, 
                ignore_index = True)
    return df


@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/postskill",methods=["POST","GET"])
def postskill():
    if request.method == 'POST':
        df = pd.read_csv('test.csv')
        print("------------------------------")
        print(df)
        print("------------------------------")
        skills = request.form.getlist('skill[]')
        Question = request.form['Question']
        Answer = request.form['Answer']
        print(df)
        print(Question)
        print(Answer)
        print(skills)
        if len(skills) > 0 and skills[0] !='':
            for value in skills:
                df = addToDataFrame(Question=Question, paraPharase=value, Answer=Answer, df=df)
                print(df)
        df.to_csv('./utils/data.csv')
        print("------------------------------")
        print("data.csv")

        print("------------------------------")
        
        msg = 'New record created successfully'
        import subprocess
        rc, output = subprocess.getstatusoutput("python utils/semi_automation_insertion2.py")
        print("-------------")
        # print(output)
        if rc==0:
            print("------------------------------")
            rc, output = subprocess.getstatusoutput("python utils/merge_data_files.py")
            print("Merging of files")
            print("------------------------------")
            subprocess.getstatusoutput("rasa train")
            print("rasa training completed...................")
            print("------------------------------")
            subprocess.getoutput("sudo docker image rm -f edubot")
            print("Docker old image removed...................")
            print("------------------------------")
            subprocess.getoutput("sudo docker build -t edubot .")
            print("Docker new image Built...................")
            print("------------------------------")
        try:
            df = pd.read_csv('./utils/data.csv')
            df.drop(df.columns, axis=1, inplace=True)
            df.to_csv('./utils/data.csv', index=False)
        except:
            pass
        try:
            print("-----------------------------------------------------------------------------------")
            print("intermediate.csv file removed")
            subprocess.getoutput("rm ./utils/intermediate.csv")
            print("-----------------------------------------------------------------------------------")
        except:
            pass
        try:
            df_test = pd.read_csv('test.csv')
            df_test.drop(df.index[:],0, inplace=True)
            df_test.to_csv('test.csv', index=False)
        except:
            pass
        
    return jsonify(msg)


@app.route("/add_row",methods=["POST"])
def add_row():
    if request.method == 'POST':
        df = pd.read_csv("test.csv")
        print("Row---------------------------")
        print(df)
        skills = request.form.getlist('skill[]')
        Question = request.form['Question']
        Answer = request.form['Answer']
        for value in skills:
            df = addToDataFrame(Question=Question, paraPharase=value, Answer=Answer, df=df)
        df.to_csv('test.csv', index=False)
        msg = 'New Row added successfully'
    return jsonify(msg)

if __name__ == "__main__":
    app.run(debug=True)