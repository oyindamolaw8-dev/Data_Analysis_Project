import pandas as pd

# Read from CVS & Excel Files
df_for_cvs_original = pd.read_csv(r"c:\Users\User1\Downloads\student_performance_data.csv")


#copied the orignal data into another variable
df_cvs_copied = df_for_cvs_original.copy()

print(df_cvs_copied)    # your total file

print(df_cvs_copied.info()) # data type and memory (shows all information about your data
# I added something