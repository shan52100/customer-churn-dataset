import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load Dataset
dataset_url = "C:\project\projectcustomerchrun\churn_project\churn_api\data\customer_churn.csv"
data = pd.read_csv(dataset_url)

# Preprocessing
data.drop(['CustomerID'], axis=1, inplace=True)
data = pd.get_dummies(data, drop_first=True)

X = data.drop('Churn', axis=1).values
y = data['Churn'].values

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build ANN Model
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))

def predict_churn(features):
    input_data = np.array(features).reshape(1, -1)
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    return float(prediction[0][0])