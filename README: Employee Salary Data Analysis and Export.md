README: Employee Salary Data Analysis and Export

This notebook shows us how to analyze a salary dataset using Python and R in Google Colab. It inspects data, filters it, provides summary statistics, and exports results to a ZIP file for download. The notebook concludes by reading the exported data back into R. (I had to use Google Colab because my Jupyter Notebook crashed, R wasn't able to download on my Mac properly, and vscode was unavailable to me, however this issue will be rectified and I will move forward with VS code.

Name of dataset:
salary_data.csv

Columns
* EmployeeName
* JobTitle
* TotalPay
upload this file to your Colab environment before running the notebook.
Features & Steps

Step one - Import Libraries
import pandas as pd
import zipfile
import os
from IPython.display import FileLink
Data manipulation, file compression, and creating a download link in Colab.

Step two - Load Dataset
python
df = pd.read_csv("salary_data.csv")
print("Data imported successfully!")
print(df.head())

CSV file is read and displays first five rows to confirm that the loading was successful.

Step three -  Dataset Columns

print("\nDataset Columns:", list(df.columns))
To help you understand the structure of the data, print column names.


Step four- Employee search

python
search_results = df[df['EmployeeName'].str.contains("John Smith", case=False, na=False)]
print("\nExample Search:\n", search_results)

Search for employees named "John Smith."

Step five - High Earners

python
high_earners = df[df['TotalPay'] > 50000]
print(f"\n{len(high_earners)} employees earn above $50,000.")


Filters and counts the number of employees earning more than $50,000.

Step 6: Job Title Breakdown

job_counts = df['JobTitle'].value_counts().head(10).to_dict()
print("\nEmployee count by Job Title (first 10):", job_counts)

Calculates the top 10 most common job titles by frequency.


Step 7 - Export as CSV and ZIP

python
output_csv = "Employee_Profile.csv"
df.to_csv(output_csv, index=False)

zip_filename = "Employee_Profile.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
 zipf.write(output_csv)

print(f"Employee profile exported and zipped as {zip_filename}")

Saves the DataFrame as a CSV file and compresses it into a ZIP file for easier download.

Step 8 - Create a Download Link
display(FileLink(zip_filename))

This creates a clickable link in Colab to download the ZIP file.

You can run R code within a Python notebook in Google Colab using the `rpy2` extension
%load_ext rpy2.ipython
Basic R Code
%%R
x <- c(1, 2, 3, 4, 5)
mean(x)

Demonstrates executing R code from a Python notebook using the `%%R` cell magic.
Unzipping and Load CSV in R

%%R
unzip("Employee_Profile.zip")
list.files()

Load the CSV into an R data frame
df <- read.csv("Employee_Profile.csv")

Display first few rows
head(df)
