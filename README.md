# Prediction-of-Disease-Outbreaks
AI-driven disease prediction model using machine learning to analyze and predict the risk of diabetes, heart disease, and Parkinson’s based on health indicators.

## Overview
This project is an AI-driven disease prediction model that utilizes machine learning techniques to predict the likelihood of a person having **diabetes, heart disease, or Parkinson’s disease** based on various health indicators. The model is trained using a dataset in CSV format and employs **Support Vector Machine (SVM)** for classification.

## Features
- **Predicts three diseases**: Diabetes, Heart Disease, and Parkinson’s Disease.
- **User-friendly interface** built with **Streamlit**.
- **Trained models** are saved and loaded for efficient predictions.
- **Feature selection and data preprocessing** ensure optimized model performance.
- **Error handling** for invalid or missing inputs.

## Technologies Used
- Python
- Scikit-Learn
- Streamlit
- Pandas & NumPy
- Pickle (for saving models)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/disease-prediction.git
   cd disease-prediction
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_file.py
   ```

## Usage
1. Choose the disease you want to predict from the sidebar.
2. Enter the required health parameters in the input fields.
3. Click on the "Predict" button to get the results.

## Model Training
- The dataset is preprocessed to handle missing values and normalize features.
- Support Vector Machine (SVM) is used for classification.
- The trained models are saved using Pickle for later use.

## Future Improvements
- Enhance model accuracy with deep learning techniques.
- Expand disease coverage beyond the current three.
- Deploy as a cloud-based API for integration into healthcare systems.

## License
This project is open-source and available under the MIT License.

## Contributors
- **Hitashri M** - Developer

## Acknowledgments
Special thanks to **TechSaksham** and my mentor **Aditya Prashant Ardak** for their valuable guidance and support throughout this project.
