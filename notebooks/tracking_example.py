import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import json

EXPERIMENT_NAME = 'test containers'
RUN_NAME = "test with linear 2"

from dotenv import load_dotenv
load_dotenv()

      
def simulate_data(seed=42, size=100):
    np.random.seed(seed)
    X = np.random.rand(size, 1) * 10
    y = 3 * X.squeeze() + 4 + np.random.randn(size) * 2
    return pd.DataFrame(data={'X': X.squeeze(), 'y': y})

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return y_pred, {"mse": mse, "r2": r2}

def create_plot(y_test, y_pred):
    fig = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual', 'y': 'Predicted'}, title="Actual vs Predicted")
    fig.update_traces(marker=dict(size=12, color='rgba(152, 0, 0, .8)', line=dict(width=2, color='DarkSlateGrey')))
    return fig

def main():
    data = simulate_data()
    data_length = len(data)
    X_train, X_test, y_train, y_test = train_test_split(data[['X']], data['y'], test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    y_pred, metrics = evaluate_model(model, X_test, y_test)
  
    params = {"data_length": data_length}
    metadata = {
        "data": "Simulated data",
        "model": "LinearRegression",
        "description": "A simple linear regression model trained on simulated data.",
        "coefficients": model.coef_.tolist(),
        "intercept": model.intercept_.tolist() if isinstance(model.intercept_, np.ndarray) else model.intercept_
    }
    fig = create_plot(y_test, y_pred)

    return metrics, params, fig, model, metadata

if __name__ == "__main__":
    # mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(EXPERIMENT_NAME)
    with mlflow.start_run(run_name=RUN_NAME):
        metrics, params, fig, model, metadata = main()
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.log_figure(fig, "plot.html")
        mlflow.log_dict(metadata, "metadata.json")
        mlflow.sklearn.log_model(model, "linear-regression-model")
