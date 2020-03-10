expected_goals
==============================

A simple expected goals model created using data from [Moneypuck.com](moneypuck.com).

This is a simple machine learning project to show how relatively easy it is to create an xG model. I used a few variables that intuitively try to capture several aspects of different situations that might lead to goals. These include distance from goal, the angle the shot takes towards the goal, and the game sitution (power play, empty net, etc). As it turns out, a few variables can be very predictive of the probability of scoring a goal. Since expected goals is a measure of probability, we require a different approach from usual machine learning metrics like RMSE or a confusion matrix to calibrate and evaluate the model. I show how we can use cross-validation to test several values of hyperparameters to choose the "best "model.

This model is created using PySpark.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
