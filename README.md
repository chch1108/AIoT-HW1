# Interactive Simple Linear Regression Visualizer

This project is a web-based application that provides an interactive environment for understanding and visualizing simple linear regression. Users can adjust various parameters to see how they affect the data and the resulting regression model. The application is built using Python and Streamlit, and it follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.

## Features

*   **Interactive Controls:** Users can modify the slope of the line, the number of data points, and the level of noise in the data.
*   **Real-time Visualization:** The application instantly updates the scatter plot of the data and the regression line based on the user's input.
*   **Model Evaluation:** The calculated slope, intercept, and R-squared value of the regression model are displayed in real-time.
*   **CRISP-DM Framework:** The project is structured around the CRISP-DM methodology, providing a clear and organized approach to the problem.

## CRISP-DM Methodology

This project follows the CRISP-DM framework:

1.  **Business Understanding:** The goal is to create an educational tool for understanding simple linear regression.
2.  **Data Understanding:** Synthetic data is generated based on a linear equation with user-defined parameters.
3.  **Data Preparation:** The data is generated and prepared for modeling based on user inputs.
4.  **Modeling:** A simple linear regression model is created and trained using scikit-learn.
5.  **Evaluation:** The model is evaluated by visualizing the regression line and displaying key metrics.
6.  **Deployment:** The application is deployed as a web service using Streamlit.

## Installation

To run this project locally, you need to have Python and pip installed. Then, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd AIOT-HW1
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the following command in your terminal:

```bash
streamlit run app.py
```

This will open the application in your web browser.

## Technologies Used

*   **Python:** The core programming language.
*   **Streamlit:** For creating the web application and user interface.
*   **scikit-learn:** For building the linear regression model.
*   **NumPy:** For numerical operations and data generation.
*   **Matplotlib:** For creating the data visualizations.
