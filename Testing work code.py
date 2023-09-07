import pandas as pd

# Step 1: Please copy the path of the excel sheet you want to use (right click the sheet in file explore and click copy path). 
# You may have to modify is by adding double backwards slashes where there are single backword slashes.
input_file = "C:\\Users\\dcnat\\Downloads\\Searches-08-30-2023.xlsx" 
df = pd.read_excel(input_file)

# Step 2: This is assuming the column that I am counting the number of hits is called "Search Phrase". Adjust as needed.
search_counts = df['Search Phrase'].value_counts().reset_index()
search_counts.columns = ['Search Phrases', 'Count']

# Step 3: Have an empty excel sheet saved and named. This is where the results are going to be. Do the same as step #1. 
# Right click the empty sheet location and click copy path. Then you may have to modify the path here with double backward slashes where there are single backword slashes.
output_file = "C:\\Users\\dcnat\\OneDrive\\Documents\\Output.xlsx"  
search_counts.to_excel(output_file, index=False)

print(search_counts)        