
# Integration with Deep Learning Libraries

NumPy arrays are fundamental in deep learning workflows. This guide explores how to work with NumPy arrays in deep learning frameworks, including conversion to tensors and integration into neural network architectures.

## Working with NumPy Arrays in Deep Learning Frameworks

### TensorFlow

TensorFlow is a popular deep learning framework that supports operations on tensors. NumPy arrays can be easily converted to TensorFlow tensors.

#### Example: Converting NumPy Arrays to TensorFlow Tensors

```python
import numpy as np
import tensorflow as tf

# Create a NumPy array
np_array = np.array([1.0, 2.0, 3.0])

# Convert to a TensorFlow tensor
tf_tensor = tf.convert_to_tensor(np_array)

print(tf_tensor)
```

### PyTorch

PyTorch is another widely-used deep learning framework that integrates seamlessly with NumPy.NumPy arrays can be converted to tensors in PyTorch to facilitate neural network training and other operations.

#### Example: Converting NumPy Arrays to PyTorch Tensors

```python
import numpy as np
import torch

# Create a NumPy array
np_array = np.array([1.0, 2.0, 3.0])

# Convert to a PyTorch tensor
torch_tensor = torch.tensor(np_array)

print(torch_tensor)
```


## Incorporating NumPy Arrays into Neural Network Architectures

### Example: Using NumPy Arrays in TensorFlow Model

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create sample data
X = np.random.rand(100, 10)
y = np.random.randint(2, size=100)

# Define a simple model
model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10)
```

### Example: Using NumPy Arrays in PyTorch Model

```python
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Create sample data
X = np.random.rand(100, 10).astype(np.float32)
y = np.random.randint(2, size=100).astype(np.float32)

# Convert to PyTorch tensors
X_tensor = torch.tensor(X)
y_tensor = torch.tensor(y)

# Define a simple model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 32)
        self.fc2 = nn.Linear(32, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

model = SimpleNN()

# Define loss and optimizer
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(10):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = criterion(outputs.squeeze(), y_tensor)
    loss.backward()
    optimizer.step()
    
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")
```
--- 