import shap
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

data = load_iris()
X = data.data
y = data.target
feature_names = data.feature_names
class_names = data.target_names  # ['setosa', 'versicolor', 'virginica']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)

# Colors for classes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

for class_idx in range(3):
    plt.figure()
    plt.title(f"Class {class_idx} - {class_names[class_idx].capitalize()} Feature Importance")
    shap.summary_plot(
        shap_values.values[:, :, class_idx],
        features=X_test,
        feature_names=feature_names,
        plot_type="bar",
        color=colors[class_idx],
        show=True
    )

# 4. Combined horizontal stacked bar plot
# Average absolute SHAP values per class
mean_abs_shap_per_class = np.mean(np.abs(shap_values.values), axis=0)

# Horizontal stacked bars
plt.figure(figsize=(8,5))
bottom = np.zeros(len(feature_names))
for i in range(3):
    plt.barh(feature_names, mean_abs_shap_per_class[:, i], left=bottom, color=colors[i], label=class_names[i].capitalize())
    bottom += mean_abs_shap_per_class[:, i]

plt.xlabel("Mean |SHAP value|")
plt.title("Combined Feature Importance Across All Classes")
plt.legend()
plt.tight_layout()
plt.show()
