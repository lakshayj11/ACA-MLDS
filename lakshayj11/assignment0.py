import numpy as np
import pandas as pd

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


for i in range(0, 620):
    if (df['Relationship_status'][i] == 'Single_and_stud'):
         df.iloc[i, 6] = (df['Practice_hours'][i] + df['Posts_shared'][i] + df['Bulla_hours'][i] + 10)*0.02 + df['Classes_missed'][i]*(-0.025)
    elif (df['Relationship_status'][i] == 'Committed_inside_campus'):
         df.iloc[i, 6] = (df['Practice_hours'][i] + df['Posts_shared'][i] + df['Bulla_hours'][i] - 10)*0.02 + df['Classes_missed'][i]*(-0.025)
    else:
        df.iloc[i, 6] = (df['Practice_hours'][i] + df['Posts_shared'][i] + df['Bulla_hours'][i])*0.02 + df['Classes_missed'][i]*(-0.025)
        

enthu_Hall_2 = sum(df.iloc[0:130, 6])/130
enthu_Hall_3 = sum(df.iloc[130:270, 6])/140
enthu_Hall_5 = sum(df.iloc[270:420, 6])/150
enthu_Hall_6 = sum(df.iloc[420:500, 6])/80
enthu_Hall_12 = sum(df.iloc[500:620, 6])/120
max_enthu = max(enthu_Hall_2, enthu_Hall_3, enthu_Hall_5, enthu_Hall_6, enthu_Hall_12)

print("The winner is ", end='')
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

enthu_csv = pd.DataFrame(df.iloc[:, 6])

enthu_csv.to_csv("enthu_data.csv")
