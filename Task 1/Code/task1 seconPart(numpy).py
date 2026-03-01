import numpy as np
x=[50, 60, 80, 100, 120] 
y=[150, 180, 240, 300, 330] 

x_array=np.array(x)
y_array=np.array(y)

x_array=np.reshape(x_array, (-1, 1))

ones = np.ones((x_array.shape[0],1))
x_new = np.hstack((ones, x_array))

theta=np.linalg.inv(x_new.T @ x_new) @ x_new.T @ y_array
print("Theta:", theta)

house_90 = np.array([1, 90])        
price_90 = house_90 @ theta        
print("Predicted price for 90 m²:", f"{price_90:.2f}")
