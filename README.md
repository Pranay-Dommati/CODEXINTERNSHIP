# CODE X Internship Projects

This repository contains four Python projects developed during the CODEX internship program. Each project demonstrates different aspects of data science, machine learning, and software development.

## Project Overview

### 1. Student Performance Analysis (FIRST-PROJECT)
**Data Analysis and Visualization with Pandas and Matplotlib**

Using the Pandas library, this project loads a CSV file and performs basic data analysis tasks, such as calculating the average of selected columns. Additionally, it uses Matplotlib to create visualizations, including bar charts, scatter plots, and heatmaps, to analyze student performance data. The project provides insights and observations based on the analysis and visualizations.

**Features:**
- CSV data loading and processing with Pandas
- Statistical analysis and calculations
- Data visualizations (bar charts, scatter plots, heatmaps)
- Comprehensive insights and observations

**Files:**
- `student_performance_analysis_improved.py` - Main analysis script
- `StudentsPerformance.csv` - Dataset containing student performance data

---

### 2. House Price Prediction (SECOND-PROJECT)
**Machine Learning Model for Real Estate Price Prediction**

This project develops a linear regression model to predict house prices based on features such as the number of rooms, location, size, and other relevant factors. The dataset was collected from Kaggle, preprocessed, and used to train the model to make accurate predictions.

**Features:**
- Linear regression model implementation
- Data preprocessing and feature engineering
- Model training and evaluation
- GUI interface for price predictions
- Trained model serialization

**Files:**
- `model_training.py` - Model training and evaluation script
- `price_prediction_gui.py` - GUI application for price predictions
- `house_price_model.pkl` - Serialized trained model
- `melb_data.csv` - Melbourne housing dataset
- `requirements.txt` - Project dependencies
- `README.md` - Project-specific documentation

---

### 3. Matrix Operations Tool (THIRD-PROJECT)
**Interactive Matrix Calculator with NumPy**

This project creates a "Matrix Operations Tool" using Python and the NumPy library. The application allows users to input matrices and perform operations like addition, subtraction, multiplication, transpose, and determinant calculation. It includes an interactive interface to display results in a structured format.

**Features:**
- Matrix input and validation
- Basic matrix operations (addition, subtraction, multiplication)
- Advanced operations (transpose, determinant)
- Interactive GUI interface
- Structured result display

**Files:**
- `matrix_operations_tool.py` - Core matrix operations logic
- `matrix_operations_gui.py` - GUI application
- `requirements.txt` - Project dependencies
- `README.md` - Project-specific documentation

---

### 4. Voice-Activated Personal Assistant (FOURTH-PROJECT)
**Interactive Voice Assistant with Speech Recognition**

This project builds a personal assistant that performs tasks like setting reminders, checking the weather, and reading the news. It integrates with speech recognition and text-to-speech libraries to create an interactive, voice-activated experience.

**Features:**
- Voice command recognition
- Text-to-speech responses
- Reminder management
- Weather information
- News reading capabilities
- Modern web-based frontend interface
- RESTful API backend

**Backend Files:**
- `backend_api.py` - Main API server
- `gemini_processor.py` - AI processing module
- `services.py` - Core service implementations
- `command_parser.py` - Voice command parsing
- `config.py` - Configuration settings
- `reminders.json` - Reminder storage
- `requirements.txt` - Backend dependencies

**Frontend Files:**
- `frontend/` - React-based web interface
- `frontend/src/components/` - UI components
- `frontend/package.json` - Frontend dependencies

## Technical Stack

### Languages and Frameworks
- **Python** - Primary programming language
- **JavaScript/React** - Frontend development (Project 4)
- **HTML/CSS** - Web interface styling

### Libraries and Tools
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical computing and matrix operations
- **Scikit-learn** - Machine learning algorithms
- **Tkinter** - GUI development
- **Speech Recognition** - Voice input processing
- **Text-to-Speech** - Voice output generation
- **Flask/FastAPI** - Web API development
- **React** - Frontend framework
- **Vite** - Build tool

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Node.js and npm (for Project 4 frontend)
- Required Python packages (see individual `requirements.txt` files)

### Installation
1. Clone the repository
2. Navigate to each project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. For Project 4 frontend:
   ```bash
   cd FOURTH-PROJECT/frontend
   npm install
   ```

### Running the Projects

1. **Student Performance Analysis:**
   ```bash
   cd FIRST-PROJECT
   python student_performance_analysis_improved.py
   ```

2. **House Price Prediction:**
   ```bash
   cd SECOND-PROJECT
   python price_prediction_gui.py
   ```

3. **Matrix Operations Tool:**
   ```bash
   cd THIRD-PROJECT
   python matrix_operations_gui.py
   ```

4. **Voice-Activated Assistant:**
   ```bash
   # Backend
   cd FOURTH-PROJECT
   python backend_api.py
   
   # Frontend (in separate terminal)
   cd FOURTH-PROJECT/frontend
   npm run dev
   ```

## Project Insights

Each project demonstrates different aspects of software development:

- **Data Analysis** - Working with real datasets and extracting meaningful insights
- **Machine Learning** - Building predictive models and evaluating performance
- **GUI Development** - Creating user-friendly interfaces for complex operations
- **Voice Processing** - Implementing speech recognition and natural language processing
- **Full-Stack Development** - Building complete applications with frontend and backend

## Contributing

These projects were developed as part of the CODEX internship program. Each project includes detailed documentation and can be extended with additional features.

## License

This project is developed for educational purposes as part of the CODEX internship program.

---

*Developed during CODEX Internship Program - July 2025*
