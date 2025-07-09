# House Price Prediction System

## Project Overview

This project develops a linear regression model to predict house prices based on various features such as the number of rooms, location, size, and other relevant factors. The system includes a user-friendly GUI for easy interaction and prediction.

## Dataset

The project uses the Melbourne Housing Dataset (`melb_data.csv`) which contains 13,580 house records with 21 features including:

- **Rooms**: Number of rooms
- **Distance**: Distance from CBD  
- **Bathroom**: Number of bathrooms
- **Car**: Number of car spaces
- **Landsize**: Land size in square meters
- **BuildingArea**: Building area in square meters
- **YearBuilt**: Year the house was built
- **Location**: Latitude and longitude coordinates
- **Type**: Property type (house, unit, townhouse)
- **Regionname**: Region of Melbourne
- **Price**: Target variable (house price)

## Features

### Data Preprocessing
- **Missing Value Handling**: Median imputation for numerical, mode for categorical
- **Feature Engineering**: PropertyAge and RoomToBathroomRatio creation
- **Encoding**: Label encoding for categorical variables
- **Outlier Removal**: Extreme outliers removed (1st-99th percentile)
- **Feature Scaling**: StandardScaler for normalized features

### Model Performance
- **Test R²**: 0.5973 (explains ~60% of price variance)
- **Test RMSE**: $346,259.91 (average prediction error)
- **Test MAE**: $249,557.43 (median prediction error)

### GUI Features
- **User-friendly Interface**: Simple tkinter-based GUI
- **Real-time Predictions**: Instant price predictions
- **Sample Data**: Pre-filled example data
- **Input Validation**: Error handling for invalid inputs
- **Clear Interface**: Easy-to-use form layout

## Files Structure

```
SECOND-PROJECT/
├── melb_data.csv              # Dataset (13,580 house records)
├── model_training.py          # Model training and preprocessing script
├── price_prediction_gui.py    # GUI application (MAIN INTERFACE - RUN THIS!)
├── house_price_model.pkl      # Saved trained model (auto-created)
├── requirements.txt           # Python dependencies (4 packages)
└── README.md                  # Documentation
```

## Installation and Usage

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
1. Clone or download the project files
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the System

### Running the System

#### Simple One-Command Launch (Recommended)
```bash
python price_prediction_gui.py
```
**That's it!** The system will automatically:
- Check if a trained model exists
- Train the model if it doesn't exist (first run only)
- Launch the GUI application

#### Manual Training (Optional)
If you want to train the model separately:
```bash
python model_training.py
```
Then run the GUI:
```bash
python price_prediction_gui.py
```

### Using the GUI

1. **Enter House Features**: Fill in the form with house details
2. **Click "Predict Price"**: Get instant price prediction
3. **Use "Sample Data"**: Load example data to test the system
4. **Clear All**: Reset all fields

### File Descriptions

- **`price_prediction_gui.py`**: **MAIN FILE TO RUN** - GUI interface with automatic model training
- **`model_training.py`**: Handles data preprocessing, model training, and saving (used by GUI)
- **`melb_data.csv`**: Melbourne housing dataset from Kaggle
- **`house_price_model.pkl`**: Trained model (auto-created on first run)

### Sample Prediction
The GUI includes sample data that predicts approximately **$857,000** for a typical 3-bedroom house.

## Model Details

### Linear Regression Model
The model learns relationships between features and prices:
```
Price = β₀ + β₁×Rooms + β₂×Distance + β₃×Bathroom + ... + βₙ×Featureₙ
```

### Key Insights
1. **Distance from CBD**: Strongest predictor (negative correlation)
2. **Property Type**: Houses more expensive than units
3. **Bathrooms**: Significant value addition
4. **Location**: Eastern suburbs command higher prices
5. **Size**: Rooms and building area positively correlate

## Technical Requirements

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning algorithms
- **joblib**: Model persistence
- **tkinter**: GUI framework (built into Python)

## Future Enhancements

1. **Advanced Models**: Random Forest, XGBoost for better accuracy
2. **More Features**: School ratings, transport accessibility
3. **Enhanced GUI**: Better styling, visualization charts
4. **Web Interface**: Flask/Django web application
5. **Real-time Data**: Integration with current market data

## License

This project is open source and available under the MIT License.

---

*This project demonstrates a complete machine learning pipeline from data preprocessing to user-friendly GUI deployment for house price prediction.*
