import pandas as pd
from Lib.json.decoder import NaN



df = pd.read_excel("IO/inputs/sample data.xlsx",sheet_name = "student answers")
#Df is original dataframe
#print(df)
#Answers with length less than the value of minimum_length will be excluded
minimum_length = 5; #Arbitrarily set to 5

df["Answer"] = df["Answer"].replace("",NaN)
df2 = df[(df["Answer"].str.len() >= minimum_length)]
df2.dropna(how="all")

#Create auto-reject df
auto_reject_df = df[
    (df["Answer"].str.len() < minimum_length) |
    (df["Answer"].isna())
]

#Replace autoreject answer match as false
auto_reject_df['Answer Match'] = auto_reject_df['Answer Match'].replace(NaN, "False")


#df2 is dataframe planned on being processed to the agent


#First load rubric into a dataframe, will pull information from said rubric.
df_rubric = pd.read_excel("IO/inputs/sample data.xlsx",sheet_name = "rubric")


print(df2.memory_usage(deep=True).sum())
df2.drop(['Q Text'],axis=1,inplace=True)
print(df2.memory_usage(deep=True).sum())

df2.to_csv("IO/outputs/sample_data_answers.csv")
auto_reject_df.to_csv("IO/outputs/auto_reject_answers.csv")





