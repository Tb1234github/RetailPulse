# RetailPulse
# RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

## Overview

RetailPulse is an AI-powered retail analytics platform designed to help businesses gain insights into customer behavior, predict future demand, optimize inventory, and identify customers at risk of churn.

The platform combines machine learning, forecasting techniques, interactive dashboards, and MLOps practices to provide data-driven decision support for retail businesses.

---

## Features

### Data Analytics

* Dataset upload and processing
* Exploratory Data Analysis (EDA)
* Missing value analysis
* Correlation analysis
* Sales trend visualization

### Customer Segmentation

* RFM (Recency, Frequency, Monetary) Analysis
* K-Means Clustering
* DBSCAN Clustering
* Customer segment visualization

### Demand Forecasting

* Prophet Forecasting
* LSTM Forecasting
* Hybrid Forecasting (Prophet + LSTM)
* What-if scenario analysis

### Churn Prediction

* XGBoost-based churn prediction
* Customer churn risk identification
* Feature importance analysis
* SHAP explainability

### Inventory Optimization

* Reorder point calculation
* Safety stock calculation
* Suggested inventory recommendations

### Monitoring & Deployment

* Docker containerization
* Kubernetes deployment manifests
* GitHub Actions CI/CD pipeline
* Prometheus monitoring
* Grafana dashboards

---

## Technology Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost
* Prophet
* TensorFlow (LSTM)

### MLOps & Deployment

* Docker
* Kubernetes
* GitHub Actions
* Prometheus
* Grafana

---

## Project Structure

RetailPulse/

├── app.py

├── data/

│   └── online_retail_II.xlsx

├── outputs/

│   ├── cleaned_retail.csv

│   ├── customer_segments.csv

│   ├── forecast.csv

│   ├── hybrid_forecast.csv

│   ├── inventory_plan.csv

│   └── churn_customers.csv

├── pages/

│   ├── EDA_dashboard.py

│   ├── Customer_analytics.py

│   ├── Demand_forecasting.py

│   ├── Inventory_optimization.py

│   ├── Real_metrics.py

│   └── Export_reports.py

├── monitoring/

│   └── prometheus.yml

├── k8s/

│   ├── deployment.yaml

│   └── service.yaml

├── .github/

│   └── workflows/

│       └── retailpulse.yml

├── Dockerfile

├── requirements.txt

└── README.md

---

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/RetailPulse.git

cd RetailPulse

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py

---

## Docker Deployment

Build Docker Image:

docker build -t retailpulse .

Run Container:

docker run -p 8501:8501 retailpulse

---

## GitHub Actions CI/CD

The project includes a GitHub Actions workflow that automatically:

* Installs dependencies
* Validates Python files
* Executes build checks

on every push to the main branch.

---

## Monitoring

Prometheus is used for metrics collection.

Grafana is used for visualization and dashboard monitoring.

---

## Load Testing

Load testing was performed using Locust.

Metrics evaluated:

* Response Time
* Requests Per Second (RPS)
* Failure Rate

---

## Dataset

Online Retail II Dataset

Contains:

* Customer Transactions
* Product Information
* Sales Records
* Invoice Data

---

## Future Enhancements

* Real-time demand forecasting
* Recommendation engine
* Multi-store analytics
* Cloud-native deployment
* Automated model retraining

---

## Author

Trisit Biswas

Final Year Project

RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform
