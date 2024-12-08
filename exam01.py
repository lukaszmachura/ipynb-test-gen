from ipytest import *
import sys

# get service handle
service = connect_to_service()

# The ID and range of a sample spreadsheet.
spreadsheet_id = '17T0Nnea1gwaAUyM7Sy2awiXyti7_2P_uOjbP8bOJxmo'

# exam name
exam = ''
if not exam:
    # take the exam name from the conf file (=this file)
    exam = sys.argv[0].split('/')[-1].strip('.py')

# copy pattern file to individual files
names_range = 'names!A1:B'
all_locations = create_individual_files(service, spreadsheet_id,
                                        exam, names_range)

# replace individual tasks
problem_range = 't1!A1:A'
replace_line = 24
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 't2!A1:A'
replace_line = 49
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

problem_range = 't3!A1:A'
replace_line = 74
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)
