# House-Price-Prediction-Web-Application

This is a machine learning-based web application built with Flask that predicts the price of a house in Pune, India, based on user-provided features like area, square footage, bedrooms, bathrooms, year built, and garage availability.

 # Project Description

This application enables users to predict house prices in Pune using a trained Random Forest Regressor. The model uses key housing features from the user and a historical dataset to provide a real-time price estimate, displayed in Indian Rupees (₹) with proper formatting.

# Features
  Predicts house prices based on:

Area / Location in Pune

Square Footage

Number of Bedrooms and Bathrooms

Year Built

Garage availability


* **Machine Learning Model**: Utilizes `scikit-learn`'s `RandomForestRegressor` for robust price prediction.
* **Data Preprocessing Pipeline**: Automatically handles missing values (imputation) and categorical features (One-Hot Encoding) using `ColumnTransformer` and `Pipeline`.
* **Web Interface (Flask)**: Provides an intuitive web form for users to input house details.
* **Dynamic Location Dropdown**: Populates the "Area" dropdown with **all** existing location entries from the dataset, ensuring the model is trained and predicts on known areas.
* **Real-time Prediction**: Calculates and displays estimated house prices upon form submission.
* **Input Validation**: Includes basic validation for user inputs to prevent common errors.
* **Indian Rupee Formatting**: Displays predicted prices in ₹ (Indian Rupee) format with appropriate comma separators.

# File Structure
'''

Okay, here is the content for your README.md file, formatted so you can easily save it. This file provides comprehensive documentation for your Pune House Price Prediction Web Application, including the features we've implemented like the full-page background, the house image, and the corner text.

You should save this content as README.md in the root directory of your project.

README.md
Markdown

# Pune House Price Prediction Web Application

This project implements a machine learning model to predict house prices in Pune, India, and exposes this functionality via a user-friendly web interface built with Flask.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Model Details](#model-details)
- [Area/Location Handling](#arealocation-handling)
- [Customization (Visuals & Text)](#customization-visuals--text)
- [Error Handling](#error-handling)
- [License](#license)

## Project Description

This application uses a Random Forest Regressor model to estimate house prices based on various features such as area, square footage, number of bedrooms, bathrooms, year built, and presence of a garage. The model is trained on a provided dataset (`pune_house_prices.csv`) and served through a local web server, allowing users to input house specifications and receive an instant price prediction.

## Features

* **Machine Learning Model**: Utilizes `scikit-learn`'s `RandomForestRegressor` for robust price prediction.
* **Data Preprocessing Pipeline**: Automatically handles missing values (imputation) and categorical features (One-Hot Encoding) using `ColumnTransformer` and `Pipeline`.
* **Web Interface (Flask)**: Provides an intuitive web form for users to input house details.
* **Dynamic Location Dropdown**: Populates the "Area" dropdown with **all** existing location entries from the dataset, ensuring the model is trained and predicts on known areas.
* **Real-time Prediction**: Calculates and displays estimated house prices upon form submission.
* **Enhanced Prediction Display**: The prediction result is displayed in a clear, distinct, and wider box.
* **Input Validation**: Includes basic validation for user inputs (e.g., minimum values, max year built).
* **Indian Rupee Formatting**: Displays predicted prices in ₹ (Indian Rupee) format with appropriate comma separators.
* **Visually Appealing Design**:
    * **Full-Page Background Image**: A custom image covers the entire page background, creating an immersive experience.
    * **Prominent House Image**: A dedicated house image is displayed within the prediction form for visual appeal.
    * **Corner Information Text**: A dynamic text element is placed in the bottom-left corner of the page, providing additional context or branding.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x**: Download from [python.org](https://www.python.org/).
* **pip**: Python's package installer (usually comes with Python).

## Installation

1.  **Clone this repository (or download the files):**
    If you are using Git:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
    Otherwise, download the `app.py` and `index.html` files and place them in a new directory.

2.  **Place your dataset:**
    Ensure you have your dataset named `pune_house_prices.csv` in the same directory as `app.py`.

3.  **Create required image folders and add images:**
    Create a folder named `static` in your project root. Inside `static`, create another folder named `images`.
    Place your chosen background image (e.g., `background.jpg`) and your house image for the form (e.g., `house_for_prediction.png`) inside this `static/images/` folder.

    Example path: `your_project/static/images/background.jpg`

4.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    * On Windows: `.\venv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate`

5.  **Install the required Python packages:**
    ```bash
    pip install pandas scikit-learn Flask numpy
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    You will see output indicating that the Flask development server is running. It will usually be accessible at `http://127.0.0.1:5000/`.

    * **Development Mode**: For development, you can set the `FLASK_DEBUG` environment variable to `True` for automatic reloading and debugging information:
        * On Windows: `set FLASK_DEBUG=True`
        * On macOS/Linux: `export FLASK_DEBUG=True`
        Then run `python app.py`. (Remember to disable this for production environments.)

2.  **Open in your browser:**
    Navigate to the URL printed in your terminal (e.g., `http://127.0.0.1:5000/`).

3.  **Enter house details:**
    Fill in the form fields with the desired house specifications and click "Predict Price".

## File Structure

.
├── app.py                      # The main Flask application and ML model training/prediction logic
├── pune_house_prices.csv       # Your dataset for training the model
├── README.md                   # This documentation file
├── static/                     # Directory for static files (CSS, JS, Images)
│   └── images/                 # Contains images used in the web interface
│       ├── background.jpg      # The full-page background image
│       └── house_for_prediction.png # The house image displayed in the form
└── templates/
└── index.html              # The HTML template for the web interface


'''

# Installation
Clone the Repository or Download:


git clone https:https://github.com/ayushiraut01/House-Price-Prediction-Web-Application
cd pune-house-price-predictor
Place the Dataset
Make sure pune_house_prices.csv is in the root directory.

# Set Up Virtual Environment (Recommended):


python -m venv venv

source venv/bin/activate       # For Linux/macOS
.\venv\Scripts\activate        # For Windows

# Install Required Packages:

pip install -r requirements.txt

Or manually:

pip install flask pandas scikit-learn numpy
 

# Usage
Run the Flask App

python app.py
Visit the Web Page

Go to your browser and open:


http://127.0.0.1:5000/


# Predict House Price

Fill in all the required fields (Area, Size, Bedrooms, etc.)

Click "Predict Price"

View the result in ₹ format

# Model Details
Model: RandomForestRegressor from scikit-learn

Pipeline: Includes numeric imputation, one-hot encoding, and training

# Evaluation Metrics:

Mean Absolute Error (MAE)

R² Score

Root Mean Squared Error (RMSE)

# Location Handling
The area dropdown in the form is dynamically populated using:


unique_areas = sorted(df['area'].dropna().unique().tolist())
Only areas present in the dataset are selectable (e.g., Wagholi, Kharadi, Camp, Shivaji Nagar, Koregaon Park, Viman Nagar, etc.)

# Screenshots


Form View: ![image](https://github.com/user-attachments/assets/24db314f-d64c-4b9a-8c9b-ef29d18b020a)



Result View:
![image](https://github.com/user-attachments/assets/bca191e5-f014-4036-9e5b-3e5b3cb09f21)



#  License

This project is open-source and available for free use under the MIT License.
Feel free to fork, modify, and improve it as needed.

