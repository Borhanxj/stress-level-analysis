import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned_stress_data_modeling.csv")

# Define features and label
X = df.drop(columns=["Stress_Level"])
y = df["Stress_Level"]

# Separate numeric and categorical columns
numeric_features = ["Age", "Sleep_Hours", "Work_Hours", "Physical_Activity_Hours"]
categorical_features = [col for col in X.columns if col not in numeric_features]

# Create preprocessing pipeline
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(drop="first"), categorical_features)
])

# Create full modeling pipeline
model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", DecisionTreeClassifier(random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Fit model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Confusion matrix plot
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Decision Tree - Confusion Matrix")
plt.tight_layout()
plt.show()
