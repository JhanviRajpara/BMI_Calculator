import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")

        # Labels and entries for height and weight
        tk.Label(root, text="Enter your height (cm):", font=("Arial", 14)).pack(pady=10)
        self.height_entry = tk.Entry(root, font=("Arial", 14))
        self.height_entry.pack(pady=5)

        tk.Label(root, text="Enter your weight (kg):", font=("Arial", 14)).pack(pady=10)
        self.weight_entry = tk.Entry(root, font=("Arial", 14))
        self.weight_entry.pack(pady=5)

        # Calculate button
        calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 14), command=self.calculate_bmi)
        calculate_button.pack(pady=20)

        # Label to display result
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        try:
            # Get height and weight
            height = float(self.height_entry.get()) / 100  # Convert to meters
            weight = float(self.weight_entry.get())

            # Calculate BMI
            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)

            # Determine category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            # Display result
            self.result_label.config(text=f"BMI: {bmi} - {category}")

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
