# END-TO-END-DATA-SCIENCE-PROJECT

COMPANY: CODTECH IT SOLUTIONS

NAME: MANISHA KUMARI

INTERN ID: CT12DN310

DOMAIN: DATA SCIENCE

DURATION: 12 WEEKS

MENTOR: NEELA SANTHOSH KUMAR

# END-TO-END DATA SCIENCE PROJECT
CodTech Internship Task 3 – Flask Deployment with Iris Dataset

## Project Overview
This project implements a complete End-to-End Data Science pipeline using the Iris dataset:
- Data loading and preprocessing
- Model training (Logistic Regression)
- Flask web app deployment
- User can input Sepal & Petal dimensions to get predicted species

## Technologies Used
- Python  
- Pandas, Scikit-learn  
- Flask  
- HTML (Frontend Form)  

## Workflow
### 1. Data Preparation
- Dataset: Iris Flower Dataset (150 samples, 4 features, 3 species)
- Features: Sepal Length, Sepal Width, Petal Length, Petal Width
- Target: Species

### 2. Model Training
- Algorithm: Logistic Regression
- Preprocessing: StandardScaler
- Output: `model.pkl` (trained model), `scaler.pkl` (scaler)

### 3. Deployment
- Flask app serves a web interface to input features
- Model predicts species based on inputs

## How to Run
1. **Install dependencies**
```bash
pip install pandas scikit-learn flask
```
2. **Train model**
```bash
python model_training.py
```
3. **Run Flask app**
```bash
python app.py
```
4. **Open browser**
```
http://127.0.0.1:5000
```
5. Enter Sepal/Petal measurements → Click **Predict** → See predicted species.

## Example Output
**Input**
```
Sepal Length: 5.1  
Sepal Width: 3.5  
Petal Length: 1.4  
Petal Width: 0.2
```
**Output**
```
Predicted Species: setosa
```
