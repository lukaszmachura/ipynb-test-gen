from ipytest import *

# get service handle
service = connect_to_service()

# The ID and range of a sample spreadsheet.
spreadsheet_id = '1eOPUHLEj5LvFEFtdeOgNo3HN1u3z_pzNqRpj3-X2pCg'

# exam name
exam = 'IS20_WdP_kolokwium1'

# copy pattern file to individual files
names_range = 'lista!A1:B'
all_locations = create_individual_files(service, spreadsheet_id,
                                        exam, names_range)

# replace individual tasks
problem_range = 'zadanie1!A1:A'
replace_line = 36
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'zadanie2!A1:A'
replace_line = 55
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'zadanie2!B1:B'
replace_line = 59
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'zadanie3!A1:A'
replace_line = 79
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 'zadanie4!A1:A'
replace_line = 108
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)
