import pandas as pd # handle tabular data , excel , sql tables, data tranformation filtering , grouping like this  reads and write data from csv and do data data anyalsis and manuiplation too 
import numpy as np # numerical computing library for working with arrays and matrices , mathematical functions , random number generation , linear algebra , fourier transform , statisticss , optimization and more
import seaborn as sns # data visualization library based on matplotlib , provides high level interface for creating informative and attractive statistical graphics
import matplotlib.pyplot as plt # plotting library for creating static , animated and interactive visualizations in python


titanic_data = pd.read_csv('Titanic-Dataset.csv') # read the csv file and load it into a pandas dataframe
print(titanic_data.head()) # display the first 5 rows of the dataframe
print(titanic_data.info()) # display the summary of the dataframe including the data types and non-null values
print(titanic_data.describe()) # display the statistical summary of the numerical columns in the dataframe
print(titanic_data.isnull().sum()) # display the number of missing values in each column

# Handling missing values
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True) # fill missing values in 'Age' column with the median age
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True) # fill missing values in 'Embarked' column with the mode (most frequent value)
titanic_data.drop(columns=['Cabin'], inplace=True) # drop the 'Cabin' column as it has too many missing values
print(titanic_data.isnull().sum()) # verify that there are no more missing values
print(titanic_data.duplicated().sum()) # check for duplicate rows in the dataframe
titanic_data.drop_duplicates(inplace=True) # remove duplicate rows
print(titanic_data.duplicated().sum()) # verify that there are no more duplicate rows

# Data type conversion
titanic_data['Pclass'] = titanic_data['Pclass'].astype('category') # convert 'Pclass' column to categorical data type

# Feature engineering
''' Feature engineering is the process of using domain knowledge to create new features or modify existing features to improve the performance of machine learning models.'''

titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1 # create a new feature 'FamilySize' by combining 'SibSp' and 'Parch'

titanic_data['IsAlone'] = np.where(titanic_data['FamilySize'] > 1, 0, 1) # create a new feature 'IsAlone' to indicate if the passenger is alone or not
print(titanic_data.head()) # display the first 5 rows of the modified dataframe

# Outlier detection and removal
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25) # calculate the first quartile (25th percentile)
    Q3 = df[column].quantile(0.75) # calculate the third quartile (75th percentile)
    IQR = Q3 - Q1 # calculate the interquartile range (IQR)
    lower_bound = Q1 - 1.5 * IQR # calculate the lower bound for outliers
    upper_bound = Q3 + 1.5 * IQR # calculate the upper bound for outliers
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)] # return the dataframe without outliers
titanic_data = remove_outliers(titanic_data, 'Fare') # remove outliers from the 'Fare' column
print(titanic_data.shape) # display the shape of the modified dataframe
print(titanic_data.describe()) # display the statistical summary of the modified dataframe

# Data normalization
titanic_data['Fare'] = (titanic_data['Fare'] - titanic_data['Fare'].min()) / (titanic_data['Fare'].max() - titanic_data['Fare'].min()) # normalize the 'Fare' column to a range of 0 to 1
print(titanic_data.head()) # display the first 5 rows of the final cleaned dataframe

# Save the cleaned data to a new CSV file
titanic_data.to_csv('Titanic-Dataset-Cleaned.csv', index=False) # save the cleaned dataframe to a new csv file without the index

# Visualizations to understand the data better
sns.countplot(x='Survived', data=titanic_data) # count plot of survivors
plt.title('Count of Survivors') # title of the plot
plt.show() # display the plot
sns.histplot(titanic_data['Age'], bins=30, kde=True) # histogram of ages with kernel density estimate
plt.title('Age Distribution') # title of the plot
plt.show() # display the plot
sns.boxplot(x='Pclass', y='Fare', data=titanic_data) # box plot of fare by passenger class
plt.title('Fare by Passenger Class') # title of the plot
plt.show() # display the plot'


#final c;eaning dataset preview
print(titanic_data.head())
plt.show() # display the plot
print(titanic_data.head()) # display the first 5 rows of the final cleaned dataframe
