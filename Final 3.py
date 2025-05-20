import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

try:
    car_data = pd.read_csv('Dataset_Batch37.csv')
    print(car_data.describe())

    X = car_data[['User ID', 'Gender', 'Age', 'EstimatedSalary']].copy()
    y = car_data['Purchased']

    X.loc[:, 'Gender'] = X['Gender'].astype('category').cat.codes


    scaler = StandardScaler()
    X[['Age', 'EstimatedSalary']] = scaler.fit_transform(X[['Age', 'EstimatedSalary']])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = SVC()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    print("\nConfusion Matrix:\n", cm)
    print("\nAccuracy:", accuracy)

except FileNotFoundError:
    print("Dataset_Batch37.csv not found. Check file path.")
except Exception as e:
    print(f"An error occurred: {e}")