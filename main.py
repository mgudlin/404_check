import pandas as pd
import requests

# Replace 'input_file.xlsx' with the path to your Excel file
input_file = 'input_file.xlsx'

# Replace 'Sheet1' with the name of the sheet containing your data
sheet_name = 'Sheet1'

# Replace 'URL_Column' with the name of the column containing the URLs
url_column = 'URL'

# Create a new column name for the 404 status
new_column = 'Status_404'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(input_file, sheet_name=sheet_name)

# Function to check if a URL returns a 404 status
def check_404(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return "404"
        else:
            return ""
    except:
        return ""

# Apply the check_404 function to the URL column and create a new column with the results
df[new_column] = df[url_column].apply(check_404)

# Save the modified DataFrame back to the Excel file
output_file = 'output_file.xlsx'
df.to_excel(output_file, index=False)
