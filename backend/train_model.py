import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib, json, os

# Directory and files
data_dir = "../data"
files = ["TS1.txt", "TS2.txt", "TS3.txt", "TS4.txt", "VS1.txt", "CE.txt"]

# Read all files
dfs = [pd.read_csv(f"{data_dir}/{f}", sep="\t", header=None) for f in files]

# Reduce each sensor file to a single feature (mean across all readings)
sensor_features = [d.mean(axis=1) for d in dfs[:-1]]  # TS1–VS1

# Use CE.txt as the target condition — take first column only
condition = dfs[-1].iloc[:, 0]  # first column from CE.txt

# Combine into one DataFrame
df = pd.concat(sensor_features + [condition], axis=1)
df.columns = ["TS1", "TS2", "TS3", "TS4", "VS1", "Condition"]

# Convert Condition into binary labels (1=Healthy, 0=Fail)
y = df["Condition"].apply(lambda x: 1 if str(x).strip().lower() in ["0", "healthy", "normal"] else 0)
X = df[["TS1", "TS2", "TS3", "TS4", "VS1"]]

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and features
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
json.dump(list(X.columns), open("model/features.json", "w"))

print("✅ Model trained successfully!")
print("Features saved:", list(X.columns))
print("Shape of data:", df.shape)
