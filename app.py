from flask import Flask, render_template, request, json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route ('/')
def index():
    return render_template('homepage.html')

@app.route ("/form")
def form():
    return render_template('predict.html')


@app.route ("/predict", methods=["GET", "POST"])
def predict():
    # print(request.form)
    if request.method == "POST":
        print(request.form["Job Title"])
        print(request.form["Seniority Level"])
        print(request.form["Location"])
        print(request.form["Industry"])
        print(request.form["Tech Tools"])


        job_title_two = request.form["Job Title"]
        in_out_london = request.form["Location"]
        seniority_level = request.form["Seniority Level"]
        industry_category = request.form["Industry"]
        tech_stack_count_group = request.form["Tech Tools"]


        excel = request.form.get('Excel', '0')
        print(excel)

        sql = request.form.get('Sql', '0')
        print(sql)

        tableau = request.form.get('Tableau', '0')
        print(tableau)

        powerbi = request.form.get('PowerBI', '0')
        print(powerbi)

        python = request.form.get('Python', '0')
        print(python)

        average_uk_annual_salary = []
        if ((job_title_two == 'Data Analyst') | (job_title_two == 'Data Engineer')) & (in_out_london == 'Outside Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(33000)
        elif ((job_title_two == 'Data Analyst') | (job_title_two == 'Data Engineer')) & (in_out_london == 'Outside Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(54000)
        elif ((job_title_two == 'Data Analyst') | (job_title_two == 'Data Engineer')) & (in_out_london == 'Outside Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(82000)
        elif ((job_title_two == 'Data Analyst') | (job_title_two == 'Data Engineer')) & (in_out_london == 'In Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif ((job_title_two == 'Data Analyst') | (job_title_two == 'Data Engineer')) & (in_out_london == 'In Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(61000)
        elif ((job_title_two == 'Data Analyst') | (job_title_two == 'Data Engineer')) & (in_out_london == 'In Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(90000)
        elif (job_title_two == 'Insights Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(35000)
        elif (job_title_two == 'Insights Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(59000)
        elif (job_title_two == 'Insights Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(79000)
        elif (job_title_two == 'Insights Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif (job_title_two == 'Insights Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(60000)
        elif (job_title_two == 'Insights Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(84000)
        elif (job_title_two == 'Business Intelligence Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif (job_title_two == 'Business Intelligence Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(50000)
        elif (job_title_two == 'Business Intelligence Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(72000)
        elif (job_title_two == 'Business Intelligence Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(40000)
        elif (job_title_two == 'Business Intelligence Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(57000)
        elif (job_title_two == 'Business Intelligence Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(74000)
        elif (job_title_two == 'Business Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(34000)
        elif (job_title_two == 'Business Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(43000)
        elif (job_title_two == 'Business Analyst') & (in_out_london == 'Outside Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(70000)
        elif (job_title_two == 'Business Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Entry level'):
            average_uk_annual_salary.append(30000)
        elif (job_title_two == 'Business Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Associate'):
            average_uk_annual_salary.append(40000)
        elif (job_title_two == 'Business Analyst') & (in_out_london == 'In Greater London') & (seniority_level == 'Mid-Senior level'):
            average_uk_annual_salary.append(68000)

        average_uk_annual_salary = float(average_uk_annual_salary[0])
        print(average_uk_annual_salary)


        features = { 
           "average_uk_annual_salary": [average_uk_annual_salary], 
           "python":[python], 
           "excel": [excel],
            "powerbi": [powerbi],
            "sql": [sql], 
            "tableau" : [tableau], 
            "seniority_level" : [seniority_level],
            "industry_category": [industry_category], 
            "in_out_london" : [in_out_london],
            "tech_stack_count_group" : [tech_stack_count_group], 
            "job_title_two" :[job_title_two]
        }

        features_df = pd.DataFrame(features)

        features_df['average_uk_annual_salary'] = features_df['average_uk_annual_salary'].astype(float)
        features_df['python'] = features_df['python'].astype(str)
        features_df['excel'] = features_df['excel'].astype(str)
        features_df['powerbi'] = features_df['powerbi'].astype(str)
        features_df['sql'] = features_df['sql'].astype(str)
        features_df['tableau'] = features_df['tableau'].astype(str)
        features_df['seniority_level'] = features_df['seniority_level'].astype(str)
        features_df['industry_category'] = features_df['industry_category'].astype(str)
        features_df['in_out_london'] = features_df['in_out_london'].astype(str)
        features_df['tech_stack_count_group'] = features_df['tech_stack_count_group'].astype(str)
        features_df['job_title_two'] = features_df['job_title_two'].astype(str)

        print(features_df)

        prediction = model.predict(features_df)
        prediction = prediction[0]
        upper_bound = round(1840 + prediction, 2)
        lower_bound = round(prediction - 1840, 2)
        print(prediction)
        print(lower_bound)
        print(upper_bound)



    return render_template('results.html',  predictions=f"Your predicted annual salary range is: £{lower_bound} - £{upper_bound}")
    
@app.route ('/results')
def result():
    return render_template('results.html')





if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)


