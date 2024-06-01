employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


new_dict = dict()
new_dict = new_dict.fromkeys(employees,defaults)



print(new_dict)