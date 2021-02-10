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
	print("Your submission was successfully saved!")

def basic_training(output=True):
	train_data = pd.read_csv(train_file_path)
	test_data = pd.read_csv(test_file_path)

	encode_data(train_data)
	encode_data(test_data)

	features = ["Sex_Enc", "Pclass", "Embarked_Enc"]

	Xy = train_data[features + ["Survived"]].dropna()

	X = Xy[features]
	y = Xy.Survived

	clf = RandomForestClassifier()

	if output:
		clf.fit(X, y)

		X_test = test_data[features]

		output_submission(test_data, clf.predict(X_test))
	else:
		print("Test Score:\n", cross_validate(clf, X, y)["test_score"])


def get_CDT(data, quantile_age, quantile_fare):
	features = ["Sex_Enc", "Embarked_Enc", "Age_Enc", "Fare_Enc"]

	data["Sex_Enc"] = data["Sex"].replace({"male":0,"female":1})
	data.Sex_Enc.fillna(data.Sex_Enc.median(), inplace=True)

	data["Embarked_Enc"] = data["Embarked"].replace({"S":0,"C":1, "Q":2})
	data.Embarked_Enc.fillna(data.Embarked_Enc.median(), inplace=True)

	data["Age_Enc"] = data.Age.fillna(data.Age.median())

	data["Fare_Enc"] = data.Fare.fillna(data.Fare.median())

	data.Age_Enc.mask((quantile_age[.0] <= data.Age_Enc) & (data.Age_Enc <= quantile_age[0.25]), other=0, inplace=True)
	data.Age_Enc.mask((quantile_age[0.25] <= data.Age_Enc) & (data.Age_Enc <= quantile_age[0.5]), other=1, inplace=True)
	data.Age_Enc.mask((quantile_age[0.5] <= data.Age_Enc) & (data.Age_Enc <= quantile_age[0.75]), other=2, inplace=True)
	data.Age_Enc.mask((quantile_age[0.75] <= data.Age_Enc) & (data.Age_Enc <= quantile_age[1.0]), other=3, inplace=True)

	data.Fare_Enc.mask((quantile_fare[.0] <= data.Fare_Enc) & (data.Fare_Enc <= quantile_fare[0.25]), other=0, inplace=True)
	data.Fare_Enc.mask((quantile_fare[0.25] <= data.Fare_Enc) & (data.Fare_Enc <= quantile_fare[0.5]), other=1, inplace=True)
	data.Fare_Enc.mask((quantile_fare[0.5] <= data.Fare_Enc) & (data.Fare_Enc <= quantile_fare[0.75]), other=2, inplace=True)
	data.Fare_Enc.mask((quantile_fare[0.75] <= data.Fare_Enc) & (data.Fare_Enc <= quantile_fare[1.0]), other=3, inplace=True)

	train_data_Enc = data[features].astype(np.int)

	columns = [	"Sex_0", "Sex_1",
				"Embarked_0", "Embarked_1", "Embarked_2",
				"Age_0", "Age_1", "Age_2", "Age_3",
				"Fare_0", "Fare_1", "Fare_2", "Fare_3",]

	CDT = pd.DataFrame([
		data.Sex_Enc.astype(np.int) == 0,
		data.Sex_Enc.astype(np.int) == 1,

		data.Embarked_Enc.astype(np.int) == 0,
		data.Embarked_Enc.astype(np.int) == 1,
		data.Embarked_Enc.astype(np.int) == 2,

		data.Age_Enc.astype(np.int) == 0,
		data.Age_Enc.astype(np.int) == 1,
		data.Age_Enc.astype(np.int) == 2,
		data.Age_Enc.astype(np.int) == 3,

		data.Fare_Enc.astype(np.int) == 0,
		data.Fare_Enc.astype(np.int) == 1,
		data.Fare_Enc.astype(np.int) == 2,
		data.Fare_Enc.astype(np.int) == 3,
		], 
		index = columns,
		dtype=np.int).T.to_numpy()

	return CDT

def mca_based_training(output=True):
	train_data = pd.read_csv(train_file_path)
	test_data = pd.read_csv(test_file_path)

	quantile_age = train_data.Age.quantile([.0, 0.25, 0.5, 0.75, 1.])
	quantile_fare = train_data.Fare.quantile([.0, 0.25, 0.5, 0.75, 1.])

	CDT_train = get_CDT(train_data, quantile_age, quantile_fare)

	F = CDT_train / CDT_train.sum()
	Fi = F.sum(axis=1).reshape((F.shape[0], 1))
	Fj = F.sum(axis=0).reshape((1, F.shape[1]))

	# CREATE X, D and M
	X = F / (Fi @ Fj) - 1
	D = np.eye(F.shape[0]) * Fi
	M = np.eye(F.shape[1]) * Fj

	# CALCULATE EIGENVALUES & EIGENVECTORS
	L, U = np.linalg.eig(X.T @ D @ X @ M)
	U = U[:, np.argsort(L)[::-1]]
	L = np.sort(L)[::-1]

	# CAUTION LITTLE CALCULUS ERROR
	L[L < 0] = L[L > 0].min()

	# CALCULATE FACTORS
	factL = np.real(X @ M @ U) # facteurs Lignes (individus)
	# factC = np.real((X.T @ D @ factL) / np.sqrt(L)) # facteurs Colonnes (variables)

	# CALCULATE HELPERS
	I = np.real(L / L.sum()) # % d'inertie
	# CtrInd = np.real((D @ factL ** 2) / L) # Contribution des individus
	# QltInd = np.real(factL **2 / (factL ** 2).sum(axis=1).reshape((F.shape[0], 1))) # Qualite de representation

	# Take 4 first factors

	X_train = factL[:,:4]
	y_train = train_data.Survived.to_numpy()

	clf = RandomForestClassifier()

	if output:
		clf.fit(X_train, y_train)

		CDT_test = get_CDT(test_data, quantile_age, quantile_fare)

		F = CDT_test / CDT_test.sum()
		Fi = F.sum(axis=1).reshape((F.shape[0], 1))
		Fj = F.sum(axis=0).reshape((1, F.shape[1]))

		# CREATE X, D and M
		X = F / (Fi @ Fj) - 1
		D = np.eye(F.shape[0]) * Fi
		M = np.eye(F.shape[1]) * Fj

		# CALCULATE EIGENVALUES & EIGENVECTORS
		L, U = np.linalg.eig(X.T @ D @ X @ M)
		U = U[:, np.argsort(L)[::-1]]
		L= np.sort(L)[::-1]

		# CAUTION LITTLE CALCULUS ERROR
		L[L < 0] = L[L > 0].min()

		# CALCULATE FACTORS
		factL = np.real(X @ M @ U) # facteurs Lignes (individus)

		X_test = factL[:,:4]
		output_submission(test_data, clf.predict(X_test))
	else:
		print("Test Score:\n", cross_validate(clf, X_train, y_train)["test_score"])


if __name__ == "__main__":
	print("-\n--Titanic Training---\n")
	print("List of training functions:")
	print("\tbasic_training()")
	print("\tmca_base_training()")