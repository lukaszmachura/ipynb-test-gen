from ipytest import *

# get service handle
service = connect_to_service()

# The ID and range of a sample spreadsheet.
spreadsheet_id = '1CFCTDf82zB7VRBBOLFEhw_46wk_Gn1axK38nlPGJnNo'

# exam name
exam = 'kc21_pp_kolokwium1'

# copy pattern file to individual files
names_range = 'lista!A1:B'
all_locations = create_individual_files(service, spreadsheet_id,
                                        exam, names_range)

# replace individual tasks
# 1
problem_range = 'z1!A1:A'
replace_line = 109
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

# 2
for problem_range, replace_line in (
        ('z2!A1:A', 147), ('z2!B1:B', 152)
    ):
    replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)


# 3
for problem_range, replace_line in (
        ('z3!A1:A', 190), ('z3!B1:B', 192),
        ('z3!C1:C', 193), ('z3!D1:D', 195),
    ):
    replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)

zad = 4
for problem_range, replace_line in (
        (f'z{zad}!A1:A', 231), (f'z{zad}!B1:B', 233),
        (f'z{zad}!C1:D', 235), (f'z{zad}!D1:D', 237),
        (f'z{zad}!E1:E', 239), (f'z{zad}!F1:F', 241),
        (f'z{zad}!G1:G', 243), (f'z{zad}!H1:H', 245),
    ):
    replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)
