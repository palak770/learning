# Label Encoding using scikit learn 

from sklearn.preprocessing import LabelEncoder
import pandas as pd 

data = pd.DataFrame({
    'Fruits':['apple','mango','banana','mango','apple','apple','orange'],
    'Price':[0.1,1.43,2.4,4.56,28.93,34.67,100.2]
    
    })

le =LabelEncoder()
data["Fruit_Encoded"] = le.fit_transform(data['Fruits'])
print(data)
print('category mapping:',le.classes_)


# Using Pandas Categorical Codes
"""
Pandas offers a built-in approach to label encoding without external libraries.
Converts category values into integer codes using astype('category').cat.codes.
Faster for quick preprocessing inside Pandas workflows.
Mapping can be extracted using .cat.categories.

"""

data['Fruit_Encoded_Pandas'] = data['Fruits'].astype('category').cat.codes
print(data)
print('category mapping:',dict(enumerate(data['Fruits'].astype('category').cat.categories)))


# Encoding ordinal data manually 

"""
Used when categories have a natural order.
Manual dictionary mapping prevents incorrect ordering assumptions.
Useful for models that rely on ranking information.
Encoded using map() function in Pandas.
    """

data_2=pd.DataFrame({
    'Satisfaction level':['low','high','medium','high','low','high','medium'],
    'Scores':[3,4,7,5,7,9,1]
})

Satisfaction_order = {'low':0,'medium':1,'high':2}
data_2['Satisfaction_endcoded']=data_2['Satisfaction level'].map(Satisfaction_order)
print(data_2)
