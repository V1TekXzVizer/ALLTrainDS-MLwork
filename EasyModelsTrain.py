import matplotlib.pyplot as plt
import numpy as np 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier 

data = load_iris()
X = data.data
y = data.target 
feature_names = data.feature_names
target_names = data.target_names 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = {
    'Дерево решений': DecisionTreeClassifier(random_state=42),
    'K- ближайших соседий': KNeighborsClassifier(n_neighbors=3),
    'Логистическая регрессия': LogisticRegression(random_state=42, max_iter=200),
    'Случайный лес': RandomForestClassifier(n_estimators=10, random_state=42)
}

results = {}
train_scores = {}
test_scores = {}

for name, clf in model.items():
    clf.fit(X_train, y_train) 
    y_train_pred = clf.predict(X_train)
    y_test_pred = clf.predict(X_test)
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)
    train_scores[name] = train_acc
    test_scores[name] = test_acc 
    results[name] = clf
    
    print(f"Лучшая модель: {name}")
    print(f"  Точность на обучающей выборке: {train_acc:.4f}")
    print(f"  Точность на тестовой выборке: {test_acc:.4f}")
    print(f"  Разница: {train_acc - test_acc:.4f}")
    
print("Лучшая модель по точности")
print("=" * 50)

best_model_name = max(test_scores, key=test_scores.get)
best_model_score = test_scores[best_model_name]

print(f"Лучшая модель: {best_model_name}")
print(f"Точность: {best_model_score:.4f}")

print("Визуализация результатов")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

models_names = [name.replace("\n", " ") for name in model.keys()]
x = np.arange(len(models_names))
width = 0.35

axes[0, 0].bar(x - width/2, [train_scores[name] for name in models_names], width, label="Train", color="skyblue", alpha=0.8)
axes[0, 0].bar(x + width/2, [test_scores[name] for name in models_names], width, label="Test", color="lightcoral", alpha=0.8)
axes[0, 0].set_xlabel("Models")
axes[0, 0].set_ylabel("Accuracy")
axes[0, 0].set_title("Model Comparison")
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(models_names, rotation=45, ha="right")
axes[0, 0].legend()
axes[0, 0].set_ylim(0, 1.05)
axes[0, 0].grid(True, alpha=0.3)

overfitting = [train_scores[name] - test_scores[name] for name in model.keys()]
colors = ["green" if diff < 0.05 else "orange" if diff < 0.1 else "red" for diff in overfitting]
axes[0, 1].bar(models_names, overfitting, color=colors, alpha=0.8)
axes[0, 1].set_xlabel("Models")
axes[0, 1].set_ylabel("Difference")
axes[0, 1].set_title("Overfitting")
axes[0, 1].axhline(y=0.05, color="green", linestyle="--", alpha=0.5, label="Good(<5%)")
axes[0, 1].axhline(y=0.1, color="orange", linestyle="--", alpha=0.5, label="Moderate(<10%)")
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
plt.setp(axes[0, 1].xaxis.get_majorticklabels(), rotation=45, ha="right")

best_model = results[best_model_name]
best_model.fit(X_train, y_train)
y_best_pred = best_model.predict(X_test)

if hasattr(best_model, 'feature_importances_'):
    importances = best_model.feature_importances_
    axes[1, 0].barh(feature_names, importances, color="green", alpha=0.7)
    axes[1, 0].set_xlabel("Importance")
    axes[1, 0].set_ylabel("Features")
    axes[1, 0].set_title("Feature Importance")
    axes[1, 0].grid(True, alpha=0.3)
else:
    axes[1, 0].text(0.5, 0.5, "No feature importances", ha="center", va="center", transform=axes[1, 0].transAxes)
    axes[1, 0].set_title("No Feature Importances", fontsize=12)

correct = (y_best_pred == y_test)
axes[1, 1].pie([sum(correct), sum(~correct)], labels=[f"Good: {sum(correct)}", f"Bad: {sum(~correct)}"], autopct="%1.1f%%", explode=[0.05, 0])
axes[1, 1].set_title(f"Prediction best model: {best_model_name.split()[0]}", fontsize=12)

plt.tight_layout()
plt.show()

new_flowers = [[5.1, 3.5, 1.4, 0.2], [6.2, 2.8, 4.8, 1.8], [7.2, 3.0, 5.8, 1.6]]

best_model = results[best_model_name]
predictions = best_model.predict(new_flowers)

for i, flower in enumerate(new_flowers):
    print(f"\n flower: {flower}")
    print(f"Predicted: {target_names[predictions[i]]}")