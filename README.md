# House-Price-Prediction

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



## File Structure

'''
.
├── app.py # Main script for scraping
├── requirements.txt # Required Python packages
├── restaurants.csv # Sample output file
└── README.md # Project documentation
'''


# Installation
Clone the Repository or Download:


git clone https:https://github.com/ayushiraut01/House-Price-Prediction-Web-Application

cd pune-house-price-predictor

Place the Dataset
Make sure pune_house_prices.csv is in the root directory.

# Set Up Virtual Environment (Recommended):


python -m venv venv

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


Form View: ![image](https://github.com/user-attachments/assets/486f4edb-becd-46da-b787-3fd314432d20)




Result View:
![image](https://github.com/user-attachments/assets/bca191e5-f014-4036-9e5b-3e5b3cb09f21)

# 🏠 House-Price-Prediction

This is a machine learning-based web application built with Flask that predicts the price of a house in **Pune, India**, based on user-provided features like area, square footage, bedrooms, bathrooms, year built, and garage availability.

---

## 📌 Project Description

This application enables users to predict house prices in Pune using a trained **Random Forest Regressor**. The model uses key housing features from the user and a historical dataset to provide a real-time price estimate, displayed in **Indian Rupees (₹)** with proper formatting.

---

## ✨ Features

🔹 Predicts house prices based on:
- Area / Location in Pune  
- Square Footage  
- Number of Bedrooms and Bathrooms  
- Year Built  
- Garage Availability

🔹 **Machine Learning Model**: Utilizes `scikit-learn`'s `RandomForestRegressor` for robust price prediction  
🔹 **Data Preprocessing Pipeline**: Handles missing values & encodes categorical features using `ColumnTransformer` and `Pipeline`  
🔹 **Web Interface**: Built with **Flask** to allow user-friendly form input  
🔹 **Dynamic Location Dropdown**: Pulls unique locations from dataset for accurate predictions  
🔹 **Real-time Prediction**: Shows results immediately on submission  
🔹 **Indian Rupee Formatting**: Results displayed in ₹ format with comma separators  
🔹 **Basic Input Validation**

---

## 📁 File Structure

.
├── app.py # Main Flask application
├── requirements.txt # Required Python packages
├── restaurants.csv # Sample output file
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

### 1. Clone the Repository:

```bash
git clone https://github.com/ayushiraut01/House-Price-Prediction-Web-Application.git
cd House-Price-Prediction-Web-Application
2. Place the Dataset
Ensure pune_house_prices.csv is in the root directory.

3. Create a Virtual Environment (Recommended):
bash
Copy
Edit
python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
4. Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install flask pandas scikit-learn numpy
🚀 Usage
Run the Flask App:
bash
Copy
Edit
python app.py
Then, open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000/
🧠 Predict House Price
Fill in all required fields (Area, Size, Bedrooms, etc.)

Click "Predict Price"

View the result displayed in ₹ (Indian Rupee) format

🧾 Model Details
Model: RandomForestRegressor from scikit-learn

Pipeline: Includes numeric imputation, one-hot encoding, and training

Evaluation Metrics:
✅ Mean Absolute Error (MAE)

✅ R² Score

✅ Root Mean Squared Error (RMSE)

🌍 Location Handling
The "Area" dropdown is dynamically populated with:

python
Copy
Edit
unique_areas = sorted(df['area'].dropna().unique().tolist())
Only valid areas from the dataset (e.g., Wagholi, Kharadi, Camp, Shivaji Nagar, Koregaon Park, Viman Nagar, etc.) are shown in the dropdown.

#  License

This project is open-source and available for free use under the MIT License.
Feel free to fork, modify, and improve it as needed.

