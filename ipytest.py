from __future__ import print_function
import pickle
import os
import shutil
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def connect_to_service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service


def get_sheet_range(service, spreadsheetId, range):
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheetId,
                                range=range).execute()
    values = result.get('values', [])
    return values


def create_dir(name):
    try:
        p = os.path.join(".", name)
        os.mkdir(p)
    except OSError as error:
        print(error)


def create_individual_files(service, spreadsheet_id, exam, names_range):
    # create directory
    create_dir(exam)

    # all names and groups
    names_groups = get_sheet_range(service, spreadsheet_id, names_range)
    assert names_groups, 'No data found.'

    # copy files
    source_file = exam + '.ipynb'
    all_locations = []
    for idx, row in enumerate(names_groups):
        name= row[0]
        destination_file = exam
        if len(row) > 1:
            group = row[1]
            destination_file += "_" + group.replace(" ", "_")
        destination_file += "_" + name.replace(" ", "_")
        destination_file += '.ipynb'
        destination_loc = os.path.join(exam, destination_file)
        shutil.copyfile(source_file, destination_loc)
        all_locations.append(destination_loc)

    return all_locations


def replace_problems(service, spreadsheet_id,
                     all_locations, prange, replace_line):
    problems = get_sheet_range(service, spreadsheet_id, prange)
    assert problems, 'No data found.'
    for student_number, file in enumerate(all_locations):
        with open(file, 'rt') as handle:
            content = handle.readlines()
        with open(file, 'wt') as handle:
            for i, line in enumerate(content):
                if i == replace_line - 1:
                    newline = " " * 4 + '"'
                    # if \ exists, mask it with \\
                    p = problems[student_number % len(problems)][0]
                    p = p.replace("\\", "\\\\")  # latex forms
                    newline += p
                    # comma at the end of line
                    if "," in line[-2:]:
                        newline += '\\n",'
                    else:
                        newline += '\\n"'
                    newline += '\n'
                    handle.write(newline)
                else:
                    handle.write(line)


if __name__ == '__main__':
    print("ipytest module")
