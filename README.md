# Portfolio Assignment 1

## M3 - Group Assignment 1
**Deadline:** Monday, 10th Feb at 12:00

## Introduction
In this assignment, you will deepen your understanding of feature engineering, data preprocessing, and neural network modeling using PyTorch. While we suggest using a house pricing dataset for illustrative purposes, you are free to choose any dataset of interest.

Your goal is to build a neural network that can handle either:
- **Cross-sectional data** (i.e., data without a time component; a single “snapshot” of many observations). In this case, you will use an **MLP (Multi-Layer Perceptron)**.
- **Time-series data** (i.e., data with a temporal or sequential component). In this case, you will use an **RNN (Recurrent Neural Network)** variant (e.g., simple RNN, LSTM) to capture temporal relationships.

## Primary Objectives
- Preprocess and engineer features from your chosen dataset.
- Build, train, and evaluate at least one neural network architecture in PyTorch:
  - **MLP** if you have cross-sectional data.
  - **RNN** if you have time-series/sequential data.
- Experiment with hyperparameters, including:
  - Number of layers/neurons
  - Activation functions
  - Learning rates
  - Epochs
  - Batch size
  - Optimizers
- Evaluate and discuss results using appropriate performance metrics.

## Prerequisites
Ensure you have the following installed before running the notebook:
- Python 3.x
- Jupyter Notebook or Jupyter Lab
- PyTorch
- Additional libraries listed in `requirements.txt`

## Installation
1. Clone this repository or download the notebook file:
```sh
git clone <repository_url>
cd <repository_folder>
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```

## Running the Notebook
1. Open Jupyter Notebook:
```sh
jupyter notebook
```
2. Navigate to the directory and open `Assignment_1.ipynb`.
3. Run the notebook cells sequentially to execute the code.

## Data Preprocessing & Feature Engineering
The dataset should be loaded and preprocessed, including:
- Handling missing values
- Encoding categorical variables
- Normalization or standardization
- Feature engineering (e.g., creating new features like `house_age`)

## Model Training
1. **Define Neural Network Architecture**
   - **MLP for Cross-sectional Data**: At least two hidden layers, activation functions (ReLU, Sigmoid, etc.), and dropout/batch normalization.
   - **RNN for Time-Series Data**: Variants like LSTM, GRU, or simple RNN.
2. **Train the Model**:
   - Define loss function (e.g., MSE for regression, CrossEntropy for classification).
   - Choose an optimizer (e.g., Adam, SGD).
   - Implement early stopping and learning rate scheduling.
3. **Hyperparameter Tuning**:
   - Test different configurations for hidden layers, learning rate, and dropout rate.
   - Compare validation performance across different hyperparameter sets.

## Model Evaluation
- Compute key metrics such as RMSE, MAE, and R² score.
- Visualize actual vs. predicted values.
- Perform residual analysis.
- Interpret results and discuss improvements.

## Results & Insights
- **Best Model and Hyperparameters:**
  - Hidden Layers: (128, 64, 32)
  - Dropout Rate: 0.3
  - Optimizer: Adam (LR = 0.001)
  - Loss Function: MSE
  - Early Stopping: Patience = 100
- **Final Performance:**
  - Train RMSE: ~159,707 | Test RMSE: ~183,314
  - Train R²: ~0.8048 | Test R²: ~0.7852
- **Key Insights:**
  - Feature selection and scaling significantly impact model performance.
  - Dropout regularization prevents overfitting.
  - Higher hidden units risk overfitting, while smaller models underperform.

## Limitations & Future Improvements
- Experiment with batch handling for improved efficiency.
- Explore alternative models beyond MLP for tabular data.
- Enhance feature engineering by creating new predictive variables.
- Implement SHAP values for better feature importance interpretation.

## License
[Specify license type if required]

