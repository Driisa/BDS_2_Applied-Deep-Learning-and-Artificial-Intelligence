# Portfolio Assignment 1

## M3 - Group Assignment 1
**Deadline:** Monday, 10th Feb at 12:00  

## Project Overview  
This notebook explores **feature engineering, data preprocessing, and neural network modeling** using **PyTorch** to predict house prices. The dataset used contains various housing attributes, including **size, number of rooms, location, and quality ratings**.  

The goal of this assignment is to build a **Multi-Layer Perceptron (MLP)** model to predict house prices based on features.  

## Summary of Work Done  
### **1. Data Preprocessing & Feature Engineering**
- **Data Loading:** The dataset was imported and examined for missing values.  
- **Feature Selection:** Key features that influence house prices were identified, such as:
  - **sqft_living** (size of the living space)
  - **grade** (quality of the house)
  - **bathrooms** (number of bathrooms)
  - **lat** (location coordinates)
  - **waterfront** (whether the house is near water)
- **Feature Engineering:** A new feature **house_age** was created based on `yr_built` and `yr_renovated`.
- **Data Encoding:**  
  - Categorical features (e.g., **waterfront** and **condition**) were converted to numerical values.
- **Scaling:**  
  - Standardization was applied to numerical features using `StandardScaler`.

### **2. Model Development**
- **Neural Network Architecture:**  
  - A **Feedforward MLP** was built using PyTorch with:
    - **3 hidden layers**: (128, 64, 32) neurons.
    - **ReLU activation functions** in hidden layers.
    - **Dropout regularization** (0.3) to prevent overfitting.
    - **Adam optimizer** with **learning rate 0.001**.
- **Training Strategy:**
  - **Loss function:** Mean Squared Error (MSE).
  - **Early Stopping:** Monitored validation loss to prevent overtraining.

### **3. Model Training & Hyperparameter Tuning**
- **Training the MLP model on the processed dataset** using **2000 epochs** (with early stopping).  
- **Hyperparameter tuning experiments** included variations in:
  - Number of hidden layers and neurons.
  - Learning rate adjustments.
  - Dropout rates.

### **4. Model Evaluation**
- **Performance Metrics Computed:**
  - **Root Mean Squared Error (RMSE)**: Measures prediction accuracy.
  - **Mean Absolute Error (MAE)**: Measures absolute prediction errors.
  - **R² Score**: Measures how well the model explains variability in house prices.
- **Visualizations:**
  - **Predicted vs. Actual House Prices** (Scatter plot).
  - **Residual Analysis** (Distribution of prediction errors).
  - **Training Loss Curve** (Tracking learning over epochs).

### **5. Key Findings**
- **Best Performing Model Configuration:**
  - **Hidden Layers:** (128, 64, 32)
  - **Dropout Rate:** 0.3
  - **Optimizer:** Adam (LR = 0.001)
  - **Early Stopping:** Patience = 100 epochs
- **Final Model Performance:**
  - **Training RMSE:** ~159,707
  - **Test RMSE:** ~183,314
  - **Training R²:** ~0.8048
  - **Test R²:** ~0.7852
- **Model Generalization:**
  - Good but slight overfitting observed (train RMSE < test RMSE).
  - Higher dropout rates impacted performance negatively.
  - Feature scaling significantly improved model stability.

---

## **How to Run the Notebook**
### **Prerequisites**
Ensure you have the following installed:
- Python 3.x  
- Jupyter Notebook or Jupyter Lab  
- PyTorch  
- Other dependencies listed in `requirements.txt`  

### **Installation**
1. Clone this repository or download the notebook file:
```sh
git clone <repository_url>
cd <repository_folder>
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```

### **Run the Notebook**
1. Open Jupyter Notebook:
```sh
jupyter notebook
```
2. Navigate to the directory and open `Assignment_1.ipynb`.
3. Run all cells sequentially to preprocess data, train the model, and evaluate performance.

---

## **Future Improvements**
- **Experiment with Batch Normalization:** To improve training stability.  
- **Try Alternative Models:** May provide better performance.  
- **Explore SHAP Values:** For better explainability of feature importance.  

---

Happy coding and exploring! 🚀
