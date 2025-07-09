#!/usr/bin/env python3
"""
Matrix Operations Tool - GUI Version
A comprehensive GUI application for performing matrix operations using NumPy and Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import numpy as np
from typing import Dict, Optional, Tuple
import json

class MatrixOperationsGUI:
    """Main GUI class for matrix operations"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations Tool")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Data storage
        self.matrices: Dict[str, np.ndarray] = {}
        self.history = []
        
        # Create the GUI interface
        self.create_widgets()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill=tk.X, padx=5, pady=5)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="🔢 Matrix Operations Tool", 
                              font=('Arial', 16, 'bold'), 
                              fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Matrix input and operations
        left_panel = tk.Frame(main_frame, bg='#ecf0f1', relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Right panel - Matrix display and results
        right_panel = tk.Frame(main_frame, bg='#ecf0f1', relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.create_left_panel(left_panel)
        self.create_right_panel(right_panel)
        
    def create_left_panel(self, parent):
        """Create the left panel with matrix input and operations"""
        # Matrix Creation Section
        creation_frame = tk.LabelFrame(parent, text="📊 Matrix Creation", 
                                     font=('Arial', 10, 'bold'), 
                                     bg='#ecf0f1', fg='#2c3e50')
        creation_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Matrix name input
        tk.Label(creation_frame, text="Matrix Name:", bg='#ecf0f1').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.matrix_name_entry = tk.Entry(creation_frame, width=15)
        self.matrix_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Matrix dimensions
        tk.Label(creation_frame, text="Rows:", bg='#ecf0f1').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.rows_entry = tk.Entry(creation_frame, width=10)
        self.rows_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(creation_frame, text="Columns:", bg='#ecf0f1').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.cols_entry = tk.Entry(creation_frame, width=10)
        self.cols_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Matrix input area
        tk.Label(creation_frame, text="Matrix Elements:", bg='#ecf0f1').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.matrix_input = scrolledtext.ScrolledText(creation_frame, width=40, height=5, wrap=tk.WORD)
        self.matrix_input.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # Instructions
        instructions = ("Enter matrix elements separated by spaces, one row per line.\n"
                       "Example for 2x2 matrix:\n1 2\n3 4")
        tk.Label(creation_frame, text=instructions, bg='#ecf0f1', 
                fg='#7f8c8d', font=('Arial', 7)).grid(row=5, column=0, columnspan=2, padx=5, pady=2)
        
        # Create matrix button
        create_btn = tk.Button(creation_frame, text="Create Matrix", 
                              command=self.create_matrix, 
                              bg='#3498db', fg='white', 
                              font=('Arial', 10, 'bold'))
        create_btn.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Matrix Operations Section
        operations_frame = tk.LabelFrame(parent, text="", 
                                       font=('Arial', 10, 'bold'), 
                                       bg='#ecf0f1', fg='#2c3e50')
        operations_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Create a header frame with title and execute button side by side
        header_frame = tk.Frame(operations_frame, bg='#ecf0f1')
        header_frame.grid(row=0, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=5)
        
        # Title on the left
        title_label = tk.Label(header_frame, text="⚙️ Matrix Operations", 
                              font=('Arial', 10, 'bold'), 
                              bg='#ecf0f1', fg='#2c3e50')
        title_label.pack(side=tk.LEFT)
        
        # Execute button on the right (smaller)
        execute_btn = tk.Button(header_frame, text="Execute", 
                               command=self.execute_operation, 
                               bg='#e74c3c', fg='white', 
                               font=('Arial', 9, 'bold'),
                               relief=tk.RAISED, bd=2,
                               height=1, width=8)
        execute_btn.pack(side=tk.RIGHT, padx=10)
        
        # Operation selection
        tk.Label(operations_frame, text="Select Operation:", bg='#ecf0f1').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.operation_var = tk.StringVar(value="addition")
        operations = [
            ("Addition", "addition"),
            ("Subtraction", "subtraction"),
            ("Multiplication", "multiplication"),
            ("Transpose", "transpose"),
            ("Determinant", "determinant"),
            ("Inverse", "inverse"),
            ("Eigenvalues", "eigenvalues")
        ]
        
        for i, (text, value) in enumerate(operations):
            tk.Radiobutton(operations_frame, text=text, variable=self.operation_var, 
                          value=value, bg='#ecf0f1').grid(row=i+2, column=0, sticky=tk.W, padx=20, pady=2)
        
        # Matrix selection for operations
        tk.Label(operations_frame, text="Matrix 1:", bg='#ecf0f1').grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.matrix1_var = tk.StringVar()
        self.matrix1_combo = ttk.Combobox(operations_frame, textvariable=self.matrix1_var, 
                                         width=15, state='readonly')
        self.matrix1_combo.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(operations_frame, text="Matrix 2:", bg='#ecf0f1').grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        self.matrix2_var = tk.StringVar()
        self.matrix2_combo = ttk.Combobox(operations_frame, textvariable=self.matrix2_var, 
                                         width=15, state='readonly')
        self.matrix2_combo.grid(row=5, column=1, padx=5, pady=5)
        
        # Matrix Management Section
        management_frame = tk.LabelFrame(parent, text="📋 Matrix Management", 
                                       font=('Arial', 10, 'bold'), 
                                       bg='#ecf0f1', fg='#2c3e50')
        management_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Buttons for matrix management
        btn_frame = tk.Frame(management_frame, bg='#ecf0f1')
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(btn_frame, text="List Matrices", command=self.list_matrices, 
                 bg='#9b59b6', fg='white', width=15).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all_matrices, 
                 bg='#e67e22', fg='white', width=15).pack(side=tk.LEFT, padx=2)
        
    def create_right_panel(self, parent):
        """Create the right panel with results display"""
        # Results display
        results_frame = tk.LabelFrame(parent, text="📈 Results Display", 
                                    font=('Arial', 10, 'bold'), 
                                    bg='#ecf0f1', fg='#2c3e50')
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create a frame for the text widget with better styling
        text_frame = tk.Frame(results_frame, bg='#ecf0f1', relief=tk.SUNKEN, bd=2)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.results_text = scrolledtext.ScrolledText(text_frame, 
                                                     width=50, height=20, 
                                                     wrap=tk.WORD, 
                                                     font=('Arial', 10),
                                                     bg='#f8f9fa',
                                                     fg='#2c3e50',
                                                     selectbackground='#3498db',
                                                     selectforeground='white',
                                                     relief=tk.FLAT,
                                                     bd=0)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # History section
        history_frame = tk.LabelFrame(parent, text="📜 Operation History", 
                                    font=('Arial', 10, 'bold'), 
                                    bg='#ecf0f1', fg='#2c3e50')
        history_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, width=50, height=8, 
                                                     wrap=tk.WORD, font=('Arial', 9),
                                                     bg='#f8f9fa', fg='#2c3e50')
        self.history_text.pack(fill=tk.X, padx=5, pady=5)
        
        # Control buttons
        control_frame = tk.Frame(parent, bg='#ecf0f1')
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(control_frame, text="Clear Results", command=self.clear_results, 
                 bg='#95a5a6', fg='white', width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Save Result", command=self.save_result, 
                 bg='#27ae60', fg='white', width=15).pack(side=tk.LEFT, padx=5)
        
    def create_matrix(self):
        """Create a new matrix from user input"""
        try:
            # Get matrix name
            name = self.matrix_name_entry.get().strip()
            if not name:
                messagebox.showerror("Error", "Please enter a matrix name!")
                return
            
            # Get dimensions
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            
            if rows <= 0 or cols <= 0:
                messagebox.showerror("Error", "Dimensions must be positive!")
                return
            
            # Get matrix elements
            matrix_text = self.matrix_input.get('1.0', tk.END).strip()
            if not matrix_text:
                messagebox.showerror("Error", "Please enter matrix elements!")
                return
            
            # Parse matrix elements
            lines = matrix_text.split('\n')
            matrix_data = []
            
            for line in lines:
                if line.strip():
                    row = [float(x) for x in line.split()]
                    if len(row) != cols:
                        messagebox.showerror("Error", f"Row must have exactly {cols} elements!")
                        return
                    matrix_data.append(row)
            
            if len(matrix_data) != rows:
                messagebox.showerror("Error", f"Matrix must have exactly {rows} rows!")
                return
            
            # Create numpy array
            matrix = np.array(matrix_data)
            
            # Store matrix
            self.matrices[name] = matrix
            
            # Update comboboxes
            self.update_matrix_lists()
            
            # Display result
            self.display_matrix(name, matrix)
            
            # Add to history
            self.add_to_history(f"Created matrix '{name}' ({rows}x{cols})")
            
            # Clear input fields
            self.matrix_name_entry.delete(0, tk.END)
            self.rows_entry.delete(0, tk.END)
            self.cols_entry.delete(0, tk.END)
            self.matrix_input.delete('1.0', tk.END)
            
            messagebox.showinfo("Success", f"Matrix '{name}' created successfully!")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def execute_operation(self):
        """Execute the selected matrix operation"""
        try:
            operation = self.operation_var.get()
            matrix1_name = self.matrix1_var.get()
            matrix2_name = self.matrix2_var.get()
            
            if not matrix1_name:
                messagebox.showerror("Error", "Please select Matrix 1!")
                return
            
            matrix1 = self.matrices[matrix1_name]
            
            if operation == "addition":
                if not matrix2_name:
                    messagebox.showerror("Error", "Please select Matrix 2 for addition!")
                    return
                matrix2 = self.matrices[matrix2_name]
                result = matrix1 + matrix2
                result_name = f"{matrix1_name} + {matrix2_name}"
                self.display_operation_result(result_name, result)
                self.add_to_history(f"Addition: {matrix1_name} + {matrix2_name}")
                
            elif operation == "subtraction":
                if not matrix2_name:
                    messagebox.showerror("Error", "Please select Matrix 2 for subtraction!")
                    return
                matrix2 = self.matrices[matrix2_name]
                result = matrix1 - matrix2
                result_name = f"{matrix1_name} - {matrix2_name}"
                self.display_operation_result(result_name, result)
                self.add_to_history(f"Subtraction: {matrix1_name} - {matrix2_name}")
                
            elif operation == "multiplication":
                if not matrix2_name:
                    messagebox.showerror("Error", "Please select Matrix 2 for multiplication!")
                    return
                matrix2 = self.matrices[matrix2_name]
                result = np.dot(matrix1, matrix2)
                result_name = f"{matrix1_name} × {matrix2_name}"
                self.display_operation_result(result_name, result)
                self.add_to_history(f"Multiplication: {matrix1_name} × {matrix2_name}")
                
            elif operation == "transpose":
                result = matrix1.T
                result_name = f"{matrix1_name}^T"
                self.display_operation_result(result_name, result)
                self.add_to_history(f"Transpose: {matrix1_name}^T")
                
            elif operation == "determinant":
                if matrix1.shape[0] != matrix1.shape[1]:
                    messagebox.showerror("Error", "Determinant requires a square matrix!")
                    return
                result = np.linalg.det(matrix1)
                self.display_scalar_result(f"det({matrix1_name})", result)
                self.add_to_history(f"Determinant: det({matrix1_name}) = {result:.6f}")
                
            elif operation == "inverse":
                if matrix1.shape[0] != matrix1.shape[1]:
                    messagebox.showerror("Error", "Inverse requires a square matrix!")
                    return
                result = np.linalg.inv(matrix1)
                result_name = f"{matrix1_name}^(-1)"
                self.display_operation_result(result_name, result)
                self.add_to_history(f"Inverse: {matrix1_name}^(-1)")
                
            elif operation == "eigenvalues":
                if matrix1.shape[0] != matrix1.shape[1]:
                    messagebox.showerror("Error", "Eigenvalues require a square matrix!")
                    return
                eigenvalues, eigenvectors = np.linalg.eig(matrix1)
                self.display_eigenvalues_result(matrix1_name, eigenvalues, eigenvectors)
                self.add_to_history(f"Eigenvalues calculated for {matrix1_name}")
            
            # Store the last result for saving
            if operation in ["addition", "subtraction", "multiplication", "transpose", "inverse"]:
                self.last_result = result
                self.last_result_name = result_name
            
        except np.linalg.LinAlgError as e:
            messagebox.showerror("Linear Algebra Error", str(e))
        except ValueError as e:
            messagebox.showerror("Value Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_matrix(self, name, matrix):
        """Display a matrix in the results area with enhanced GUI styling"""
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(font=('Arial', 10), bg='#f8f9fa')
        
        # Title with enhanced styling
        self.results_text.insert(tk.END, "🎯 ", "title")
        self.results_text.insert(tk.END, "MATRIX CREATED", "title")
        self.results_text.insert(tk.END, " 🎯\n\n", "title")
        
        # Matrix information with better formatting
        self.results_text.insert(tk.END, "📊 Matrix Name: ", "info")
        self.results_text.insert(tk.END, f"{name}\n", "title")
        self.results_text.insert(tk.END, "📐 Dimensions: ", "info")
        self.results_text.insert(tk.END, f"{matrix.shape[0]} × {matrix.shape[1]}\n", "title")
        
        # Matrix type information
        if matrix.shape[0] == matrix.shape[1]:
            self.results_text.insert(tk.END, "🔲 Type: ", "info")
            self.results_text.insert(tk.END, "Square Matrix\n", "success")
        else:
            self.results_text.insert(tk.END, "🔳 Type: ", "info")
            self.results_text.insert(tk.END, "Rectangular Matrix\n", "info")
        
        # Matrix display with enhanced styling
        self.display_matrix_with_styling(matrix)
        
        # Configure text tags for styling
        self.configure_text_tags()
    
    def display_operation_result(self, result_name, result):
        """Display the result of a matrix operation with enhanced GUI styling"""
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(font=('Arial', 10), bg='#f8f9fa')
        
        # Operation result header with enhanced styling
        self.results_text.insert(tk.END, "🎉 ", "success")
        self.results_text.insert(tk.END, "OPERATION SUCCESSFUL", "success")
        self.results_text.insert(tk.END, " 🎉\n\n", "success")
        
        # Result information with better formatting
        self.results_text.insert(tk.END, "� Result: ", "info")
        self.results_text.insert(tk.END, f"{result_name}\n", "title")
        self.results_text.insert(tk.END, "📐 Matrix Size: ", "info")
        self.results_text.insert(tk.END, f"{result.shape[0]} × {result.shape[1]}\n", "title")
        
        # Result matrix display with enhanced styling
        self.display_matrix_with_styling(result)
        
        # Add summary information
        total_elements = result.shape[0] * result.shape[1]
        positive_count = np.sum(result > 0)
        negative_count = np.sum(result < 0)
        zero_count = np.sum(np.abs(result) < 1e-10)
        
        self.results_text.insert(tk.END, "📈 Matrix Statistics:\n", "title")
        self.results_text.insert(tk.END, f"   • Total elements: {total_elements}\n", "info")
        self.results_text.insert(tk.END, f"   • Positive values: {positive_count}\n", "info")
        self.results_text.insert(tk.END, f"   • Negative values: {negative_count}\n", "info")
        self.results_text.insert(tk.END, f"   • Zero values: {zero_count}\n", "info")
        
        # Configure text tags for styling
        self.configure_text_tags()
    
    def display_matrix_with_styling(self, matrix):
        """Display matrix with modern GUI styling and visual enhancements"""
        rows, cols = matrix.shape
        
        # Create a visually appealing matrix display
        self.results_text.insert(tk.END, "\n", "")
        
        # Matrix header with styling
        self.results_text.insert(tk.END, "╔", "matrix_border")
        self.results_text.insert(tk.END, "═" * (cols * 14 + 1), "matrix_border")
        self.results_text.insert(tk.END, "╗\n", "matrix_border")
        
        # Matrix content with enhanced styling
        for i in range(rows):
            self.results_text.insert(tk.END, "║", "matrix_border")
            self.results_text.insert(tk.END, " ", "matrix_bg")
            
            for j in range(cols):
                value = matrix[i, j]
                if abs(value) < 1e-10:
                    value = 0.0  # Clean up near-zero values
                
                # Format value with better presentation
                if value == int(value):
                    formatted_value = f"{int(value):>6}"
                else:
                    formatted_value = f"{value:>6.3f}"
                
                # Add background styling and value styling
                if i % 2 == 0:  # Alternating row colors
                    if value >= 0:
                        self.results_text.insert(tk.END, formatted_value, "matrix_positive_even")
                    else:
                        self.results_text.insert(tk.END, formatted_value, "matrix_negative_even")
                else:
                    if value >= 0:
                        self.results_text.insert(tk.END, formatted_value, "matrix_positive_odd")
                    else:
                        self.results_text.insert(tk.END, formatted_value, "matrix_negative_odd")
                
                if j < cols - 1:
                    self.results_text.insert(tk.END, "  ", "matrix_bg")
            
            self.results_text.insert(tk.END, " ", "matrix_bg")
            self.results_text.insert(tk.END, "║\n", "matrix_border")
        
        # Bottom border
        self.results_text.insert(tk.END, "╚", "matrix_border")
        self.results_text.insert(tk.END, "═" * (cols * 14 + 1), "matrix_border")
        self.results_text.insert(tk.END, "╝\n\n", "matrix_border")
    
    def configure_text_tags(self):
        """Configure text tags for enhanced GUI styling"""
        # Configure background color for the text widget
        self.results_text.config(bg='#f8f9fa', fg='#2c3e50', selectbackground='#3498db')
        
        # Header and title styles
        self.results_text.tag_config("title", foreground="#2c3e50", font=('Arial', 14, 'bold'))
        self.results_text.tag_config("success", foreground="#27ae60", font=('Arial', 12, 'bold'))
        self.results_text.tag_config("info", foreground="#7f8c8d", font=('Arial', 10))
        
        # Enhanced matrix border styling
        self.results_text.tag_config("matrix_border", foreground="#34495e", font=('Courier', 12, 'bold'))
        self.results_text.tag_config("matrix_bg", background="#ecf0f1")
        
        # Matrix value styles with alternating row backgrounds
        self.results_text.tag_config("matrix_positive_even", 
                                   foreground="#27ae60", 
                                   background="#e8f5e8", 
                                   font=('Courier', 11, 'bold'))
        self.results_text.tag_config("matrix_negative_even", 
                                   foreground="#e74c3c", 
                                   background="#fdf2f2", 
                                   font=('Courier', 11, 'bold'))
        self.results_text.tag_config("matrix_positive_odd", 
                                   foreground="#27ae60", 
                                   background="#f0f8f0", 
                                   font=('Courier', 11, 'bold'))
        self.results_text.tag_config("matrix_negative_odd", 
                                   foreground="#e74c3c", 
                                   background="#fdf8f8", 
                                   font=('Courier', 11, 'bold'))
        
        # Fallback matrix styles
        self.results_text.tag_config("matrix_value", foreground="#2c3e50", font=('Courier', 10, 'bold'))
        self.results_text.tag_config("matrix_positive", foreground="#27ae60", font=('Courier', 10, 'bold'))
        self.results_text.tag_config("matrix_negative", foreground="#e74c3c", font=('Courier', 10, 'bold'))
        
        # Scalar and special value styles
        self.results_text.tag_config("scalar", foreground="#8e44ad", font=('Arial', 16, 'bold'))
        self.results_text.tag_config("scalar_box", background="#ecf0f1", foreground="#2c3e50", font=('Courier', 12, 'bold'))
        self.results_text.tag_config("warning", foreground="#f39c12", font=('Arial', 11, 'bold'))
        
        # Enhanced border styles
        self.results_text.tag_config("border", foreground="#34495e", font=('Courier', 11, 'bold'))
        
        # Eigenvalue styles
        self.results_text.tag_config("eigenvalue", foreground="#9b59b6", font=('Courier', 12, 'bold'))
    
    
    def display_scalar_result(self, operation_name, result):
        """Display a scalar result with enhanced GUI styling"""
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(font=('Arial', 10), bg='#f8f9fa')
        
        # Operation header
        self.results_text.insert(tk.END, f"✅ Operation Complete!\n", "success")
        self.results_text.insert(tk.END, f"🔢 {operation_name}\n\n", "title")
        
        # Enhanced result display with styled box
        self.results_text.insert(tk.END, "╔═══════════════════════════════╗\n", "border")
        self.results_text.insert(tk.END, "║        RESULT VALUE           ║\n", "border")
        self.results_text.insert(tk.END, "╠═══════════════════════════════╣\n", "border")
        
        # Clean up result value
        if abs(result) < 1e-10:
            result = 0.0
        result_str = f"{result:.6f}"
        padding = (31 - len(result_str)) // 2
        self.results_text.insert(tk.END, f"║{' ' * padding}", "border")
        self.results_text.insert(tk.END, f"{result_str}", "scalar")
        self.results_text.insert(tk.END, f"{' ' * (31 - len(result_str) - padding)}║\n", "border")
        
        self.results_text.insert(tk.END, "╚═══════════════════════════════╝\n\n", "border")
        
        # Enhanced status message with better formatting
        if abs(result) < 1e-10:
            self.results_text.insert(tk.END, "⚠️  MATRIX STATUS: SINGULAR\n", "warning")
            self.results_text.insert(tk.END, "   • Determinant is approximately zero\n", "info")
            self.results_text.insert(tk.END, "   • Matrix cannot be inverted\n", "info")
            self.results_text.insert(tk.END, "   • System may have no unique solution\n", "info")
        else:
            self.results_text.insert(tk.END, "✅ MATRIX STATUS: NON-SINGULAR\n", "success")
            self.results_text.insert(tk.END, "   • Determinant is non-zero\n", "info")
            self.results_text.insert(tk.END, "   • Matrix can be inverted\n", "info")
            self.results_text.insert(tk.END, "   • System has a unique solution\n", "info")
        
        # Configure text tags for styling
        self.configure_text_tags()
    
    def display_eigenvalues_result(self, matrix_name, eigenvalues, eigenvectors):
        """Display eigenvalues and eigenvectors with enhanced GUI styling"""
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(font=('Arial', 10), bg='#f8f9fa')
        
        # Header
        self.results_text.insert(tk.END, f"✅ Eigenvalue Analysis Complete!\n", "success")
        self.results_text.insert(tk.END, f"🔢 Matrix: {matrix_name}\n\n", "title")
        
        # Eigenvalues section with enhanced styling
        self.results_text.insert(tk.END, "📊 EIGENVALUES\n", "title")
        self.results_text.insert(tk.END, "╔═══════════════════════════════╗\n", "border")
        self.results_text.insert(tk.END, "║         EIGENVALUES           ║\n", "border")
        self.results_text.insert(tk.END, "╠═══════════════════════════════╣\n", "border")
        
        for i, val in enumerate(eigenvalues):
            if np.isreal(val):
                val_str = f"λ{i+1} = {val.real:.6f}"
            else:
                val_str = f"λ{i+1} = {val.real:.6f} + {val.imag:.6f}i"
            
            padding = (31 - len(val_str)) // 2
            self.results_text.insert(tk.END, f"║{' ' * padding}", "border")
            self.results_text.insert(tk.END, val_str, "eigenvalue")
            self.results_text.insert(tk.END, f"{' ' * (31 - len(val_str) - padding)}║\n", "border")
        
        self.results_text.insert(tk.END, "╚═══════════════════════════════╝\n\n", "border")
        
        # Eigenvectors section with better formatting
        self.results_text.insert(tk.END, "📐 EIGENVECTORS\n", "title")
        self.results_text.insert(tk.END, "Each column represents an eigenvector\n\n", "info")
        self.display_matrix_with_styling(eigenvectors)
        
        # Add interpretation
        self.results_text.insert(tk.END, "💡 INTERPRETATION\n", "title")
        self.results_text.insert(tk.END, f"   • Found {len(eigenvalues)} eigenvalue(s)\n", "info")
        
        real_count = sum(1 for val in eigenvalues if np.isreal(val))
        complex_count = len(eigenvalues) - real_count
        
        if real_count > 0:
            self.results_text.insert(tk.END, f"   • {real_count} real eigenvalue(s)\n", "info")
        if complex_count > 0:
            self.results_text.insert(tk.END, f"   • {complex_count} complex eigenvalue(s)\n", "info")
        
        # Configure text tags for styling
        self.configure_text_tags()
    
    def format_matrix(self, matrix):
        """Format matrix for display"""
        return np.array2string(matrix, formatter={'float_kind': lambda x: f"{x:8.3f}"})
    
    def update_matrix_lists(self):
        """Update the matrix selection comboboxes"""
        matrix_names = list(self.matrices.keys())
        self.matrix1_combo['values'] = matrix_names
        self.matrix2_combo['values'] = matrix_names
    
    def list_matrices(self):
        """List all available matrices with enhanced styling"""
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(font=('Arial', 10), bg='#f8f9fa')
        
        # Header
        self.results_text.insert(tk.END, "📋 MATRIX INVENTORY\n", "title")
        self.results_text.insert(tk.END, "═" * 40 + "\n\n", "border")
        
        if not self.matrices:
            self.results_text.insert(tk.END, "❌ No matrices available.\n", "warning")
            self.results_text.insert(tk.END, "   Create a matrix using the Matrix Creation section.\n", "info")
        else:
            self.results_text.insert(tk.END, "✅ Available Matrices:\n\n", "success")
            
            for i, (name, matrix) in enumerate(self.matrices.items(), 1):
                self.results_text.insert(tk.END, f"{i}. ", "info")
                self.results_text.insert(tk.END, f"'{name}'", "title")
                self.results_text.insert(tk.END, f" → {matrix.shape[0]}×{matrix.shape[1]}", "info")
                
                # Add matrix type information
                if matrix.shape[0] == matrix.shape[1]:
                    self.results_text.insert(tk.END, " (Square)\n", "success")
                else:
                    self.results_text.insert(tk.END, " (Rectangular)\n", "info")
        
        self.results_text.insert(tk.END, "\n" + "═" * 40 + "\n", "border")
        self.results_text.insert(tk.END, f"📊 Total matrices: {len(self.matrices)}\n", "title")
        
        # Configure text tags for styling
        self.configure_text_tags()
    
    def clear_all_matrices(self):
        """Clear all matrices"""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all matrices?"):
            self.matrices.clear()
            self.update_matrix_lists()
            self.clear_results()
            self.add_to_history("All matrices cleared")
            messagebox.showinfo("Success", "All matrices cleared!")
    
    def clear_results(self):
        """Clear the results display"""
        self.results_text.delete('1.0', tk.END)
    
    def save_result(self):
        """Save the last operation result as a new matrix"""
        if not hasattr(self, 'last_result'):
            messagebox.showwarning("Warning", "No result available to save!")
            return
        
        # Ask for matrix name
        name = tk.simpledialog.askstring("Save Result", "Enter name for the result matrix:")
        if name:
            self.matrices[name] = self.last_result
            self.update_matrix_lists()
            self.add_to_history(f"Saved result as '{name}'")
            messagebox.showinfo("Success", f"Result saved as '{name}'!")
    
    def add_to_history(self, operation):
        """Add an operation to the history"""
        self.history.append(operation)
        self.history_text.insert(tk.END, f"{len(self.history)}. {operation}\n")
        self.history_text.see(tk.END)

def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = MatrixOperationsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
