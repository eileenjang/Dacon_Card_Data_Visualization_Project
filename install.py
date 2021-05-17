import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
from matplotlib import rc
rc('font', family='AppleGothic')
import seaborn as sns
import numpy as np
from collections import Counter
import warnings 
warnings.filterwarnings('ignore')
import gc
import os
import string
color = sns.color_palette()

#전처리

train = pd.read_csv('./data/train.csv')
#(train.shape)
#print(train.head())
#print(train.describe())
train['installments'] = train['installments'].fillna(1)

mask = train['days_of_week'].isin([0])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '월'         # Replace values based on boolean mask


mask = train['days_of_week'].isin([1])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '화'         # Replace values based on boolean mask


mask = train['days_of_week'].isin([2])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '수'         # Replace values based on boolean mask


mask = train['days_of_week'].isin([3])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '목'         # Replace values based on boolean mask

mask = train['days_of_week'].isin([4])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '금'         # Replace values based on boolean mask

mask = train['days_of_week'].isin([5])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '토'         # Replace values based on boolean mask


mask = train['days_of_week'].isin([6])  # Create a boolean mask of the condition
train.loc[mask, 'days_of_week'] = '일'         # Replace values based on boolean mask
#print(train.head())

train['weekday'] = '평일'
mask2 = train['days_of_week'].isin(['토','일'])
train.loc[mask2, 'weekday'] = '주말'  
#print(train.head())
train.drop(train[train['amount'] < 0].index, inplace=True)
#print(train.head())

#print(train['time'])

times=train['time']
def time_split(times):
    retimes = []
    for t in times:
        t = t.split(':')    
        if (int(t[1]) < 30):
            retimes.append(f'{t[0]}:15')
        else:
            retimes.append(f'{t[0]}:45')
    return retimes  

#train['retime'] = time_split(times)
#print(train)


def apply_time(x):
    t = x.split(':')   
    if int(t[1]) < 30:
        return f'{t[0]}:15'
    else:
        return f'{t[0]}:45'

train['time'] = train['time'].apply(apply_time)
#print(train)

#EDA
train_sorted_by_values = train.sort_values(by=['amount', 'card_id'] ,ascending=False)
#print(train_sorted_by_values.head())

# train_amount = train[train['store_id'] == 0]
# train_amount = train_amount[['date','amount']].groupby(["date"]).sum()
# train_amount.sort_values(by=['amount'], ascending=False)
# min = train_amount.iloc[-1].name.split('-')
# max = train_amount.iloc[0].name.spliid_groupt('-')
# print(min[0] + ", " + min[1])
# print(max[0] + ', ' + max[1])

id_group = train.groupby(["store_id"]).mean()
id_group = id_group.rename(columns= {'amount' : 'avg_total_income'})
id_group = id_group.reset_index()
merge = train.merge(id_group, how='left', on='store_id')
merge.to_excel('avg_total_income')
"""
def date_split(dates):
    redates=[]
    for d in dates:
        d=d.split('-')
        del d[2]
    return redates

#train_sorted_by_values_2['redate']=date_split(dates)
#print(train_sorted_by_values_2.head())

#인사이트 도출
train["total"] = train["amount"] * train["installments"]
def split_date(date):
    return date.split("-")
train["year"], train["month"], train["day"] = train['date'].apply(lambda x: split_date(x))
train["year"] = train["year"].astype(int)
train["month"] = train["month"].astype(int)
train["day"] = train["day"].astype(int)
#print(train.head())
sns.barplot(data=train, x="weekday", y="total")
#plt.show()
sns.barplot(data=train, x="days_of_week", y="total")
plt.show()
"""