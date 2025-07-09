import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from model_training import HousePriceModel
import os
import threading

class HousePricePredictionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("House Price Prediction System")
        self.root.geometry("600x700")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize model
        self.model = HousePriceModel()
        self.load_or_train_model()
        
        # Create GUI elements
        self.create_widgets()
        
    def load_or_train_model(self):
        """Load the trained model or train it if not found"""
        try:
            if os.path.exists('house_price_model.pkl'):
                self.model.load_model()
                self.model_loaded = True
                print("Model loaded successfully!")
            else:
                print("Model not found. Training new model...")
                self.train_model_automatically()
        except Exception as e:
            print(f"Error loading model: {e}")
            self.train_model_automatically()
    
    def train_model_automatically(self):
        """Train the model automatically if not found"""
        try:
            print("Training model, please wait...")
            # Load and preprocess data
            df_model = self.model.load_and_preprocess_data()
            # Train model
            self.model.train_model(df_model)
            # Save model
            self.model.save_model()
            self.model_loaded = True
            print("Model training completed successfully!")
        except Exception as e:
            self.model_loaded = False
            print(f"Error training model: {e}")
            messagebox.showerror("Error", f"Error training model: {str(e)}")
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main title
        title_label = tk.Label(self.root, text="🏠 House Price Prediction System", 
                              font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Create main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Input fields frame
        input_frame = tk.LabelFrame(main_frame, text="House Features", 
                                   font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#2c3e50')
        input_frame.pack(fill='x', pady=10)
        
        # Create input fields
        self.create_input_fields(input_frame)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=20)
        
        # Predict button
        predict_btn = tk.Button(button_frame, text="🔮 Predict Price", 
                               command=self.predict_price, font=("Arial", 12, "bold"),
                               bg='#3498db', fg='white', padx=20, pady=10)
        predict_btn.pack(side='left', padx=10)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="🗑️ Clear All", 
                             command=self.clear_fields, font=("Arial", 12, "bold"),
                             bg='#e74c3c', fg='white', padx=20, pady=10)
        clear_btn.pack(side='left', padx=10)
        
        # Sample data button
        sample_btn = tk.Button(button_frame, text="📋 Sample Data", 
                              command=self.fill_sample_data, font=("Arial", 12, "bold"),
                              bg='#f39c12', fg='white', padx=20, pady=10)
        sample_btn.pack(side='left', padx=10)
        
        # Result frame
        result_frame = tk.LabelFrame(main_frame, text="Prediction Result", 
                                    font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#2c3e50')
        result_frame.pack(fill='x', pady=10)
        
        # Result display
        self.result_var = tk.StringVar()
        self.result_var.set("Enter house features and click 'Predict Price'")
        
        result_label = tk.Label(result_frame, textvariable=self.result_var, 
                               font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#27ae60',
                               wraplength=550, justify='center')
        result_label.pack(pady=20)
        
        # Status bar
        self.status_var = tk.StringVar()
        status_text = "Model Ready" if self.model_loaded else "Model Not Loaded"
        self.status_var.set(f"Status: {status_text}")
        
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                             relief='sunken', anchor='w', font=("Arial", 10))
        status_bar.pack(side='bottom', fill='x')
    
    def create_input_fields(self, parent):
        """Create input fields for house features"""
        # Create entry variables
        self.entries = {}
        
        # Field definitions (label, key, default_value, tooltip)
        fields = [
            ("Number of Rooms:", "Rooms", "3", "Total number of rooms in the house"),
            ("Distance from CBD (km):", "Distance", "10", "Distance from city center in kilometers"),
            ("Number of Bathrooms:", "Bathroom", "2", "Total number of bathrooms"),
            ("Car Spaces:", "Car", "2", "Number of car parking spaces"),
            ("Land Size (sqm):", "Landsize", "500", "Land size in square meters"),
            ("Building Area (sqm):", "BuildingArea", "150", "Building area in square meters"),
            ("Year Built:", "YearBuilt", "2000", "Year the house was built"),
            ("Latitude:", "Lattitude", "-37.8", "Latitude coordinate"),
            ("Longitude:", "Longtitude", "144.96", "Longitude coordinate"),
            ("Property Count:", "Propertycount", "5000", "Number of properties in the area"),
            ("Property Type:", "Type", "house", "Type: house, unit, or townhouse"),
            ("Region:", "Regionname", "Northern Metropolitan", "Melbourne region name")
        ]
        
        # Create input fields in a grid
        for i, (label, key, default, tooltip) in enumerate(fields):
            row = i // 2
            col = (i % 2) * 3
            
            # Label
            lbl = tk.Label(parent, text=label, font=("Arial", 10), bg='#f0f0f0', anchor='w')
            lbl.grid(row=row, column=col, padx=5, pady=8, sticky='w')
            
            # Entry
            self.entries[key] = tk.Entry(parent, font=("Arial", 10), width=15)
            self.entries[key].grid(row=row, column=col+1, padx=5, pady=8, sticky='ew')
            self.entries[key].insert(0, default)
            
            # Tooltip (simplified as a small label)
            if col == 0:  # Only for left column to avoid overcrowding
                tip_lbl = tk.Label(parent, text=f"💡 {tooltip}", font=("Arial", 8), 
                                  bg='#f0f0f0', fg='#7f8c8d', wraplength=250, justify='left')
                tip_lbl.grid(row=row, column=col+2, padx=5, pady=8, sticky='w')
        
        # Configure column weights
        for i in range(6):
            parent.columnconfigure(i, weight=1)
    
    def predict_price(self):
        """Predict house price based on input features"""
        if not self.model_loaded:
            messagebox.showerror("Error", "Model not loaded. Please train the model first.")
            return
        
        try:
            # Get input values
            features = self.get_input_features()
            
            # Make prediction
            predicted_price = self.model.predict_price(features)
            
            # Display result
            self.result_var.set(f"🏠 Predicted House Price: ${predicted_price:,.2f}")
            self.status_var.set("Status: Prediction completed successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error making prediction: {str(e)}")
            self.status_var.set("Status: Error occurred")
    
    def get_input_features(self):
        """Extract and validate input features"""
        features = []
        
        # Feature order must match the model's expected input
        feature_order = [
            'Rooms', 'Distance', 'Bathroom', 'Car', 'Landsize', 
            'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude', 
            'Propertycount', 'Type', 'Regionname', 'PropertyAge', 'RoomToBathroomRatio'
        ]
        
        # Get numerical features
        try:
            rooms = float(self.entries['Rooms'].get())
            distance = float(self.entries['Distance'].get())
            bathroom = float(self.entries['Bathroom'].get())
            car = float(self.entries['Car'].get())
            landsize = float(self.entries['Landsize'].get())
            building_area = float(self.entries['BuildingArea'].get())
            year_built = float(self.entries['YearBuilt'].get())
            lattitude = float(self.entries['Lattitude'].get())
            longtitude = float(self.entries['Longtitude'].get())
            property_count = float(self.entries['Propertycount'].get())
            
            # Encode categorical features
            property_type = self.entries['Type'].get().lower()
            region = self.entries['Regionname'].get()
            
            # Simple encoding for property type
            type_encoding = {'house': 1, 'unit': 0, 'townhouse': 2}
            encoded_type = type_encoding.get(property_type, 1)
            
            # Simple encoding for region (simplified)
            region_encoding = {
                'northern metropolitan': 0,
                'southern metropolitan': 1,
                'eastern metropolitan': 2,
                'western metropolitan': 3,
                'south-eastern metropolitan': 4
            }
            encoded_region = region_encoding.get(region.lower(), 0)
            
            # Calculate derived features
            current_year = 2017
            property_age = current_year - year_built
            room_to_bathroom_ratio = rooms / (bathroom + 1)
            
            # Create features array in the correct order
            features = [
                rooms, distance, bathroom, car, landsize,
                building_area, year_built, lattitude, longtitude,
                property_count, encoded_type, encoded_region,
                property_age, room_to_bathroom_ratio
            ]
            
            return features
            
        except ValueError as e:
            raise ValueError("Please enter valid numerical values for all fields")
    
    def clear_fields(self):
        """Clear all input fields"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_var.set("Enter house features and click 'Predict Price'")
        self.status_var.set(f"Status: Fields cleared")
    
    def fill_sample_data(self):
        """Fill fields with sample data"""
        sample_data = {
            'Rooms': '3',
            'Distance': '10',
            'Bathroom': '2',
            'Car': '2',
            'Landsize': '500',
            'BuildingArea': '150',
            'YearBuilt': '2000',
            'Lattitude': '-37.8',
            'Longtitude': '144.96',
            'Propertycount': '5000',
            'Type': 'house',
            'Regionname': 'Northern Metropolitan'
        }
        
        for key, value in sample_data.items():
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, value)
        
        self.status_var.set("Status: Sample data loaded")

def main():
    """Main function to run the GUI"""
    print("="*50)
    print("🏠 HOUSE PRICE PREDICTION SYSTEM")
    print("="*50)
    print("Starting application...")
    print("If model doesn't exist, it will be trained automatically.")
    print("Please wait while the system initializes...")
    print("="*50)
    
    root = tk.Tk()
    app = HousePricePredictionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
