# Matrix Operations Tool

A comprehensive Python application for performing matrix operations using NumPy with a modern **Graphical User Interface (GUI)**.

## 🎯 Features

### Core Matrix Operations
- **Matrix Creation**: Input custom matrices with any dimensions
- **Matrix Addition**: Add two matrices of the same dimensions
- **Matrix Subtraction**: Subtract one matrix from another
- **Matrix Multiplication**: Multiply two compatible matrices
- **Matrix Transpose**: Calculate the transpose of any matrix
- **Matrix Determinant**: Calculate determinant for square matrices
- **Matrix Inverse**: Calculate inverse for non-singular square matrices
- **Eigenvalues & Eigenvectors**: Calculate eigenvalues and eigenvectors for square matrices

### 🖥️ Modern GUI Interface
- **Interactive Interface**: Modern Tkinter-based graphical interface with professional styling
- **Visual Matrix Input**: Easy-to-use forms for matrix creation
- **Point-and-Click Operations**: Radio buttons for operation selection
- **Enhanced Results Display**: Color-coded matrix display with alternating row backgrounds
- **Real-time Results**: Immediate display of operation results with visual enhancements
- **Matrix Management**: Save, load, and manage multiple matrices
- **Professional Design**: Color-coded sections, clean layout, and modern styling
- **Matrix Statistics**: Automatic analysis of positive, negative, and zero values
- **Error Dialogs**: User-friendly error messages and validation

## 📁 Project Structure

```
THIRD-PROJECT/
├── matrix_operations_gui.py    # Main GUI application
├── matrix_operations_tool.py   # Core matrix operations (CLI version)
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── PROJECT_SUMMARY.md        # Project documentation
└── .vscode/                  # VS Code configuration
    └── tasks.json
```

## Installation

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 🖥️ GUI Version (Recommended)
Run the graphical interface:
```bash
python matrix_operations_gui.py
```

### 🎯 How to Use the GUI

1. **Create Matrices**:
   - Enter matrix name, dimensions (rows/columns)
   - Input matrix elements (space-separated, one row per line)
   - Click "Create Matrix"

2. **Perform Operations**:
   - Select operation type (Addition, Subtraction, etc.)
   - Choose matrices from dropdown menus
   - Click "Execute" button next to "Matrix Operations"

3. **View Results**:
   - Results display in the right panel with enhanced styling
   - Color-coded positive (green) and negative (red) values
   - Alternating row backgrounds for better readability
   - Matrix statistics and analysis

4. **Matrix Management**:
   - Use "List Matrices" to view all created matrices
   - Save operation results as new matrices
   - Clear all matrices when needed

### 💻 CLI Version
For command-line usage:
```bash
python matrix_operations_tool.py
```

## 🔧 Technical Details

### Dependencies
- **NumPy**: For matrix operations and linear algebra
- **Tkinter**: For GUI interface (included with Python)

### Key Features
- **Error Handling**: Comprehensive validation for matrix operations
- **Memory Management**: Efficient matrix storage and manipulation
- **User-Friendly Interface**: Intuitive GUI with professional styling
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🎨 GUI Enhancements

The GUI features modern styling with:
- **Enhanced Matrix Display**: Professional borders and color coding
- **Alternating Row Colors**: Better visual separation
- **Value-Based Coloring**: Green for positive, red for negative values
- **Matrix Statistics**: Automatic analysis of matrix properties
- **Professional Typography**: Clean fonts and proper spacing
- **Celebration Headers**: Engaging feedback for completed operations

## 📊 Supported Operations

| Operation | Description | Requirements |
|-----------|-------------|--------------|
| Addition | A + B | Same dimensions |
| Subtraction | A - B | Same dimensions |
| Multiplication | A × B | Compatible dimensions |
| Transpose | A^T | Any matrix |
| Determinant | det(A) | Square matrix |
| Inverse | A^(-1) | Non-singular square matrix |
| Eigenvalues | λ and eigenvectors | Square matrix |

## � Getting Started

1. **Run the application**:
   ```bash
   python matrix_operations_gui.py
   ```

2. **Create your first matrix**:
   - Name: "A"
   - Dimensions: 2x2
   - Elements: 
     ```
     1 2
     3 4
     ```

3. **Try operations**:
   - Create another matrix "B"
   - Select "Addition" operation
   - Choose matrices A and B
   - Click "Execute"

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

**Matrix Operations Tool** - Making linear algebra accessible through intuitive GUI design! 🎯

Or use the Windows launcher:
```bash
run_gui.bat
```

