from google.colab import files
import pandas as pd

#upload the file local system 
uploaded = files.upload()

#Get the filename of the uploaded file
aaa = list(uploaded.keys())[0]

#Read the csv file using pandas 
df = pd.read_csv(aaa)
df.head(20)
df.tail(10)
#Display the dataframe
#df.iloc[2:9] # dispifo()lay first few rows
