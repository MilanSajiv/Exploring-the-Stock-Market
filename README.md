# Exploring-the-Stock-Market
This repository contains Python scripts for exploring the stock market, including fetching historical stock data and predicting future stock prices using Long Short-Term Memory (LSTM) neural networks.

## Prerequisites
Before running the script, make sure you have the following libraries installed:

yfinance
numpy
pandas
tensorflow
scikit-learn
matplotlib

You can install them using pip:
pip install yfinance numpy pandas tensorflow scikit-learn matplotlib


## Stock Prediction GUI
This Python script allows users to fetch and visualize historical stock price data using the Yahoo Finance API. It provides a simple Graphical User Interface (GUI) built with tkinter for ease of use.

## Useage

1. Clone the repository to your local machine:
git clone https://github.com/MilanSajiv/Exploring-the-Stock-Market.git

2.Run the script:
python visualize_stock_data.py

3. Enter the stock symbol, start date, and end date in the respective input fields

4. Click the "Show Graph" button to fetch and display the historical stock price data

## Example
Here's a simple example of how to use the script:

Stock Symbol: AAPL
Start Date: 2020-01-01
End Date: 2022-01-01

## Stock Price Prediction
This Python script utilizes Long Short-Term Memory (LSTM) neural networks to predict future stock prices based on historical data fetched from Yahoo Finance API.

## Useage

1. Clone the repository to your local machine:
git clone https://github.com/MilanSajiv/Exploring-the-Stock-Market.git

2.Run the script:
python Predict_stock_data.py

3. Follow the prompts to enter the stock symbol, start date, and end date for which you want to predict the stock prices.

4. The script will fetch historical stock data, train an LSTM model, make predictions, and plot the actual vs. predicted stock prices.

## Example
Here's a simple example of how to use the script:

Stock Symbol: AAPL
Start Date: 2020-01-01
End Date: 2025-01-01

## License
This project is licensed under the MIT License - see the LICENSE file for details.

