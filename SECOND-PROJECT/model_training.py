import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import warnings
warnings.filterwarnings('ignore')

class HousePriceModel:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.label_encoders = {}
        self.feature_names = None
        self.is_trained = False
        
    def load_and_preprocess_data(self, filepath='melb_data.csv'):
        """Load and preprocess the Melbourne housing dataset"""
        print("Loading dataset...")
        df = pd.read_csv(filepath)
        
        # Remove rows with missing target
        df = df.dropna(subset=['Price'])
        
        # Select essential features for prediction
        features = [
            'Rooms', 'Distance', 'Bathroom', 'Car', 'Landsize', 
            'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude', 
            'Propertycount', 'Type', 'Regionname'
        ]
        
        df_model = df[features + ['Price']].copy()
        
        # Handle missing values
        numerical_cols = ['Rooms', 'Distance', 'Bathroom', 'Car', 'Landsize', 
                         'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude', 'Propertycount']
        
        for col in numerical_cols:
            if col in df_model.columns:
                df_model[col] = df_model[col].fillna(df_model[col].median())
        
        # Handle categorical variables
        categorical_cols = ['Type', 'Regionname']
        for col in categorical_cols:
            if col in df_model.columns:
                df_model[col] = df_model[col].fillna(df_model[col].mode()[0])
                le = LabelEncoder()
                df_model[col] = le.fit_transform(df_model[col])
                self.label_encoders[col] = le
        
        # Feature engineering
        current_year = 2017
        df_model['PropertyAge'] = current_year - df_model['YearBuilt']
        df_model['RoomToBathroomRatio'] = df_model['Rooms'] / (df_model['Bathroom'] + 1)
        
        # Remove outliers
        Q1 = df_model['Price'].quantile(0.01)
        Q99 = df_model['Price'].quantile(0.99)
        df_model = df_model[(df_model['Price'] >= Q1) & (df_model['Price'] <= Q99)]
        
        print(f"Dataset preprocessed successfully. Final shape: {df_model.shape}")
        return df_model
    
    def train_model(self, df_model):
        """Train the linear regression model"""
        print("Training model...")
        
        # Separate features and target
        X = df_model.drop('Price', axis=1)
        y = df_model['Price']
        
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model = LinearRegression()
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate model
        y_test_pred = self.model.predict(X_test_scaled)
        
        # Calculate metrics
        r2 = r2_score(y_test, y_test_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
        mae = mean_absolute_error(y_test, y_test_pred)
        
        print(f"Model Performance:")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE: ${rmse:,.2f}")
        print(f"MAE: ${mae:,.2f}")
        
        self.is_trained = True
        return r2, rmse, mae
    
    def predict_price(self, house_features):
        """Predict price for a house given its features"""
        if not self.is_trained:
            raise ValueError("Model must be trained first")
        
        # Convert features to the correct format
        features_array = np.array([house_features])
        
        # Scale features
        features_scaled = self.scaler.transform(features_array)
        
        # Make prediction
        prediction = self.model.predict(features_scaled)[0]
        return prediction
    
    def save_model(self, filepath='house_price_model.pkl'):
        """Save the trained model"""
        if not self.is_trained:
            raise ValueError("Model must be trained first")
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'feature_names': self.feature_names
        }
        
        joblib.dump(model_data, filepath)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath='house_price_model.pkl'):
        """Load a pre-trained model"""
        model_data = joblib.load(filepath)
        
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.label_encoders = model_data['label_encoders']
        self.feature_names = model_data['feature_names']
        self.is_trained = True
        
        print(f"Model loaded from {filepath}")

def train_and_save_model():
    """Train the model and save it for use in GUI"""
    model = HousePriceModel()
    
    # Load and preprocess data
    df_model = model.load_and_preprocess_data()
    
    # Train model
    r2, rmse, mae = model.train_model(df_model)
    
    # Save model
    model.save_model()
    
    print("\nModel training completed successfully!")
    print("You can now use the GUI to make predictions.")
    
    return model

if __name__ == "__main__":
    print("="*50)
    print("HOUSE PRICE PREDICTION MODEL TRAINING")
    print("="*50)
    
    model = train_and_save_model()
