# ipynb-test-gen
Generator plików *.ipynb na kolokwia/egzaminy WdP, AiP, PP, P...

Requirements
1. Google Sheets API for Python. Basically follow [this guide](https://developers.google.com/sheets/api/quickstart/python)

2. Google sheet, with the structure similar to the [example provided](https://docs.google.com/spreadsheets/d/17T0Nnea1gwaAUyM7Sy2awiXyti7_2P_uOjbP8bOJxmo/edit?usp=sharing)


How to setup the script
1. import functions
```
from ipytest import *
```

2. get service handle
```
service = connect_to_service()
```

3. The ID and range of a sample spreadsheet.
```
spreadsheet_id = '17T0Nnea1gwaAUyM7Sy2awiXyti7_2P_uOjbP8bOJxmo'
```

4. Provide exam name. Directory with such a name will be created, if doesn't exists.
```
exam = 'kc20_pp_kolokwium1'
```

5. Copy pattern file to individual files
```
names_range = 'names!A1:B'
all_locations = create_individual_files(service, spreadsheet_id,
                                        exam, names_range)
```

3. In original, source *ipynb file locate the line (`replace_line`) for certain task (`t1`) which you have to replace as well as find and provide range with data from sheet (`problem_range`)

```
# replace individual tasks
problem_range = 't1!A1:A'
replace_line = 37
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)
```

For each task, and each line you have to create a similar call.
