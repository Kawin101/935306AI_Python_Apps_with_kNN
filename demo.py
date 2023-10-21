import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# Load the CSV data
data = pd.read_csv('data.csv')

# Create a KNN model
X = data[['Height', 'Weight', 'Size']]
y = data['Gender']
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Function to predict Gender
def predict_gender():
    try:
        k = int(k_entry.get())
        height = int(height_entry.get())
        weight = int(weight_entry.get())
        size = int(size_entry.get())

        features = [[height, weight, size]]
        prediction = knn.predict(features)

        result_label.config(text=f'Predicted Gender: {prediction[0]}')

    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Function to update the textarea with data from the CSV file
def update_textarea():
    textarea.delete(1.0, tk.END)  # Clear the existing content
    data = pd.read_csv('data.csv')
    textarea.insert(tk.INSERT, data.to_string(index=False))

def reset_textInput():
    k_entry.delete(0, tk.END)  # Clear the existing content
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    size_entry.delete(0, tk.END)

def reset_newTextinput():
    new_height_entry.delete(0, tk.END)  # Clear the existing content
    new_weight_entry.delete(0, tk.END)
    new_size_entry.delete(0, tk.END)
    new_gender_entry.delete(0, tk.END)

# Function to add new data
def add_data():
    global data  # Declare 'data' as a global variable
    try:
        new_height = int(new_height_entry.get())
        new_weight = int(new_weight_entry.get())
        new_size = int(new_size_entry.get())
        new_gender = new_gender_entry.get()

        new_id = len(data) + 1  # Generate an auto-incremented ID

        new_data = pd.DataFrame({'Id': [new_id], 'Height': [new_height], 'Weight': [new_weight], 'Size': [new_size], 'Gender': [new_gender]})
        data = pd.concat([data, new_data], ignore_index=True)

        # Save the updated data back to the CSV file
        data.to_csv('data.csv', index=False)

        update_textarea()  # Update the textarea with the new data
        reset_newTextinput()
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Create the main application window
app = tk.Tk()
app.title("KNN Gender Predictor")

# Labels
k_label = tk.Label(app, text="K:")
height_label = tk.Label(app, text="Height:")
weight_label = tk.Label(app, text="Weight:")
size_label = tk.Label(app, text="Size:")

# Entry fields
k_entry = tk.Entry(app)
height_entry = tk.Entry(app)
weight_entry = tk.Entry(app)
size_entry = tk.Entry(app)

# Result label
result_label = tk.Label(app, text="Predicted Gender: ", font=("Arial", 12))

# Predict button
predict_button = tk.Button(app, text="Predict Gender", command=predict_gender)

# Reset Text Input button
reset_button = tk.Button(app, text="Reset", command=reset_textInput)

# Create a textarea for displaying data
textarea = scrolledtext.ScrolledText(app, width=40, height=10)
update_textarea()

# Entry fields for adding new data
new_height_label = tk.Label(app, text="New Height:")
new_weight_label = tk.Label(app, text="New Weight:")
new_size_label = tk.Label(app, text="New Size:")
new_gender_label = tk.Label(app, text="New Gender")

new_height_entry = tk.Entry(app)
new_weight_entry = tk.Entry(app)
new_size_entry = tk.Entry(app)
new_gender_entry = tk.Entry(app)

# Add data button
add_data_button = tk.Button(app, text="Add Data", command=add_data)

# Layout using the grid manager
k_label.grid(row=0, column=0)
k_entry.grid(row=0, column=1)
height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)
weight_label.grid(row=2, column=0)
weight_entry.grid(row=2, column=1)
size_label.grid(row=3, column=0)
size_entry.grid(row=3, column=1)
predict_button.grid(row=4, column=0, columnspan=2)
reset_button.grid(row=4, column=1, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)
textarea.grid(row=6, column=0, columnspan=2)
new_height_label.grid(row=7, column=0)
new_height_entry.grid(row=7, column=1)
new_weight_label.grid(row=8, column=0)
new_weight_entry.grid(row=8, column=1)
new_size_label.grid(row=9, column=0)
new_size_entry.grid(row=9, column=1)
new_gender_label.grid(row=10, column=0)
new_gender_entry.grid(row=10, column=1)
add_data_button.grid(row=11, column=0, columnspan=2)

app.mainloop()