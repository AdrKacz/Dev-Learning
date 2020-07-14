import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

train_file_path = "Input/train.csv"
test_file_path = "Input/test.csv"

train_data = pd.read_csv(train_file_path)
test_data = pd.read_csv(test_file_path)

train_data["Sex_Enc"] = train_data["Sex"].replace({"male":0,"female":1})
train_data["Embarked_Enc"] = train_data["Embarked"].replace({"S":0,"C":1, "Q":2})

test_data["Sex_Enc"] = test_data["Sex"].replace({"male":0,"female":1})
test_data["Embarked_Enc"] = test_data["Embarked"].replace({"S":0,"C":1, "Q":2})

features = ["Sex_Enc", "Pclass", "Embarked_Enc"]

Xy = train_data[features + ["Survived"]].dropna()

X = Xy[features]
y = Xy.Survived

clf = RandomForestClassifier(random_state=0)
clf.fit(X, y)


X_test = test_data[features]

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': clf.predict(X_test)})
output.to_csv("submission.csv", index=False)
print("Your submssion was successfully saved!")