import pandas as pd

# Step 1: load dataset
df = pd.read_csv("Python/Practice/study_data.csv")

# Step 2: separate feature and label
X = df[['hours']]
y = df['marks']

# Step 3: split training and testing data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

print("Training data:")
print(X_train)
print("\nTesting data:")
print(X_test)

# Step 4: import model
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Step 5: train model
model.fit(X_train, y_train)

# Step 6: predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test.values)

# Step 7: evaluate error
from sklearn.metrics import mean_absolute_error

error = mean_absolute_error(y_test, predictions)
print("Error:", error)
