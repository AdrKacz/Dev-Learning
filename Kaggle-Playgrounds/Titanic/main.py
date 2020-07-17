import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

from random import random

train_file_path = "Input/train.csv"
test_file_path = "Input/test.csv"


def encode_data(data):
	data["Sex_Enc"] = data["Sex"].replace({"male":0,"female":1})
	data["Embarked_Enc"] = data["Embarked"].replace({"S":0,"C":1, "Q":2})

def output_submission(test_data, y_test):
	output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': y_test})
	output.to_csv("submission.csv", index=False)
	print("Your submssion was successfully saved!")

def basic_training(train_data, test_data, random_state=0, output=True):

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

def mca(train_data, test_data):
	# Perfom MCA ~ ACM (Analyse factorielle des correspondance multiples)
	# Main composant have to be discrete

	features = ["Sex_Enc", "Embarked_Enc", "Age_Enc", "Fare_Enc"]

	train_data["Sex_Enc"] = train_data["Sex"].replace({"male":0,"female":1})
	train_data.Sex_Enc.fillna(train_data.Sex_Enc.median(), inplace=True)

	train_data["Embarked_Enc"] = train_data["Embarked"].replace({"S":0,"C":1, "Q":2})
	train_data.Embarked_Enc.fillna(train_data.Embarked_Enc.median(), inplace=True)

	train_data["Age_Enc"] = train_data.Age.fillna(train_data.Age.median())

	train_data["Fare_Enc"] = train_data.Fare.fillna(train_data.Fare.median())

	quantile_age = train_data.Age.quantile([.0, 0.25, 0.5, 0.75, 1.])

	train_data.Age_Enc.mask((quantile_age[.0] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[0.25]), other=0, inplace=True)
	train_data.Age_Enc.mask((quantile_age[0.25] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[0.5]), other=1, inplace=True)
	train_data.Age_Enc.mask((quantile_age[0.5] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[0.75]), other=2, inplace=True)
	train_data.Age_Enc.mask((quantile_age[0.75] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[1.0]), other=3, inplace=True)

	quantile_fare = train_data.Fare.quantile([.0, 0.25, 0.5, 0.75, 1.])

	train_data.Fare_Enc.mask((quantile_fare[.0] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[0.25]), other=0, inplace=True)
	train_data.Fare_Enc.mask((quantile_fare[0.25] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[0.5]), other=1, inplace=True)
	train_data.Fare_Enc.mask((quantile_fare[0.5] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[0.75]), other=2, inplace=True)
	train_data.Fare_Enc.mask((quantile_fare[0.75] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[1.0]), other=3, inplace=True)

	print("Quantile Age:\n", quantile_age)
	print("Quantile Fare:\n", quantile_fare)

	train_data_Enc = train_data[features].astype(np.int)




def restore_data(train_data, test_data):
	train_data = pd.read_csv(train_file_path)
	test_data = pd.read_csv(test_file_path)



if __name__ == "__main__":
	train_data = pd.read_csv(train_file_path)
	test_data = pd.read_csv(test_file_path)

	print("-\n--Titanic Training---\n")
	print("To restore data:\n\trestore_data(train_data, test_data)\n")
	print("List of training functions:")
	print("\tbasic_training(train_data, test_data)")
	print("\tmca(train_data, test_data)")

	print("\n\nDo not need to call function === Testing Code ===")

	train_data = pd.read_csv(train_file_path)
	test_data = pd.read_csv(test_file_path)

	features = ["Sex_Enc", "Embarked_Enc", "Age_Enc", "Fare_Enc"]
	features_testing = ["Age", "Age_Enc", "Fare", "Fare_Enc"]


	train_data["Sex_Enc"] = train_data["Sex"].replace({"male":0,"female":1})
	train_data.Sex_Enc.fillna(train_data.Sex_Enc.median(), inplace=True)

	train_data["Embarked_Enc"] = train_data["Embarked"].replace({"S":0,"C":1, "Q":2})
	train_data.Embarked_Enc.fillna(train_data.Embarked_Enc.median(), inplace=True)

	train_data["Age_Enc"] = train_data.Age.fillna(train_data.Age.median())

	train_data["Fare_Enc"] = train_data.Fare.fillna(train_data.Fare.median())

	quantile_age = train_data.Age.quantile([.0, 0.25, 0.5, 0.75, 1.])

	train_data.Age_Enc.mask((quantile_age[.0] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[0.25]), other=0, inplace=True)
	train_data.Age_Enc.mask((quantile_age[0.25] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[0.5]), other=1, inplace=True)
	train_data.Age_Enc.mask((quantile_age[0.5] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[0.75]), other=2, inplace=True)
	train_data.Age_Enc.mask((quantile_age[0.75] <= train_data.Age_Enc) & (train_data.Age_Enc <= quantile_age[1.0]), other=3, inplace=True)

	quantile_fare = train_data.Fare.quantile([.0, 0.25, 0.5, 0.75, 1.])

	train_data.Fare_Enc.mask((quantile_fare[.0] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[0.25]), other=0, inplace=True)
	train_data.Fare_Enc.mask((quantile_fare[0.25] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[0.5]), other=1, inplace=True)
	train_data.Fare_Enc.mask((quantile_fare[0.5] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[0.75]), other=2, inplace=True)
	train_data.Fare_Enc.mask((quantile_fare[0.75] <= train_data.Fare_Enc) & (train_data.Fare_Enc <= quantile_fare[1.0]), other=3, inplace=True)

	print("Quantile Age:\n", quantile_age)
	print("Quantile Fare:\n", quantile_fare)

	train_data_Enc = train_data[features].astype(np.int)

	CDT = pd.DataFrame([
		train_data.Sex_Enc.astype(np.int) == 0,
		train_data.Sex_Enc.astype(np.int) == 1,

		train_data.Embarked_Enc.astype(np.int) == 0,
		train_data.Embarked_Enc.astype(np.int) == 1,
		train_data.Embarked_Enc.astype(np.int) == 2,

		train_data.Age_Enc.astype(np.int) == 0,
		train_data.Age_Enc.astype(np.int) == 1,
		train_data.Age_Enc.astype(np.int) == 2,
		train_data.Age_Enc.astype(np.int) == 3,

		train_data.Fare_Enc.astype(np.int) == 0,
		train_data.Fare_Enc.astype(np.int) == 1,
		train_data.Fare_Enc.astype(np.int) == 2,
		train_data.Fare_Enc.astype(np.int) == 3,
	])

