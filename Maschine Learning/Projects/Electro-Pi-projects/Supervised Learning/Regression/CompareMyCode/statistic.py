import numpy as np 

class statistic():
    
  def Mean(values):
    return np.sum(values)/len(values)

  def Variance(values, mean):
    return sum([(x - mean)**2 for x in values]) 

  def Covariance(x, X_mean , y , y_mean):
    cov = 0.0
    for i in range(len(x)):
      cov += (x[i] - X_mean) * (y[i] - y_mean) 
    return cov

  def coefficents(x,covariance,variance,mean_x,mean_y):
    b1 = covariance / variance
    b0 = mean_y - b1 * mean_x
    return [b0, b1]

  def SimpleLinearRegression(train, test,coefficents):
    pred = list()
    b0, b1 = coefficents
    for i in test:
      yhat = b0 + b1 * i
      pred.append(yhat)
    return pred

  def MSE(actual, predicted):
    actual, predicted = np.array(actual), np.array(predicted)
    return np.square(np.subtract(actual,predicted)).mean()


  

      
      