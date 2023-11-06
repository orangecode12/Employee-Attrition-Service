
import requests

url = 'http://employee-attrition-env.eba-uwmps6pa.eu-west-1.elasticbeanstalk.com/predict'

employee = {"age":35,
            "businesstravel":"Travel_Rarely",
            "dailyrate":464,
            "department":"Research & Development",
            "distancefromhome":7,
            "education":1,
            "educationfield":"Other",
            "employeecount":1,
            "employeenumber":53,
            "environmentsatisfaction":1,
            "gender":"Male",
            "hourlyrate":75,
            "jobinvolvement":1,
            "joblevel":1,
            "jobrole":"Laboratory Technician",
            "jobsatisfaction":1,
            "maritalstatus":"Divorced",
            "monthlyincome":191,
            "monthlyrate":10910,
            "numcompaniesworked":1,
            "over18":"Y",
            "overtime":"No",
            "percentsalaryhike":12,
            "performancerating":1,
            "relationshipsatisfaction":1,
            "standardhours":80,
            "stockoptionlevel":1,
            "totalworkingyears":1,
            "trainingtimeslastyear":3,
            "worklifebalance":3,
            "yearsatcompany":1,
            "yearsincurrentrole":0,
            "yearssincelastpromotion":0,
            "yearswithcurrmanager":0}

            
print(requests.post(url, json = employee).json())


