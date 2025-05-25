from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

def train_model(df):
    df = df.copy()
    df['Target'] = df['4. close'].shift(-1)
    df.dropna(inplace=True)
    X = df[['1. open', '2. high', '3. low', '5. volume']]
    y = df['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model
