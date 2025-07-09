#!/usr/bin/env python3
"""
Matrix Operations Tool
A comprehensive tool for performing matrix operations using NumPy
"""

import numpy as np
import os
import sys
from typing import Optional, Tuple, List

class MatrixOperationsTool:
    """Main class for matrix operations"""
    
    def __init__(self):
        self.matrices = {}
        self.history = []
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display the application header"""
        print("=" * 60)
        print("         MATRIX OPERATIONS TOOL")
        print("=" * 60)
        print("Powered by NumPy | Interactive Matrix Calculator")
        print("=" * 60)
    
    def display_menu(self):
        """Display the main menu"""
        print("\n📊 MAIN MENU:")
        print("1. Create/Input Matrix")
        print("2. Display Matrix")
        print("3. Matrix Addition")
        print("4. Matrix Subtraction")
        print("5. Matrix Multiplication")
        print("6. Matrix Transpose")
        print("7. Matrix Determinant")
        print("8. Matrix Inverse")
        print("9. Matrix Eigenvalues and Eigenvectors")
        print("10. List All Matrices")
        print("11. View Operation History")
        print("12. Clear All Matrices")
        print("0. Exit")
        print("-" * 40)
    
    def get_matrix_input(self, name: str) -> np.ndarray:
        """Get matrix input from user"""
        print(f"\n🔢 Creating matrix '{name}'")
        
        while True:
            try:
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                
                if rows <= 0 or cols <= 0:
                    print("❌ Matrix dimensions must be positive!")
                    continue
                break
            except ValueError:
                print("❌ Please enter valid integers!")
        
        print(f"\nEnter matrix elements ({rows}x{cols}):")
        print("You can enter row by row, separated by spaces")
        print("Example for 2x2: '1 2' then '3 4'")
        
        matrix_data = []
        for i in range(rows):
            while True:
                try:
                    row_input = input(f"Row {i+1}: ")
                    row = list(map(float, row_input.split()))
                    
                    if len(row) != cols:
                        print(f"❌ Please enter exactly {cols} numbers!")
                        continue
                    
                    matrix_data.append(row)
                    break
                except ValueError:
                    print("❌ Please enter valid numbers separated by spaces!")
        
        matrix = np.array(matrix_data)
        return matrix
    
    def create_matrix(self):
        """Create a new matrix"""
        print("\n🆕 CREATE NEW MATRIX")
        
        while True:
            name = input("Enter matrix name (e.g., A, B, M1): ").strip()
            if name and name not in self.matrices:
                break
            elif name in self.matrices:
                overwrite = input(f"Matrix '{name}' already exists. Overwrite? (y/n): ")
                if overwrite.lower() == 'y':
                    break
            else:
                print("❌ Please enter a valid matrix name!")
        
        matrix = self.get_matrix_input(name)
        self.matrices[name] = matrix
        
        print(f"\n✅ Matrix '{name}' created successfully!")
        self.display_matrix_formatted(name, matrix)
        
        # Add to history
        self.history.append(f"Created matrix '{name}' ({matrix.shape[0]}x{matrix.shape[1]})")
    
    def display_matrix_formatted(self, name: str, matrix: np.ndarray):
        """Display a matrix in a formatted way"""
        print(f"\n📋 Matrix '{name}' ({matrix.shape[0]}x{matrix.shape[1]}):")
        print("-" * 30)
        
        # Format numbers for better display
        formatted_matrix = np.array2string(matrix, 
                                         formatter={'float_kind': lambda x: f"{x:8.3f}"})
        print(formatted_matrix)
        print("-" * 30)
    
    def display_matrix(self):
        """Display a specific matrix"""
        if not self.matrices:
            print("❌ No matrices available. Create one first!")
            return
        
        print("\n📋 DISPLAY MATRIX")
        print("Available matrices:", list(self.matrices.keys()))
        
        name = input("Enter matrix name to display: ").strip()
        if name in self.matrices:
            self.display_matrix_formatted(name, self.matrices[name])
        else:
            print(f"❌ Matrix '{name}' not found!")
    
    def get_two_matrices(self) -> Tuple[Optional[str], Optional[str]]:
        """Get two matrix names from user"""
        if len(self.matrices) < 2:
            print("❌ Need at least 2 matrices for this operation!")
            return None, None
        
        print("Available matrices:", list(self.matrices.keys()))
        
        first = input("Enter first matrix name: ").strip()
        second = input("Enter second matrix name: ").strip()
        
        if first not in self.matrices:
            print(f"❌ Matrix '{first}' not found!")
            return None, None
        
        if second not in self.matrices:
            print(f"❌ Matrix '{second}' not found!")
            return None, None
        
        return first, second
    
    def matrix_addition(self):
        """Perform matrix addition"""
        print("\n➕ MATRIX ADDITION")
        
        first, second = self.get_two_matrices()
        if not first or not second:
            return
        
        try:
            result = self.matrices[first] + self.matrices[second]
            result_name = f"{first}+{second}"
            
            print(f"\n✅ Result: {first} + {second} = {result_name}")
            self.display_matrix_formatted(result_name, result)
            
            # Ask if user wants to save result
            save = input("Save result as new matrix? (y/n): ")
            if save.lower() == 'y':
                name = input("Enter name for result matrix: ").strip()
                if name:
                    self.matrices[name] = result
                    print(f"✅ Result saved as '{name}'")
            
            self.history.append(f"Addition: {first} + {second} = {result_name}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Matrices must have the same dimensions for addition!")
    
    def matrix_subtraction(self):
        """Perform matrix subtraction"""
        print("\n➖ MATRIX SUBTRACTION")
        
        first, second = self.get_two_matrices()
        if not first or not second:
            return
        
        try:
            result = self.matrices[first] - self.matrices[second]
            result_name = f"{first}-{second}"
            
            print(f"\n✅ Result: {first} - {second} = {result_name}")
            self.display_matrix_formatted(result_name, result)
            
            # Ask if user wants to save result
            save = input("Save result as new matrix? (y/n): ")
            if save.lower() == 'y':
                name = input("Enter name for result matrix: ").strip()
                if name:
                    self.matrices[name] = result
                    print(f"✅ Result saved as '{name}'")
            
            self.history.append(f"Subtraction: {first} - {second} = {result_name}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Matrices must have the same dimensions for subtraction!")
    
    def matrix_multiplication(self):
        """Perform matrix multiplication"""
        print("\n✖️ MATRIX MULTIPLICATION")
        
        first, second = self.get_two_matrices()
        if not first or not second:
            return
        
        try:
            result = np.dot(self.matrices[first], self.matrices[second])
            result_name = f"{first}×{second}"
            
            print(f"\n✅ Result: {first} × {second} = {result_name}")
            self.display_matrix_formatted(result_name, result)
            
            # Ask if user wants to save result
            save = input("Save result as new matrix? (y/n): ")
            if save.lower() == 'y':
                name = input("Enter name for result matrix: ").strip()
                if name:
                    self.matrices[name] = result
                    print(f"✅ Result saved as '{name}'")
            
            self.history.append(f"Multiplication: {first} × {second} = {result_name}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("For multiplication, columns of first matrix must equal rows of second matrix!")
    
    def matrix_transpose(self):
        """Perform matrix transpose"""
        print("\n🔄 MATRIX TRANSPOSE")
        
        if not self.matrices:
            print("❌ No matrices available!")
            return
        
        print("Available matrices:", list(self.matrices.keys()))
        name = input("Enter matrix name to transpose: ").strip()
        
        if name not in self.matrices:
            print(f"❌ Matrix '{name}' not found!")
            return
        
        result = self.matrices[name].T
        result_name = f"{name}^T"
        
        print(f"\n✅ Result: {name}^T = {result_name}")
        self.display_matrix_formatted(result_name, result)
        
        # Ask if user wants to save result
        save = input("Save result as new matrix? (y/n): ")
        if save.lower() == 'y':
            new_name = input("Enter name for result matrix: ").strip()
            if new_name:
                self.matrices[new_name] = result
                print(f"✅ Result saved as '{new_name}'")
        
        self.history.append(f"Transpose: {name}^T = {result_name}")
    
    def matrix_determinant(self):
        """Calculate matrix determinant"""
        print("\n🔢 MATRIX DETERMINANT")
        
        if not self.matrices:
            print("❌ No matrices available!")
            return
        
        print("Available matrices:", list(self.matrices.keys()))
        name = input("Enter matrix name to calculate determinant: ").strip()
        
        if name not in self.matrices:
            print(f"❌ Matrix '{name}' not found!")
            return
        
        matrix = self.matrices[name]
        
        if matrix.shape[0] != matrix.shape[1]:
            print("❌ Determinant can only be calculated for square matrices!")
            return
        
        try:
            det = np.linalg.det(matrix)
            
            print(f"\n✅ Determinant of matrix '{name}':")
            print(f"det({name}) = {det:.6f}")
            
            # Additional info
            if abs(det) < 1e-10:
                print("⚠️  Matrix is singular (determinant ≈ 0)")
            else:
                print("✅ Matrix is non-singular (invertible)")
            
            self.history.append(f"Determinant: det({name}) = {det:.6f}")
            
        except np.linalg.LinAlgError as e:
            print(f"❌ Error calculating determinant: {e}")
    
    def matrix_inverse(self):
        """Calculate matrix inverse"""
        print("\n🔄 MATRIX INVERSE")
        
        if not self.matrices:
            print("❌ No matrices available!")
            return
        
        print("Available matrices:", list(self.matrices.keys()))
        name = input("Enter matrix name to calculate inverse: ").strip()
        
        if name not in self.matrices:
            print(f"❌ Matrix '{name}' not found!")
            return
        
        matrix = self.matrices[name]
        
        if matrix.shape[0] != matrix.shape[1]:
            print("❌ Inverse can only be calculated for square matrices!")
            return
        
        try:
            inv_matrix = np.linalg.inv(matrix)
            result_name = f"{name}^(-1)"
            
            print(f"\n✅ Inverse of matrix '{name}':")
            self.display_matrix_formatted(result_name, inv_matrix)
            
            # Ask if user wants to save result
            save = input("Save result as new matrix? (y/n): ")
            if save.lower() == 'y':
                new_name = input("Enter name for result matrix: ").strip()
                if new_name:
                    self.matrices[new_name] = inv_matrix
                    print(f"✅ Result saved as '{new_name}'")
            
            self.history.append(f"Inverse: {name}^(-1) = {result_name}")
            
        except np.linalg.LinAlgError as e:
            print(f"❌ Error: {e}")
            print("Matrix is singular and cannot be inverted!")
    
    def matrix_eigenvalues(self):
        """Calculate eigenvalues and eigenvectors"""
        print("\n🔍 EIGENVALUES AND EIGENVECTORS")
        
        if not self.matrices:
            print("❌ No matrices available!")
            return
        
        print("Available matrices:", list(self.matrices.keys()))
        name = input("Enter matrix name to calculate eigenvalues: ").strip()
        
        if name not in self.matrices:
            print(f"❌ Matrix '{name}' not found!")
            return
        
        matrix = self.matrices[name]
        
        if matrix.shape[0] != matrix.shape[1]:
            print("❌ Eigenvalues can only be calculated for square matrices!")
            return
        
        try:
            eigenvalues, eigenvectors = np.linalg.eig(matrix)
            
            print(f"\n✅ Eigenvalues of matrix '{name}':")
            for i, val in enumerate(eigenvalues):
                if np.isreal(val):
                    print(f"λ{i+1} = {val.real:.6f}")
                else:
                    print(f"λ{i+1} = {val.real:.6f} + {val.imag:.6f}i")
            
            print(f"\n✅ Eigenvectors of matrix '{name}':")
            print("-" * 40)
            formatted_eigenvectors = np.array2string(eigenvectors, 
                                                    formatter={'float_kind': lambda x: f"{x:8.3f}"})
            print(formatted_eigenvectors)
            
            self.history.append(f"Eigenvalues calculated for matrix '{name}'")
            
        except np.linalg.LinAlgError as e:
            print(f"❌ Error calculating eigenvalues: {e}")
    
    def list_matrices(self):
        """List all available matrices"""
        print("\n📋 ALL MATRICES")
        
        if not self.matrices:
            print("❌ No matrices available!")
            return
        
        print("-" * 50)
        for name, matrix in self.matrices.items():
            print(f"Matrix '{name}': {matrix.shape[0]}x{matrix.shape[1]}")
        print("-" * 50)
        print(f"Total matrices: {len(self.matrices)}")
    
    def view_history(self):
        """View operation history"""
        print("\n📜 OPERATION HISTORY")
        
        if not self.history:
            print("❌ No operations performed yet!")
            return
        
        print("-" * 50)
        for i, operation in enumerate(self.history, 1):
            print(f"{i}. {operation}")
        print("-" * 50)
    
    def clear_matrices(self):
        """Clear all matrices"""
        if not self.matrices:
            print("❌ No matrices to clear!")
            return
        
        confirm = input("Are you sure you want to clear all matrices? (y/n): ")
        if confirm.lower() == 'y':
            self.matrices.clear()
            print("✅ All matrices cleared!")
            self.history.append("All matrices cleared")
    
    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.display_header()
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (0-12): ").strip()
                
                if choice == '0':
                    print("\n👋 Thank you for using Matrix Operations Tool!")
                    break
                elif choice == '1':
                    self.create_matrix()
                elif choice == '2':
                    self.display_matrix()
                elif choice == '3':
                    self.matrix_addition()
                elif choice == '4':
                    self.matrix_subtraction()
                elif choice == '5':
                    self.matrix_multiplication()
                elif choice == '6':
                    self.matrix_transpose()
                elif choice == '7':
                    self.matrix_determinant()
                elif choice == '8':
                    self.matrix_inverse()
                elif choice == '9':
                    self.matrix_eigenvalues()
                elif choice == '10':
                    self.list_matrices()
                elif choice == '11':
                    self.view_history()
                elif choice == '12':
                    self.clear_matrices()
                else:
                    print("❌ Invalid choice! Please try again.")
                
                if choice != '0':
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                input("\nPress Enter to continue...")

def main():
    """Main function"""
    try:
        app = MatrixOperationsTool()
        app.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
