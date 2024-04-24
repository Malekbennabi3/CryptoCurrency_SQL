import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Load your timeseries data as a pandas DataFrame
data = pd.read_csv("../Data/ETTh1.csv")

# Define the target variable (what you want to predict)
target_variable = "value"  # Replace with your actual target column name

# Split data into training and testing sets
train_data = data[:-1]
test_data = data[-1:]

# Scale the data (optional, but recommended for better training)
scaler = MinMaxScaler(feature_range=(0, 1))  # Create a MinMaxScaler object
scaled_train_data = scaler.fit_transform(train_data[[target_variable]])
scaled_test_data = scaler.transform(test_data[[target_variable]])

# Create sequences for LSTM model (past values to predict the next)
look_back = 30  # Number of past values to consider for prediction


def create_sequences(data, target, look_back):
    sequences = []
    for i in range(len(data) - look_back - 1):
        x = data[i:(i + look_back)]
        y = target[i + look_back]
        sequences.append([x, y])
    return np.array(sequences)


train_sequences = create_sequences(scaled_train_data, scaled_train_data[:, 0], look_back)
test_sequences = create_sequences(scaled_test_data, scaled_test_data[:, 0], look_back)

# Separate features and target for training data
X_train, y_train = train_sequences[:, :-1], train_sequences[:, -1]

# Define and train the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))  # First LSTM layer with 50 units
model.add(LSTM(50))  # Second LSTM layer with 50 units
model.add(Dense(1))  # Output layer with 1 unit for single value prediction
model.compile(loss="mae", optimizer="adam")  # Mean Absolute Error loss and Adam optimizer
model.fit(X_train, y_train, epochs=100, batch_size=32)  # Train for 100 epochs with batch size of 32

# Make predictions on the test data
predicted_scaled = model.predict(test_sequences)

# Invert scaling for actual prediction values
predicted = scaler.inverse_transform(predicted_scaled)[:, 0]

# Calculate MAE on the test data (assuming 'actual' is the actual target value in test_data)
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(test_data[target_variable].values[1:], predicted)
print(f"MAE on test data: {mae:.2f}")  # Format MAE to two decimal places
