# eq: X1+X2 = 8, X1+Y1 = 13, X2+Y2 = 8, Y1-Y2 = 6
# for this we need a A matrix [X1, X2, Y1, Y2]

#import library
from IPython.display import clear_output
from matplotlib import pyplot as plt
import collections
import numpy as np
%matplotlib inline
# code
A = np.array([[1,1,0,0], [0,0,1,-1], [1,0,1,0], [0,1,0,1]])
# we also need b matrix
b = np.array([8,6,13,8]).reshape((4,1))
# we need a random x initializer with shape = (4,1)
x = np.random.rand(4,1) 
print("A:", A)
print()
print("b:",b)
print()
print("x:",x)
# Now we evaluate
def live_plot(data_dict, figsize=(7,5), title=''):
    clear_output(wait=True)
    plt.figure(figsize=figsize)
    for label,data in data_dict.items():
        plt.plot(data, label=label)
    plt.title(title)
    plt.grid(True)
    plt.xlabel('epoch')
    plt.legend(loc='center left') # the plot evolves to the right
    plt.show();

def rounding(x):
    ret = []
    for i in x:
        start = str(i).split(".")[0]
        i  = str(i).split(".")[-1][:2] 
        if not ((int(i)+1)%10):
            ret.append(float(start+"."+(str(int(i)+1))[:2]))
        elif not ((int(i)+2)%10):
            ret.append(float(start+"."+(str(int(i)+2))[:2]))
        else:
            ret.append(float(start+"."+i))
    return np.array(ret).reshape((len(x), 1))

def mse(x):
    return 0.5*(np.linalg.norm(x, ord=2)**2)
def stop_value(A,b,x):
    return np.linalg.norm(A.T.dot((np.dot(A,x)-b)), ord=2)

# print initial error and eq:
print()
print(f"{np.dot(A,x)-b}")
print()
print(f"mse:{mse(np.dot(A,x)-b)}")

tol = 0
learning_rate = 0.0001
x_copy = x
X = np.dot(A,x_copy)
z = X-b
cost_function = 0.5*((np.linalg.norm(z, ord=2))**2)
it = 0
mse_ = []

while(stop_value(A,b,x_copy)>tol and it<100000):
#     print(stop_value(A,b,x))
    x_copy = x_copy-learning_rate*(A.T.dot((np.dot(A,x_copy)-b)))
    Z = np.dot(A,x_copy)-b
    mse_.append(mse(Z))
    it += 1

# data = collections.defaultdict(list)
# for i in mse_:
#     data['mse'].append(mse(Z))
#     live_plot(data)
    
x_plot = np.arange(len(mse_)).reshape((len(mse_),1))
y_plot = np.array(mse_).reshape((len(mse_),1))
plt.plot(x_plot[:],y_plot[:],color= 'blue')
plt.title("History")
plt.xlabel("iteration")
plt.ylabel("MSE_error")
plt.show()
print()
print("after calculation")
print()
print(f"{np.dot(A,x_copy)-b}")
print()
print(f"mse:{mse(np.dot(A,x_copy)-b)}")
print()
print("The value of variables are:")
print(x_copy)
print()
print("Final value(apprx):")
c = np.squeeze(x_copy)
final_val = rounding(c)
print(final_val)
