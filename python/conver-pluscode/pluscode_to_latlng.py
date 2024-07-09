import pandas as pd
import openlocationcode.openlocationcode as olc


excel_file = "plc_brvt1.xlsx"
excel_data = pd.read_excel(excel_file, sheet_name=None)

# Iterate through each sheet
for sheet_name, sheet_data in excel_data.items():
    print("Sheet:", sheet_name)
    
    # PlusCodes are in a column named 'Plus_Code'
    plus_codes = sheet_data['Plus Code'].tolist()
    
    # Convert Plus Codes to coordinates
    coordinates = []
    for plus_code in plus_codes:
        decoded_code = olc.decode(plus_code)
        latitude, longitude = decoded_code.latitudeCenter, decoded_code.longitudeCenter
        coordinates.append((latitude, longitude))
    
    # Add lat, lng
    sheet_data['Latitude'] = [coord[0] for coord in coordinates]
    sheet_data['Longitude'] = [coord[1] for coord in coordinates]
    

    with pd.ExcelWriter(excel_file, mode='a', if_sheet_exists='replace') as writer:
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)
