import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pickle

# load the csv file
df = pd.read_csv('iris.csv')

print(df.head())

# Select independent and dependent variable
x = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

# Split the dataset into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)

# Feature scaling
sc = StandardScaler()
x_scaled_train = sc.fit_transform(x_train)
x_scaled_test = sc.transform(x_test)

# Instantiate the model
clf = RandomForestClassifier()
knn = KNeighborsClassifier()
svm = SVC()

# Fit the model
clf.fit(x_scaled_train, y_train)
knn.fit(x_scaled_train, y_train)
svm.fit(x_scaled_train, y_train)

# Make pickle file of our model
pickle.dump(clf, open("clf_model_iris.pkl", "wb"))
pickle.dump(knn, open("knn_model_iris.pkl", "wb"))
pickle.dump(svm, open("svm_model_iris.pkl", "wb"))