from ipytest import *

# get service handle
service = connect_to_service()

# The ID and range of a sample spreadsheet.
spreadsheet_id = '19hhbp1Obf3ykhx3nYosyBY8SECn90pAaSz_4bO8bYGI'

# exam name
exam = 'kc20_pp_kolokwium1'

# copy pattern file to individual files
names_range = 'lista!A1:B'
all_locations = create_individual_files(service, spreadsheet_id,
                                        exam, names_range)

# replace individual tasks
problem_range = 'z1!A1:A'
replace_line = 100
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'z2!A1:A'
replace_line = 126
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'z3!A1:A'
replace_line = 151
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'z4!A1:A'
replace_line = 184
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)
