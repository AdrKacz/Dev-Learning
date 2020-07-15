import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

from random import random


def encode_data(data):
	data["Sex_Enc"] = data["Sex"].replace({"male":0,"female":1})
	data["Embarked_Enc"] = data["Embarked"].replace({"S":0,"C":1, "Q":2})

def output_submission(test_data, y_test):
	output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': y_test})
	output.to_csv("submission.csv", index=False)
	print("Your submssion was successfully saved!")

def basic_training(random_state=0, output=True):
	train_data = pd.read_csv(train_file_path)
	test_data = pd.read_csv(test_file_path)

	encode_data(train_data)
	encode_data(test_data)

	features = ["Sex_Enc", "Pclass", "Embarked_Enc"]

	Xy = train_data[features + ["Survived"]].dropna()

	X = Xy[features]
	y = Xy.Survived

	clf = RandomForestClassifier(random_state=random_state)
	clf.fit(X, y)


	X_test = test_data[features]

	if output:
		output_submission(test_data, clf.predict(X_test))

def mca(data):
	# Perfom MCA ~ ACM (Analyse factorielle des correspondance multiples)
	# Indeed, main composant are discrete
	# data["Sex_Enc"] = data["Sex"].replace({"male":0,"female":1})
	# data["Embarked_Enc"] = data["Embarked"].replace({"S":0,"C":1, "Q":2})

	# train_data["Age_Filled"] = train_data.fillna(train_data.Age.median())

	# train_data.assign(Age_Filled_Enc)
	# quantile_age = train_data.Age.quantile([0.25, 0.5, 0.75])
	# train_data["Age_Filled_Enc"][(train_data["Age_Filled"] < quantile_age[0.25])] = 0
	# train_data["Age_Filled_Enc"][(train_data["Age_Filled"] > quantile_age[0.25]) & (train_data["Age_Filled"] < quantile_age[0.5])] = 1
	# train_data["Age_Filled_Enc"][(train_data["Age_Filled"] > quantile_age[0.5]) & (train_data["Age_Filled"] < quantile_age[0.75])] = 2
	# train_data["Age_Filled_Enc"][(train_data["Age_Filled"] > quantile_age[0.75])] = 3

	# train_data.assign(Fare_Enc)
	# quantile_fare = train_data.Fare.quantile([0.25, 0.5, 0.75])
	# train_data["Fare_Enc"][(train_data["Fare"] < quantile_fare[0.25])] = 0
	# train_data["Fare_Enc"][(train_data["Fare"] > quantile_fare[0.25]) & (train_data["Fare"] < quantile_fare[0.5])] = 1
	# train_data["Fare_Enc"][(train_data["Fare"] > quantile_fare[0.5]) & (train_data["Fare"] < quantile_fare[0.75])] = 2
	# train_data["Fare_Enc"][(train_data["Fare"] > quantile_fare[0.75])] = 3





if __name__ == "__main__":
	train_file_path = "Input/train.csv"
	test_file_path = "Input/test.csv"

	print("-\n--Titanic Training---\n")
	print("List of training functions:")
	print("\tbasic_training()")