from ipytest import *

# get service handle
service = connect_to_service()

# The ID and range of a sample spreadsheet.
spreadsheet_id = '1eOPUHLEj5LvFEFtdeOgNo3HN1u3z_pzNqRpj3-X2pCg'

# exam name
exam = 'IS20_WdP_kolokwium_rozgrzewka'

# copy pattern file to individual files
names_range = 'lista!A1:B'
all_locations = create_individual_files(service, spreadsheet_id,
                                        exam, names_range)
