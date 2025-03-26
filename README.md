# Customer Churn Prediction Project

Hey there! Welcome to my Customer Churn Prediction project—I put this together to figure out which customers might ditch a service, and I’m pretty stoked with how it turned out! It’s got data analysis, a solid prediction model, and even a little web app to play with. Whether you’re into data science or just curious, here’s the scoop on what I built and how you can check it out.

## What’s This All About?

- I wanted to tackle a real-world problem: predicting when customers might leave a company—like a telecom service, for instance.
- The idea? Dig into customer data, spot patterns, and build a tool to guess who’s at risk of churning, so businesses could maybe keep them around with some smart moves.
- It’s split into three big pieces: exploring the data, training a model, and serving it up with a Flask app—kinda like my flight fare project, but for churn this time!

## What’s Inside?

- Here’s the rundown of what you’ll find in this repo:
  - **`churn_analysis.ipynb`**: My Jupyter Notebook where I dive into the data—think charts, stats, and insights about what makes customers stick or split.
  - **`churn_prediction.ipynb`**: Another notebook where I whip up a machine learning model (XGBoost, because it’s clutch) to predict churn, plus save it for later use.
  - **`app.py`**: The Flask backend that powers the web app—takes user inputs and spits out churn predictions.
  - **`templates/index.html`**: The front-end HTML for the Flask app—nice form to plug in customer details and see the results.
  - **`.gitignore`**: Keeps big files (like datasets and models) out of the repo—more on that below!

## How It Works

- **Analysis**:
  - I start with `churn_analysis.ipynb`—load up a dataset (like Telco Customer Churn from Kaggle), poke around with Pandas, and plot stuff with Seaborn.
  - You’ll see bar charts of churn rates, boxplots of tenure vs. charges, maybe a heatmap of what’s tied to leaving—helps me figure out the big drivers.
- **Prediction**:
  - In `churn_prediction.ipynb`, I clean the data (drop junk, encode categories), split it into train/test, and train an XGBoost model—ends up pretty accurate, like 85-90% usually.
  - Saves the model as `churn_model.sav` and feature columns so the app can use them.
- **Web App**:
  - Fire up `app.py`, and it runs a Flask server—hit `http://127.0.0.1:5000/` in your browser.
  - `index.html` gives you a form: punch in customer details (like tenure, contract type), hit predict, and bam—tells you if they’re likely to churn.

## Getting Started

- Wanna run this yourself? Here’s how to get it rolling:
  - **Clone the Repo**:
    ```bash
    git clone https://github.com/iamshaneofc/customer-churn-project.git
    cd customer-churn-project
