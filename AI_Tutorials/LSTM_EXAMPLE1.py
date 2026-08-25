#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 03:00:39 2026

@author: apm
"""


# ============================================================
# 1. Imports
# ============================================================

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


# ============================================================
# 2. Download Bitcoin data from CoinGecko
# ============================================================

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": 365,
    "interval": "daily"
}

response = requests.get(
    url,
    params=params,
    timeout=30
)

print("Status code:", response.status_code)

response.raise_for_status()

data = response.json()


# ============================================================
# 3. Convert prices to DataFrame
# ============================================================

df = pd.DataFrame(
    data["prices"],
    columns=["timestamp", "Close"]
)

df["Date"] = pd.to_datetime(
    df["timestamp"],
    unit="ms"
)

df = df.set_index("Date")

df = df.drop(
    columns=["timestamp"]
)

print(df.head())

'''
Date                     
2025-08-26  110100.281956
2025-08-27  111712.868681
2025-08-28  111241.292648
2025-08-29  112512.680983
2025-08-30  108335.633152


'''



print(df.tail())

print("Number of observations:", len(df))
#Number of observations: 366




# ============================================================
# 4. Plot historical Bitcoin price
# ============================================================

plt.figure(figsize=(14, 6))

plt.plot(
    df.index,
    df["Close"]
)

plt.title(
    "Bitcoin Historical Closing Price"
)

plt.xlabel("Date")
plt.ylabel("BTC Price (USD)")

plt.grid(alpha=0.3)

plt.show()


# ============================================================
# 5. Extract the Close column
# ============================================================

close = df["Close"].copy()

close = close.dropna()

print(close.head())

print("Shape:", close.shape)

#Shape: (366,)



# ============================================================
# 6. Convert to NumPy
# ============================================================

data_values = close.values.reshape(-1, 1)

print("Original data shape:", data_values.shape)

#Original data shape: (366, 1)



# ============================================================
# 7. Parameters
# ============================================================

SEQUENCE_LENGTH = 60 #60 toze ghabl ro bebine

FORECAST_DAYS = 7 #7 roze yanade , done done pishbini

#1 rooz ro mikham 

BATCH_SIZE = 32

EPOCHS = 50


# ============================================================
# 8. Train/Test split
# ============================================================

train_size = int(
    len(data_values) * 0.80
)

print("Total number of days:", len(data_values))

print("Training days:", train_size)

print(
    "Testing days:",
    len(data_values) - train_size
)
'''
Total number of days: 366
Training days: 292
Testing days: 74


shuffle nemikonam 



'''

# ============================================================
# 9. Normalize data
# ============================================================

scaler = MinMaxScaler(
    feature_range=(0, 1)
)

# IMPORTANT:
# Fit scaler ONLY on training data

scaler.fit(
    data_values[:train_size]
)

scaled_data = scaler.transform(
    data_values
)


print("First scaled values:")

print(
    scaled_data[:5]
)

'''
First scaled values:
[[0.77084401]
 [0.79608621]
 [0.78870452]
 [0.80860586]
 [0.74322155]]

'''

# ============================================================
# 10. Create sequences
# ============================================================
'''

time   price






x1 x2 x3 x4 ... x60     y1 y2 y.. y7





'''
def create_sequences(
    data,
    sequence_length,
    forecast_days
):

    X = []
    y = []

    for i in range(
        len(data)
        - sequence_length
        - forecast_days
        + 1
    ):

        # --------------------------------
        # Input:
        # Previous 60 days
        # --------------------------------

        input_sequence = data[
            i:
            i + sequence_length
        ]

        # --------------------------------
        # Target:
        # Next 7 days
        # --------------------------------

        target_sequence = data[
            i + sequence_length:
            i + sequence_length + forecast_days
        ]

        X.append(
            input_sequence
        )

        y.append(
            target_sequence.flatten()
        )

    return (
        np.array(X),
        np.array(y)
    )


X, y = create_sequences(
    scaled_data,
    SEQUENCE_LENGTH,
    FORECAST_DAYS
)


print("X shape:", X.shape)

print("y shape:", y.shape)

#X shape: (300, 60, 1)
#y shape: (300, 7)




# ============================================================
# 11. Split sequences into training and testing
# ============================================================

train_samples = (
    train_size
    - SEQUENCE_LENGTH
    - FORECAST_DAYS
    + 1
)

print(
    "Training sequence samples:",
    train_samples
)


X_train = X[
    :train_samples
]

y_train = y[
    :train_samples
]


X_test = X[
    train_samples:
]

y_test = y[
    train_samples:
]


print(
    "X_train:",
    X_train.shape
)

print(
    "y_train:",
    y_train.shape
)

print(
    "X_test:",
    X_test.shape
)

print(
    "y_test:",
    y_test.shape
)

'''
Training sequence samples: 226
X_train: (226, 60, 1)
y_train: (226, 7)



74 ta test daram

X_test: (74, 60, 1)
y_test: (74, 7)

'''
# ============================================================
# 12. Convert to PyTorch tensors
# ============================================================

X_train = torch.tensor(
    X_train,
    dtype=torch.float32
)

y_train = torch.tensor(
    y_train,
    dtype=torch.float32
)

X_test = torch.tensor(
    X_test,
    dtype=torch.float32
)

y_test = torch.tensor(
    y_test,
    dtype=torch.float32
)


print(
    "PyTorch X_train shape:",
    X_train.shape
)

print(
    "PyTorch y_train shape:",
    y_train.shape
)


# ============================================================
# 13. Create DataLoader
# ============================================================

train_dataset = TensorDataset(
    X_train,
    y_train
)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)


# ============================================================
# 14. Select device
# ============================================================

if torch.cuda.is_available():

    device = torch.device(
        "cuda"
    )

elif torch.backends.mps.is_available():

    device = torch.device(
        "mps"
    )

else:

    device = torch.device(
        "cpu"
    )


print(
    "Using device:",
    device
)


#Using device: mps




# ============================================================
# 15. Define LSTM model
# ============================================================

class BitcoinLSTM(nn.Module):

    def __init__(
        self,
        input_size=1,
        hidden_size=32,
        num_layers=1,
        forecast_days=7
    ):

        super().__init__()

        # ----------------------------------
        # LSTM
        # ----------------------------------

        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2
        )

        # ----------------------------------
        # Fully connected output layer
        # ----------------------------------

        self.fc = nn.Linear(
            hidden_size,
            forecast_days
        )


    def forward(self, x):

        # x shape:
        #
        # (batch_size,
        #  sequence_length,
        #  features)
        #
        # Example:
        #
        # (32, 60, 1)


        output, (
            hidden_state,
            cell_state
        ) = self.lstm(x)


        # output shape:
        #
        # (batch_size,
        #  sequence_length,
        #  hidden_size)
        #
        # Example:
        #
        # (32, 60, 64)


        # We only take the output
        # of the LAST timestep

        last_output = output[
            :,
            -1,
            :
        ]


        # last_output shape:
        #
        # (batch_size, hidden_size)
        #
        # Example:
        #
        # (32, 64)


        prediction = self.fc(
            last_output
        )


        # prediction shape:
        #
        # (batch_size, 7)

        return prediction


# ============================================================
# 16. Create model
# ============================================================

model = BitcoinLSTM(
    input_size=1,
    hidden_size=32,
    num_layers=1,
    forecast_days=FORECAST_DAYS
)


model = model.to(
    device
)


print(model)






#-------balaei ya paeini

model = BitcoinLSTM(
    input_size=1,
    hidden_size=128,
    num_layers=1,
    forecast_days=FORECAST_DAYS
)


model = model.to(
    device
)


print(model)




'''
60 previous Bitcoin prices

        ↓

LSTM
hidden_size = 64

        ↓

LSTM
hidden_size = 64

        ↓

Last LSTM output

        ↓

Linear
64 → 7

        ↓

Day +1
Day +2
Day +3
Day +4
Day +5
Day +6
Day +7

'''




# ============================================================
# 17. Loss function and optimizer
# ============================================================

criterion = nn.MSELoss()


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# ============================================================
# 18. Training
# ============================================================

loss_history = []


for epoch in range(EPOCHS):

    model.train()

    total_loss = 0


    for (
        X_batch,
        y_batch
    ) in train_loader:


        # Move batch to device

        X_batch = X_batch.to(
            device
        )

        y_batch = y_batch.to(
            device
        )


        # ----------------------------------
        # Forward propagation
        # ----------------------------------

        predictions = model(
            X_batch
        )


        # ----------------------------------
        # Calculate loss
        # ----------------------------------

        loss = criterion(
            predictions,
            y_batch
        )


        # ----------------------------------
        # Clear old gradients
        # ----------------------------------

        optimizer.zero_grad()


        # ----------------------------------
        # Backpropagation
        # ----------------------------------

        loss.backward()


        # ----------------------------------
        # Gradient clipping
        #
        # Useful for recurrent networks
        # ----------------------------------

        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )


        # ----------------------------------
        # Update weights
        # ----------------------------------

        optimizer.step()


        total_loss += (
            loss.item()
        )


    average_loss = (
        total_loss
        /
        len(train_loader)
    )


    loss_history.append(
        average_loss
    )


    if (
        epoch + 1
    ) % 5 == 0:

        print(
            f"Epoch "
            f"{epoch + 1}/{EPOCHS} "
            f"| Loss: "
            f"{average_loss:.6f}"
        )



'''
hidden tsate 32 size
Epoch 5/50 | Loss: 0.031460
Epoch 10/50 | Loss: 0.023826
Epoch 15/50 | Loss: 0.014106
Epoch 20/50 | Loss: 0.008863
Epoch 25/50 | Loss: 0.008442
Epoch 30/50 | Loss: 0.006953
Epoch 35/50 | Loss: 0.006485
Epoch 40/50 | Loss: 0.006449
Epoch 45/50 | Loss: 0.009601
Epoch 50/50 | Loss: 0.005505




hiden stioze 128 
Epoch 10/50 | Loss: 0.011127
Epoch 15/50 | Loss: 0.006754
Epoch 20/50 | Loss: 0.005803
Epoch 25/50 | Loss: 0.004913
Epoch 30/50 | Loss: 0.006470
Epoch 35/50 | Loss: 0.004804
Epoch 40/50 | Loss: 0.005364
Epoch 45/50 | Loss: 0.007340
Epoch 50/50 | Loss: 0.004959

'''



# ============================================================
# 19. Plot training loss
# ============================================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    loss_history
)

plt.title(
    "LSTM Training Loss"
)

plt.xlabel(
    "Epoch"
)

plt.ylabel(
    "MSE Loss"
)

plt.grid(
    alpha=0.3
)

plt.show()








# ============================================================
# 20. Evaluate on test data
# ============================================================

model.eval()


with torch.no_grad():

    test_predictions = model(
        X_test.to(device)
    )


# Move back to CPU

test_predictions = (
    test_predictions
    .cpu()
    .numpy()
)


actual_test = (
    y_test
    .cpu()
    .numpy()
)


print(
    "Predictions shape:",
    test_predictions.shape
)

print(
    "Actual shape:",
    actual_test.shape
)
'''
Predictions shape: (74, 7)
Actual shape: (74, 7)

'''




# ============================================================
# 21. Convert predictions back to USD
# ============================================================

predicted_prices = (
    scaler.inverse_transform(
        test_predictions.reshape(
            -1,
            1
        )
    )
    .reshape(
        test_predictions.shape
    )
)


actual_prices = (
    scaler.inverse_transform(
        actual_test.reshape(
            -1,
            1
        )
    )
    .reshape(
        actual_test.shape
    )
)


print(
    "First predicted 7 days:"
)

print(
    predicted_prices[0]
)


print(
    "\nActual 7 days:"
)

print(
    actual_prices[0]
)


'''
First predicted 7 days:
[68377.35  69052.88  68587.5   69144.27  69016.164 69123.56  68947.336]

Actual 7 days:
[63273.54  63069.15  61669.76  61480.145 63555.66  63532.277 64408.81 ]


'''


# ============================================================
# 22. Metrics
# ============================================================

mae = mean_absolute_error(
    actual_prices.flatten(),
    predicted_prices.flatten()
)


rmse = np.sqrt(
    mean_squared_error(
        actual_prices.flatten(),
        predicted_prices.flatten()
    )
)


print(
    f"MAE: "
    f"${mae:,.2f}"
)

print(
    f"RMSE: "
    f"${rmse:,.2f}"
)

'''
MAE: $4,314.45
RMSE: $4,724.36





MAE: $2,899.40
RMSE: $3,697.14

'''





# ============================================================
# 23. Actual vs predicted
# ============================================================

actual_day1 = (
    actual_prices[
        :,
        0
    ]
)


predicted_day1 = (
    predicted_prices[
        :,
        0
    ]
)


plt.figure(
    figsize=(14, 6)
)


plt.plot(
    actual_day1,
    label="Actual BTC Price"
)


plt.plot(
    predicted_day1,
    label="Predicted BTC Price"
)


plt.title(
    "Bitcoin LSTM Prediction "
    "on Test Data"
)


plt.xlabel(
    "Test Sequence"
)

plt.ylabel(
    "BTC Price (USD)"
)


plt.legend()

plt.grid(
    alpha=0.3
)

plt.show()







# ============================================================
# 24. Show one 7-day example
# ============================================================

example = 10


print(
    "Actual:"
)

for day, price in enumerate(
    actual_prices[example],
    start=1
):

    print(
        f"Day +{day}: "
        f"${price:,.2f}"
    )

'''
Actual:
Day +1: $64,444.54
Day +2: $62,897.24
Day +3: $63,489.81
Day +4: $64,253.40
Day +5: $63,255.49
Day +6: $63,937.29
Day +7: $62,662.29

'''

print(
    "\nPredicted:"
)

for day, price in enumerate(
    predicted_prices[example],
    start=1
):

    print(
        f"Day +{day}: "
        f"${price:,.2f}"
    )


'''
Predicted:
Day +1: $67,508.55
Day +2: $68,421.84
Day +3: $68,165.20
Day +4: $68,342.84
Day +5: $68,310.78
Day +6: $67,656.12
Day +7: $68,529.81

'''



# ============================================================
# 25. Plot one 7-day forecast
# ============================================================

days = np.arange(
    1,
    FORECAST_DAYS + 1
)


plt.figure(
    figsize=(10, 5)
)


plt.plot(
    days,
    actual_prices[example],
    marker="o",
    label="Actual"
)


plt.plot(
    days,
    predicted_prices[example],
    marker="o",
    label="Predicted"
)


plt.xticks(
    days
)


plt.xlabel(
    "Days into Future"
)

plt.ylabel(
    "BTC Price (USD)"
)


plt.title(
    "LSTM 7-Day Bitcoin Prediction"
)


plt.legend()

plt.grid(
    alpha=0.3
)

plt.show()
