# Integration with Machine Learning Libraries

NumPy is extensively used in machine learning workflows. This guide covers how to use NumPy arrays with popular machine learning libraries, including data preprocessing and feeding arrays into models.

## Preprocessing Data for Machine Learning Tasks

Preprocessing is a crucial step in preparing data for machine learning tasks. NumPy arrays can be used to perform various preprocessing techniques.

### Example: Normalizing Data

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create sample data
data = np.random.rand(100, 5)

# Normalize data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data)

print(normalized_data)
```

### Example: Handling Missing Values

```python
import numpy as np
from sklearn.impute import SimpleImputer

# Create sample data with missing values
data = np.array([[1, 2], [np.nan, 3], [7, 6]])

# Handle missing values
imputer = SimpleImputer(strategy='mean')
imputed_data = imputer.fit_transform(data)

print(imputed_data)
```

## Using NumPy Arrays with Machine Learning Libraries

### scikit-learn

scikit-learn is a powerful library for machine learning that integrates well with NumPy for data manipulation and model training.

#### Example: Training a Simple Model

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Create sample data
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# Train a linear regression model
model = LinearRegression().fit(X, y)

# Print model parameters
print(f"Model coefficients: {model.coef_}")
print(f"Model intercept: {model.intercept_}")
```


## Feeding NumPy Arrays into Machine Learning Models

NumPy arrays are commonly used to feed data into machine learning models.

### Example: Training a Classifier

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print(f"Model accuracy: {accuracy}")
```

---