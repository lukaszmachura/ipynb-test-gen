# ipynb-test-gen
Generator plików *.ipynb na kolokwia/egzaminy WdP, AiP, PP, P...

Requirements
1. Google Sheets API for Python. Basically follow [this guide](https://developers.google.com/sheets/api/quickstart/python)

2. Google sheet, with the structure similar to the [example provided](https://docs.google.com/spreadsheets/d/17T0Nnea1gwaAUyM7Sy2awiXyti7_2P_uOjbP8bOJxmo/edit?usp=sharing)

3. In original *ipynb file locate the line (`replace_line`) for certain task (`z1`) which you have to replace and find and provide range from sheet (`problem_range`)

```
# replace individual tasks
problem_range = 'z1!A1:A'
replace_line = 37
replace_problems(service,
                 spreadsheet_id,
                 all_locations,
                 problem_range,
                 replace_line)
```

For each task, and each line you have to create a similar call.
