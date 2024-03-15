from flask import Flask, render_template, request, json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route ('/',  methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form["Job Title"])
        print(request.form["Seniority Level"])
        print(request.form["Location"])
        print(request.form["Industry"])
        print(request.form["Tech Tools"])

        Job_title = request.form["Job Title"]
        Location = request.form["Location"]
        Seniority_Level = request.form["Seniority Level"]
        Industry = request.form["Industry"]
        Tech_Tools = request.form["Tech Tools"]


        Excel = request.form.get('Excel', '0')
        print(Excel)

        Sql = request.form.get('Sql', '0')
        print(Sql)

        Tableau = request.form.get('Tableau', '0')
        print(Tableau)

        PowerBI = request.form.get('PowerBI', '0')
        print(PowerBI)

        Python = request.form.get('Python', '0')
        print(Python)

        average_uk_annual_salary = []
        if ((Job_title == 'Data Analyst') | (Job_title == 'Data Engineer')) & (Location == 'Outside Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(33000)
        elif ((Job_title == 'Data Analyst') | (Job_title == 'Data Engineer')) & (Location == 'Outside Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(54000)
        elif ((Job_title == 'Data Analyst') | (Job_title == 'Data Engineer')) & (Location == 'Outside Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(82000)
        elif ((Job_title == 'Data Analyst') | (Job_title == 'Data Engineer')) & (Location == 'In Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif ((Job_title == 'Data Analyst') | (Job_title == 'Data Engineer')) & (Location == 'In Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(61000)
        elif ((Job_title == 'Data Analyst') | (Job_title == 'Data Engineer')) & (Location == 'In Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(90000)
        elif (Job_title == 'Insights Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(35000)
        elif (Job_title == 'Insights Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(59000)
        elif (Job_title == 'Insights Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(79000)
        elif (Job_title == 'Insights Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif (Job_title == 'Insights Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(60000)
        elif (Job_title == 'Insights Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(84000)
        elif (Job_title == 'Business Intelligence Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif (Job_title == 'Business Intelligence Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(50000)
        elif (Job_title == 'Business Intelligence Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(72000)
        elif (Job_title == 'Business Intelligence Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif (Job_title == 'Business Intelligence Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(57000)
        elif (Job_title == 'Business Intelligence Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(74000)
        elif (Job_title == 'Business Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(34986.206132)
        elif (Job_title == 'Business Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(43347.407031)
        elif (Job_title == 'Business Analyst') & (Location == 'Outside Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(51290.702062)
        elif (Job_title == 'Business Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Entry level'):
            average_uk_annual_salary.append(37696.019439)
        elif (Job_title == 'Business Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Associate'):
            average_uk_annual_salary.append(46854.961651)
        elif (Job_title == 'Business Analyst') & (Location == 'In Greater London') & (Seniority_Level == 'Mid-Senior level'):
            average_uk_annual_salary.append(52322.974685)

        average_uk_annual_salary = float(average_uk_annual_salary[0])
        print(average_uk_annual_salary)

        features = [average_uk_annual_salary, Python, Excel, PowerBI, Sql, Tableau, Seniority_Level, Industry, Location, Tech_Tools, Job_title]
        print(features)

        features_array = [np.array(features)]
        print(features_array)

        prediction = model.predict(features_array)
        print(prediction)


    return render_template('index.html')


# @app.route ("/predict", method=["GET", "POST"])
# def predict():
#     return json.dumps({'job_title': request.forms['job_title']})




if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)


