from flask import Flask, render_template, jsonify, request
# fields,marshall_with
import config1
from utils import DataScienceSalary
import traceback
# import pymongo
app = Flask(__name__)

# db=pymongo()
# db.init_app(app)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict_salary', methods = ['GET','POST'])
def predict_salary():
    try:
        if request.method == 'POST':
            data = request.form.get
            # print("User Data is :",data)
            work_year = data('work_year')
            experience_level = data('experience_level')
            employment_type  = data('employment_type')
            job_title = data('job_title')
            salary = int(data('salary'))
            salary_currency= data('salary_currency')
            employee_residence = data('employee_residence')
            remote_ratio = int(data('remote_ratio'))
            company_location = data('company_location')
            company_size=data('company_size')


            DataScienceSalary_res = DataScienceSalary(work_year, experience_level,
                                          employment_type, job_title,
                                        salary, salary_currency, employee_residence,
                                        remote_ratio,company_location,company_size)
            dssalary_res = DataScienceSalary_res.get_predicted_res()
            # DataScienceSalary_res.database()

            

            return  render_template('index1.html', prediction = dssalary_res)


        else:
            data = request.args.get

            # print("User Data is ::::",data)
            
            work_year = data('work_year')
            experience_level = data('experience_level')
            employment_type  = data('employment_type')
            job_title = data('job_title')
            salary = int(data('salary'))
            salary_currency= data('salary_currency')
            employee_residence = data('employee_residence')
            remote_ratio = int(data('remote_ratio'))
            company_location = data('company_location')
            company_size=data('company_size')

            DataScienceSalary_res = DataScienceSalary(work_year, experience_level,
                                          employment_type, job_title,
                                        salary, salary_currency, employee_residence,
                                        remote_ratio,company_location,company_size)
            dssalary_res = DataScienceSalary_res.get_predicted_res()

            # salary_pre= predict_salary(work_year, experience_level,
            #                               employment_type, job_title,
            #                             salary, salary_currency, employee_residence,
            #                             remote_ratio,company_location,company_size)
            # prediction1 = salary_pre.predict_salary()
            # salary_pre.database()

            # DataScienceSalary_res = DataScienceSalary(work_year, experience_level,
            #                               employment_type, job_title,
            #                             salary, salary_currency, employee_residence,
            #                             remote_ratio,company_location,company_size)
            # dssalary_res = DataScienceSalary_res.get_predicted_res()
            # DataScienceSalary_res.database()
            return  render_template('index1.html', prediction = dssalary_res)

            
    except:
        print(traceback.print_exc())
        # return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config1.PORT_NUMBER,debug=False)