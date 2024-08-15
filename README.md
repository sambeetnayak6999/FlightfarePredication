# FlightfarePredication

Project Overview

This project focuses on predicting the price of flight tickets based on various features such as airline, source, destination, departure time, arrival time, duration, and the number of stops. The model is built using historical data and aims to provide accurate predictions to help travelers and businesses make informed decisions.

Features

Data Collection: The dataset used for this project is collected from [Kaggle](https://www.kaggle.com/), which includes several thousand flight records.
Data Preprocessing: Includes handling missing values, feature encoding, feature selection, and data normalization.
Model Building: Various machine learning models were tested, including Linear Regression, Decision Trees, Random Forests, and Gradient Boosting Machines.
Hyperparameter Tuning: Applied Grid Search and Random Search for hyperparameter tuning to improve model performance.
Evaluation Metrics: Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared score were used to evaluate the models.
Visualization: Data visualization techniques were employed to gain insights into the data and model performance.
Deployment: The model was deployed using Flask/Streamlit for a user-friendly web interface that allows users to input flight details and get price predictions.

Technologies Used

Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Flask/Streamlit
Tools: Jupyter Notebook, Git, GitHub
Deployment Platform: Heroku/Streamlit

Dataset

The dataset used in this project is available on Kaggle and contains the following features:
  - Airline: The name of the airline.
  - Date of Journey: The date on which the flight is scheduled.
  - Source: The starting location of the flight.
  - Destination: The ending location of the flight.
  - Route: The route taken by the flight.
  - Dep_Time: The departure time of the flight.
  - Arrival_Time: The arrival time of the flight.
  - Duration: The duration of the flight.
  - Total_Stops: Total number of stops the flight makes.
  - Additional_Info: Additional information about the flight.
  - Price: The target variable representing the price of the flight.

 Model Performance

- Linear Regression: RMSE: X, R-squared: X
- Random Forest: RMSE: X, R-squared: X
- Gradient Boosting: RMSE: X, R-squared: X


Future Enhancements

- Incorporate more features such as passenger class and ticket type.
- Experiment with deep learning models for potentially better accuracy.
- Develop a mobile-friendly interface for ease of use on different devices.

Contributions

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.


Acknowledgments

- The dataset was provided by [Kaggle](https://www.kaggle.com/).
