def predict_next(model, latest_row):
    features = latest_row[['1. open', '2. high', '3. low', '5. volume']].values.reshape(1, -1)
    return model.predict(features)[0]
