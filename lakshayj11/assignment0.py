import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv('galaxy_data.csv')

#H5_STRENGTH = 150
#H2_STRENGTH = 130
#H3_STRENGTH = 140
#H12_STRENGTH = 120
#H6_STRENGTH = 80

Hall_2 = df.iloc[0:130, :].values 
Hall_3 = df.iloc[130:270, :].values
Hall_5 = df.iloc[270:420, :].values
Hall_6 = df.iloc[420:500, :].values
Hall_12 = df.iloc[500:620, :].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,
                  strategy="mean")

imputer = imputer.fit(Hall_2[:, [1,4]])
imputer = imputer.fit(Hall_3[:, [1,4]])
imputer = imputer.fit(Hall_5[:, [1,4]])
imputer = imputer.fit(Hall_6[:, [1,4]])
imputer = imputer.fit(Hall_12[:, [1,4]])

Hall_2[:, [1, 4]] = imputer.transform(Hall_2[:, [1,4]])
Hall_3[:, [1, 4]] = imputer.transform(Hall_3[:, [1,4]])
Hall_5[:, [1, 4]] = imputer.transform(Hall_5[:, [1,4]])
Hall_6[:, [1, 4]] = imputer.transform(Hall_6[:, [1,4]])
Hall_12[:, [1, 4]] = imputer.transform(Hall_12[:, [1,4]])

imputer = SimpleImputer(missing_values=np.nan,
                  strategy="median")

imputer = imputer.fit(Hall_2[:, [2, 3]])
imputer = imputer.fit(Hall_3[:, [2, 3]])
imputer = imputer.fit(Hall_5[:, [2, 3]])
imputer = imputer.fit(Hall_6[:, [2, 3]])
imputer = imputer.fit(Hall_12[:, [2, 3]])

Hall_2[:, [2, 3]] = imputer.transform(Hall_2[:, [2, 3]])
Hall_3[:, [2, 3]] = imputer.transform(Hall_3[:, [2, 3]])
Hall_5[:, [2, 3]] = imputer.transform(Hall_5[:, [2, 3]])
Hall_6[:, [2, 3]] = imputer.transform(Hall_6[:, [2, 3]])
Hall_12[:, [2, 3]] = imputer.transform(Hall_12[:, [2, 3]])

imputer = SimpleImputer(missing_values=np.nan,
                  strategy="constant", 
                  fill_value="Single_and_stud" )

imputer = imputer.fit(Hall_2[:, [1, 5]])
imputer = imputer.fit(Hall_3[:, [1, 5]])
imputer = imputer.fit(Hall_6[:, [1, 5]])
imputer = imputer.fit(Hall_12[:, [1, 5]])

Hall_2[:, [1, 5]] = imputer.transform(Hall_2[:, [1, 5]])
Hall_3[:, [1, 5]] = imputer.transform(Hall_3[:, [1, 5]])
Hall_6[:, [1, 5]] = imputer.transform(Hall_6[:, [1, 5]])
Hall_12[:, [1, 5]] = imputer.transform(Hall_12[:, [1, 5]])

imputer = SimpleImputer(missing_values=np.nan,
                  strategy="constant", 
                  fill_value="Committed_inside_campus" )

imputer = imputer.fit(Hall_5[:, [1, 5]])

Hall_5[:, [1, 5]] = imputer.transform(Hall_5[:, [1, 5]])

df.iloc[0:130,:] = Hall_2[:,:]
df.iloc[130:270,:] = Hall_3[:,:]
df.iloc[270:420,:] = Hall_5[:,:]
df.iloc[420:500,:] = Hall_6[:,:]
df.iloc[500:620,:] = Hall_12[:,:]

Enthu = []

for i in range(0, 620):
    if (df['Relationship_status'][i] == 'Single_and_stud'):
         e = (df['Practice_hours'][i] + df['Posts_shared'][i] + df['Bulla_hours'][i] + 10)*0.02 + df['Classes_missed'][i]*(-0.025)
    elif (df['Relationship_status'][i] == 'Committed_inside_campus'):
         e = (df['Practice_hours'][i] + df['Posts_shared'][i] + df['Bulla_hours'][i] - 10)*0.02 + df['Classes_missed'][i]*(-0.025)
    else:
        e = (df['Practice_hours'][i] + df['Posts_shared'][i] + df['Bulla_hours'][i])*0.02 + df['Classes_missed'][i]*(-0.025)
    Enthu.append(e)    
    

Enthu = pd.DataFrame(Enthu)
Hall_2 = pd.DataFrame(Hall_2)
Hall_3 = pd.DataFrame(Hall_3)
Hall_5 = pd.DataFrame(Hall_5)
Hall_6 = pd.DataFrame(Hall_6)
Hall_12 = pd.DataFrame(Hall_12)

Final_data = pd.concat([Hall_2, Hall_3, Hall_5, Hall_6, Hall_12])

for i in range(620):
    Final_data[i][6] = Enthu[i]

Final = pd.DataFrame(Final_data)

#Final.to_csv("galaxy_data.csv")

enthu_Hall_2 = sum(Enthu[0:130])/130
enthu_Hall_3 = sum(Enthu[130:270])/140
enthu_Hall_5 = sum(Enthu[270:420])/150
enthu_Hall_6 = sum(Enthu[420:500])/80
enthu_Hall_12 = sum(Enthu[500:620])/120
max_enthu = max(enthu_Hall_2, enthu_Hall_3, enthu_Hall_5, enthu_Hall_6, enthu_Hall_12)

print("The winner is ")
if enthu_Hall_2 == max_enthu:
    print("Hall 2")
elif enthu_Hall_3 == max_enthu:
    print("Hall 3")
elif enthu_Hall_5 == max_enthu:
    print("Hall 5")
elif enthu_Hall_6 == max_enthu:
    print("Hall 6")
else:
    print("Hall 12")

with open('enthu_data.csv', 'w', newline = '') as file:
    dash = csv.writer(file)
    dash.writerow(["Enthu"])
    for i in range(0, 620):
        dash.writerow([Enthu[i]])        
        

