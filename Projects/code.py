# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
df=pd.read_csv(path)

# Code starts here
newdf=df['Gender'].replace('-','Agender',inplace=True)
print(newdf)
gender=pd.Series(df['Gender']).value_counts()
print(gender)

gender=pd.Series(df['Gender']).value_counts()
plt.figure(figsize=(6,6))
plt.pie(gender)
plt.title('Gender Categories')
plt.legend(labels=['Male','Female','Agender'])
df['Alignment'].value_counts().plot(kind='bar')
data=df[['Combat','Intelligence']].copy()
covariance=data.cov().iloc[0,1]
std_Combat=data.Combat.std()
std_Intelligence=data.Intelligence.std()
data=df[['Combat','Strength']].copy()
covariance=data.cov().iloc[0,1]
std_Combat=data.Combat.std()
std_Strength=data.Strength.std()
pearson=covariance/(std_Combat*std_Strength)
print("Pearson's Correlation Coefficent:",pearson)
q1=df['Total'].quantile(0.99)
newdf=df[df["Total"] >q1]
super_best_names=newdf['Name'].tolist()
print(super_best_names)