#### GUI Features:
- **Left Panel**: Matrix input and operations
- **Right Panel**: Results display and history
- **Interactive Forms**: Easy matrix creation with validation
- **Dropdown Menus**: Select matrices for operations
- **Radio Buttons**: Choose operations visually
- **Save Results**: Store operation results as new matrices
- **Professional Design**: Color-coded sections and clean layout

### 💻 CLI Version
Run the command-line interface:
```bash
python matrix_operations_tool.py
```

Or use the Windows launcher:
```bash
run_matrix_tool.bat
```

### ⚙️ VS Code Integration
If using VS Code, you can run the application using built-in tasks:
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Run Matrix Operations GUI"
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Run Matrix Operations Tool" (CLI)
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Run GUI Demo"

### Available Tasks:
- **Run Matrix Operations GUI**: Launch the GUI application
- **Run Matrix Operations Tool**: Launch the CLI application
- **Run GUI Demo**: Run the GUI with demo data pre-loaded
- **Run Demo**: Execute the CLI demonstration script
- **Run Tests**: Execute the CLI test suite
- **Run GUI Tests**: Execute the GUI test suite
- **Install Dependencies**: Install required Python packages

## Requirements

- Python 3.6 or higher
- NumPy library
- Tkinter (usually included with Python)

### Main Menu Options

1. **Create/Input Matrix** - Create a new matrix by entering dimensions and elements
2. **Display Matrix** - View a specific matrix
3. **Matrix Addition** - Add two matrices
4. **Matrix Subtraction** - Subtract two matrices
5. **Matrix Multiplication** - Multiply two matrices
6. **Matrix Transpose** - Calculate transpose of a matrix
7. **Matrix Determinant** - Calculate determinant of a square matrix
8. **Matrix Inverse** - Calculate inverse of a non-singular square matrix
9. **Matrix Eigenvalues and Eigenvectors** - Calculate eigenvalues and eigenvectors
10. **List All Matrices** - View all stored matrices
11. **View Operation History** - See history of all operations
12. **Clear All Matrices** - Remove all stored matrices
0. **Exit** - Exit the application

### Example Usage

1. **Creating a Matrix**:
   - Select option 1
   - Enter matrix name (e.g., "A")
   - Enter dimensions (e.g., 2 rows, 2 columns)
   - Enter elements row by row (e.g., "1 2" then "3 4")

2. **Matrix Operations**:
   - Create at least two matrices
   - Select the desired operation
   - Choose the matrices to operate on
   - View the formatted result
   - Optionally save the result as a new matrix

3. **Advanced Operations**:
   - For determinant/inverse: Matrix must be square
   - For eigenvalues: Matrix must be square
   - For multiplication: Columns of first matrix must equal rows of second matrix

## Features in Detail

### Matrix Input
- Supports any matrix size (rows × columns)
- Accepts floating-point numbers
- Validates input dimensions and data types
- Clear instructions and error messages

### Matrix Display
- Formatted output with proper alignment
- Shows matrix dimensions
- Clean, readable presentation
- Consistent formatting across all operations

### Error Handling
- Dimension compatibility checks
- Singular matrix detection
- Invalid input validation
- User-friendly error messages

### Operation History
- Tracks all performed operations
- Displays operation sequence
- Helps users keep track of their work

## Mathematical Operations

### Supported Operations
- **Addition**: A + B (same dimensions required)
- **Subtraction**: A - B (same dimensions required)
- **Multiplication**: A × B (columns of A must equal rows of B)
- **Transpose**: A^T (flips matrix over its diagonal)
- **Determinant**: det(A) (square matrices only)
- **Inverse**: A^(-1) (non-singular square matrices only)
- **Eigenvalues**: λ values and corresponding eigenvectors

### Matrix Properties
- Checks for square matrices
- Detects singular matrices
- Validates dimension compatibility
- Handles complex eigenvalues

## Example Session

```
=============================================================
         MATRIX OPERATIONS TOOL
=============================================================
Powered by NumPy | Interactive Matrix Calculator
=============================================================

📊 MAIN MENU:
1. Create/Input Matrix
2. Display Matrix
3. Matrix Addition
4. Matrix Subtraction
5. Matrix Multiplication
6. Matrix Transpose
7. Matrix Determinant
8. Matrix Inverse
9. Matrix Eigenvalues and Eigenvectors
10. List All Matrices
11. View Operation History
12. Clear All Matrices
0. Exit
```

## Technical Details

- Built with Python and NumPy
- Object-oriented design
- Cross-platform compatibility
- Clean, maintainable code structure
- Comprehensive error handling
- Type hints for better code documentation

## Contributing

Feel free to contribute by:
- Adding new matrix operations
- Improving the user interface
- Adding export/import functionality
- Enhancing error handling
- Adding unit tests

## License

This project is open source and available under the MIT License.
