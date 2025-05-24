import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/cleaned_stress_data_modeling.csv")

# Define features and target
X = df.drop(columns=["Stress_Level"])
y = df["Stress_Level"]

# Separate numeric and categorical features
numeric_features = ["Age", "Sleep_Hours", "Work_Hours", "Physical_Activity_Hours"]
categorical_features = [col for col in X.columns if col not in numeric_features]

# Preprocessing
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(drop="first"), categorical_features)
])

# Create pipeline with Logistic Regression
model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train and evaluate
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print metrics
print(classification_report(y_test, y_pred))

# Show confusion matrix
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Logistic Regression - Confusion Matrix")
plt.tight_layout()
plt.show()
