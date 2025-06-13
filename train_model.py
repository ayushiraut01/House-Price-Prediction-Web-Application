import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
from flask import Flask, render_template, request, jsonify # Import Flask components

app = Flask(__name__)

# --- Model Loading and Training (executed once when the app starts) ---
# This part is largely your provided Python code for model training

df = None # Initialize df to None
model_pipeline = None
features = []
numerical_features = []
categorical_features = []
unique_areas = [] # To store unique areas for the dropdown

try:
    df = pd.read_csv('pune_house_prices.csv')
    print("Dataset loaded successfully.")
    
    target = 'price' 

    if target not in df.columns:
        print(f"Error: '{target}' column not found in the dataset. Please check the column name.")
        exit()

    df.dropna(subset=[target], inplace=True)

    features = [col for col in df.columns if col not in [target, 'id']]

    numerical_features = df[features].select_dtypes(include=np.number).columns.tolist()
    categorical_features = df[features].select_dtypes(include='object').columns.tolist()

    # Get unique areas for the HTML dropdown
    if 'area' in categorical_features:
        unique_areas = sorted(df['area'].dropna().unique().tolist())
    
    print(f"\nNumerical Features: {numerical_features}")
    print(f"Categorical Features: {categorical_features}")

    # Preprocessing Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
            ]), numerical_features),
            ('cat', Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ]), categorical_features)
        ])

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                     ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])
    
    model_pipeline.fit(X_train, y_train)
    print("\nRandom Forest Regression model trained successfully.")

    # Model Evaluation (for server startup info, not directly for user)
    y_pred = model_pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"\nModel Evaluation on Test Set (on startup):")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R-squared (R2): {r2:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

except Exception as e:
    print(f"Error during model loading/training: {e}")
    # You might want to handle this more gracefully in a production app
    model_pipeline = None # Ensure model is None if training failed

# --- Flask Routes ---

@app.route('/', methods=['GET', 'POST'])
def predict_house_price():
    prediction = None
    if request.method == 'POST':
        if model_pipeline is None:
            return "Error: Model not trained/loaded. Please check server logs.", 500

        try:
            # Get data from the form
            num_bedrooms = int(request.form['bedrooms'])
            num_bathrooms = int(request.form['bathrooms'])
            square_feet = int(request.form['square_footage']) # Renamed to match HTML
            has_garage = int(request.form['garage']) # Renamed to match HTML
            year_built = int(request.form['year_built']) # Renamed to match HTML
            area = request.form['location']

            # Create a DataFrame for prediction, ensuring column names match the features used in training
            new_house_data = pd.DataFrame([{
                'area': area,
                'square_feet': square_feet,
                'num_bedrooms': num_bedrooms,
                'num_bathrooms': num_bathrooms,
                'year_built': year_built,
                'has_garage': has_garage
            }])
            
            # Ensure the new_house_data has the same columns as the features used in training
            # This is crucial for the preprocessor
            new_house_data = new_house_data.reindex(columns=features, fill_value=np.nan)


            # Predict the price
            predicted_price = model_pipeline.predict(new_house_data)[0]
            prediction = f"₹ {predicted_price:,.2f}" # Format as Indian Rupee with commas

        except Exception as e:
            prediction = f"Error during prediction: {e}. Please check your inputs."
            print(f"Prediction error: {e}")

    # Render the HTML template, passing unique areas and prediction if available
    return render_template('index.html', locations=unique_areas, prediction=prediction)

if __name__ == '__main__':
    # It's good practice to run in debug mode for development, but disable for production
    app.run(debug=True)