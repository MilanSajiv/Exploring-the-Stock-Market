import yfinance as yf
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Fetch historical stock data
def fetch_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")

# Prepare the data for LSTM
def prepare_data(stock_data):
    prices = stock_data['Close'].values.reshape(-1, 1)

    # Scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(prices)

    return scaled_prices, scaler

# Split data into training and testing sets
def split_data(data):
    train_size = int(len(data) * 0.8)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

# Create the LSTM model
def build_model():
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape=(1, 1)))
    model.add(LSTM(64))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Train the LSTM model
def train_model(model, train_data):
    X_train, y_train = train_data[:-1], train_data[1:]
    X_train = np.reshape(X_train, (X_train.shape[0], 1, 1))
    model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=2)

# Predict the future stock prices
def predict_stock_prices(model, test_data, scaler):
    X_test = np.reshape(test_data, (test_data.shape[0], 1, 1))
    predicted_prices = model.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted_prices)
    return predicted_prices

# Plot the actual and predicted stock prices
def plot_predictions(actual_prices, predicted_prices):
    plt.plot(actual_prices, label='Actual')
    plt.plot(predicted_prices, label='Predicted')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.show()

# Set the stock symbol, start date, and end date
symbol = input("Enter the stock symbol (e.g., AAPL): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Fetch stock data
stock_data = fetch_stock_data(symbol, start_date, end_date)

# Prepare the data
scaled_prices, scaler = prepare_data(stock_data)

# Split the data into training and testing sets
train_data, test_data = split_data(scaled_prices)

# Build and train the LSTM model
model = build_model()
train_model(model, train_data)

# Predict the future stock prices
predicted_prices = predict_stock_prices(model, test_data, scaler)

# Plot the predictions
plot_predictions(stock_data['Close'].values, predicted_prices)