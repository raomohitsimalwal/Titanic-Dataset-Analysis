import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_data = pd.read_csv(r'D:\OneDrive\Prodigy InfoTech\DS_02\titanic\train.csv')

print(train_data.head())

##################################

#Data Cleaning

print(train_data.isnull().sum())

train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())

train_data['Cabin'] = train_data['Cabin'].fillna(train_data['Cabin'].mode()[0])

train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])

print(train_data.isnull().sum())

##################################

#Exploratory Data Analysis (EDA)

# #survived plot
sns.countplot(x='Survived', data=train_data)
plt.show()

# # Fare for different classes
sns.boxplot(x='Pclass', y='Fare', data=train_data)
plt.show()

# Survival by Age
sns.kdeplot(data=train_data, x='Age', hue='Survived', fill=True, common_norm=False)
plt.title('Survival by Age')
plt.show()

# Survival by Sex
sns.countplot(x='Survived', hue='Sex', data=train_data)
plt.title('Survival by Sex')
plt.show()

# Survival by Pclass
sns.countplot(x='Survived', hue='Pclass', data=train_data)
plt.title('Survival by Pclass')
plt.show()

# Survival by Embarked
sns.countplot(x='Survived', hue='Embarked', data=train_data)
plt.title('Survival by Embarked')
plt.show()

# Survival by Family Size
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1

sns.countplot(x='Survived', hue='FamilySize', data=train_data)
plt.title('Survival by Family Size')
plt.show()

# Survival by Fare
sns.kdeplot(data=train_data, x='Fare', hue='Survived', fill=True, common_norm=False)
plt.title('Survival by Fare')
plt.show()

#Survival by Pclass and Sex
sns.catplot(x='Pclass', y='Survived', hue='Sex', data=train_data, kind='bar')
plt.title('Survival by Pclass and Sex')
plt.show()
