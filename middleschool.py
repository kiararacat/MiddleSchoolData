# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Kiararacat
This is a temporary script file.
"""
#%% Load Data 
import pandas as pd 
data = pd.read_csv('middleSchoolData.csv')
#%% Q1
a = data['applications'].isna().sum()
#%%
a = data['acceptances'].isna().sum() 
#%%
import numpy as np 
applications = data['applications'] #loading application data
acceptances = data['acceptances'] #loading acceptances data
q1r = np.corrcoef(applications,acceptances)

import matplotlib.pyplot as plt
plt.plot(applications,acceptances,'o') #o represents scatter
plt.xlabel('applications')
plt.ylabel('acceptances')
plt.title('App X Acc')

#%% Q2
q2cleandata=data.dropna(subset=['school_size'])
app_rate=q2cleandata['applications']/q2cleandata['school_size']
app_rateAcceptR=np.corrcoef(app_rate,q2cleandata.acceptances)

plt.plot(app_rate,q2cleandata.acceptances,'o')

#%% Q3 
a=data['acceptances'].isna().sum()
a=data['school_size'].isna().sum()
acc_rate=q2cleandata['acceptances']/q2cleandata['school_size']
school=data.school_name[acc_rate.idxmax()]
row = acc_rate.idxmax()

#%% Q4: relationship between L-Q and V-X? 
# multiple colums, use correlation matrix
q4cd=data.dropna(subset=data.loc['rigorous_instruction':'trust'].columns)
q4cd=data.dropna(subset=data.loc['student_achievement':'math_scores_exceed'].columns)
# .columns will help gather multiple columns 
perceptions=q4cd.loc[:,'rigorous_instruction':'trust']
#%% :, is slicing, very Niubi
performances=q4cd.loc[:,'student_achievement':'math_scores_exceed']
q4cor=pd.concat((perceptions,performances),axis=1)
q4cor=q4cor.corr()
q4cor=q4cor.iloc[:6,-3:]
# very highend 
plt.imshow(q4cor)
plt.colorbar()












