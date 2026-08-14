from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit([[1], [2], [3]], [2, 4, 6])

prediction = model.predict([[4]])
print("Prediction:", prediction[0])
