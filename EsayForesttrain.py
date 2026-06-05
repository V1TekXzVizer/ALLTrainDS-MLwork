from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
import matplotlib.pyplot as plt

data = load_iris()
X = data.data
y = data.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train) 

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Размер обучающей выборки: {X_train.shape}")
print(f"Размер тестовой выборки: {X_test.shape}")

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
ax[0].bar(data.feature_names, model.feature_importances_)
ax[0].set_title("Feature Importances")
ax[0].set_xticklabels(data.feature_names, rotation=45)
ax[0].set_ylabel("Importance")

train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

ax[1].bar(["Train", "Test"], [train_acc, test_acc])
ax[1].set_title("Model Accuracy")
ax[1].set_ylabel("Accuracy")

plt.tight_layout()
plt.show()