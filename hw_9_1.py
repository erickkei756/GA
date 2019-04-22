
# import csv

import csv

employees = [
  {
    "first_name": "Bill",
    "last_name": "Lumbergh",
    "job_title": "Vice President",
    "hire_date": 1985,
    "performance_review": "excellent"
  }, {
    "first_name": "Michael",
    "last_name": "Bolton",
    "job_title": "Programmer",
    "hire_date": 1995,
    "performance_review": "poor"
  }, {
    "first_name": "Peter",
    "last_name": "Gibbons",
    "job_title": "Programmer",
    "hire_date": 1989,
    "performance_review": "poor"
  }, {
    "first_name": "Samir",
    "last_name": "Nagheenanajar",
    "job_title": "Programmer",
    "hire_date": 1974,
    "performance_review": "fair"
  }, {
    "first_name": "Milton",
    "last_name": "Waddams",
    "job_title": "Collator",
    "hire_date": 1974,
    "performance_review": "does he even work here?"
  }, {
    "first_name": "Bob",
    "last_name": "Porter",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }, {
    "first_name": "Bob",
    "last_name": "Slydell",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }
]



# This line opens or creates a `names.csv` file.
with open('tps_report.csv', 'w') as csv_file:
  fieldnames = ['first_name','last_name','job_title','hire_date','performance_review']
  writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
  writer.writeheader()
  for emp in employees:
    #print(emp['first_name'])


    #writer.writerow()
   #{'first_name':emp['first_name'],'last_name': #emp['last_name'],'job_title',emp['job_title']#,'hire_date':emp['hire_date'],#'performance_review':emp['performance_review']}
    # for key in emp:
      # writer.writerow(emp['first_name']['last_name'],['job_title'],['hire_date'],['performance_review'])
    #print(emp)
    writer.writerow(emp)
