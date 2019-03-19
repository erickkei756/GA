

employees = [{"Name": "Ron Swanson","Age": "xx","Department":"Management","Phone":"555-1234","Salary":"xx"},{"Name": "Leslie Knope","Age":"xx", "Department": "Management","Phone": "555-1234","Salary":"xx"},
{"Name": "Andy Dwyer","Age":"xx","Department": "Management","Phone": "555-1234","Salary": "$87,000"},{"Name":"April Ludgate","Age":"xx","Department":"Administration","Phone":"555-3345","Salary":"xx"}]

for emp in employees:
  #print(emp["name"])
  print(f"{emp['Name']} in {emp['Department']} can be reached at {emp['Phone']}. Age and salary are a secret!")
