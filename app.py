import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title('Simple Linear Regression with CRISP-DM')

# 1. Business Understanding
st.header('1. Business Understanding')
st.write("""
This web application provides an interactive environment for understanding simple linear regression.
Users can adjust parameters to see how they affect the data and the regression model.
This follows the CRISP-DM methodology.
""")

# 2. Data Understanding
st.header('2. Data Understanding')
st.write("We'll generate synthetic data based on the equation `y = ax + b + noise`.")

# 3. Data Preparation
st.header('3. Data Preparation')
st.write("Use the sliders below to modify the data generation parameters.")

# User-configurable parameters
a = st.slider('Slope (a)', -10.0, 10.0, 2.5, 0.1)
num_points = st.slider('Number of points', 10, 500, 100, 10)
noise_level = st.slider('Noise level', 0.0, 10.0, 2.0, 0.1)
b = 5 # Fixed intercept for simplicity

# Data generation function
def generate_data(a, b, num_points, noise_level):
    X = np.linspace(0, 10, num_points).reshape(-1, 1)
    y = a * X.squeeze() + b + np.random.normal(0, noise_level, num_points)
    return X, y

X, y = generate_data(a, b, num_points, noise_level)

# 4. Modeling
st.header('4. Modeling')
st.write("We'll use scikit-learn's `LinearRegression` model to find the best-fit line for the data.")

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 5. Evaluation
st.header('5. Evaluation')
st.write("The model's performance is evaluated through visualization and metrics.")

fig, ax = plt.subplots()
ax.scatter(X, y, label='Generated Data')
ax.plot(X, y_pred, color='red', label='Regression Line')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.legend()
st.pyplot(fig)

st.write(f"**Model Parameters:**")
st.write(f"  - Slope (Coefficient): `{model.coef_[0]:.2f}`")
st.write(f"  - Intercept: `{model.intercept_:.2f}`")

r_squared = model.score(X, y)
st.write(f"**Model Fit:**")
st.write(f"  - R-squared: `{r_squared:.2f}`")

# 6. Deployment
st.header('6. Deployment')
st.write("""
This application is deployed as a Streamlit web app. 
To run this application locally, you would use the command: `streamlit run app.py`
""")
