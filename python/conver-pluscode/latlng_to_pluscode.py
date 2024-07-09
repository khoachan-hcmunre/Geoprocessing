import pandas as pd
import openlocationcode.openlocationcode as olc


def generate_plus_code(latitude, longitude, code_length):
    code = olc.encode(latitude, longitude)
    return code[:code_length]


excel_file = "Cẩm_Xuyên.xlsx"
excel_data = pd.read_excel(excel_file, sheet_name=None)

# Iterate through each sheet 
for sheet_name, sheet_data in excel_data.items():
    print("Sheet:", sheet_name)
    
    latitudes = sheet_data['lat'].tolist()
    longitudes = sheet_data['lng'].tolist()
    
    # Convert coordinates to PlusCodes
    plus_codes = []
    for lat, lng in zip(latitudes, longitudes):
        plus_code = generate_plus_code(lat, lng, code_length=11) 
        plus_codes.append(plus_code)
    
    # Add PlusCode column
    sheet_data['Plus Code'] = plus_codes
    

    output_file = f"{sheet_name}_output.xlsx"
    sheet_data.to_excel(output_file, index=False)
