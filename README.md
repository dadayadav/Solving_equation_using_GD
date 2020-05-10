# Solving_equation_using_GD
### To understand <code style="font:solid; color:'blue'">Gradient Descent</code> algorithm, I make a simple linear equation solver program, we use mse as a loss function.
<p>-------------------------------------------</p>
In this <code>model_code.py</code> file:
```python
#input 
# ---------------------------------------------------------
A = np.array([[1,1,0,0], [0,0,1,-1], [1,0,1,0], [0,1,0,1]])
# we also need b matrix
b = np.array([8,6,13,8]).reshape((4,1))
# we need a random x initializer with shape = (4,1)
x = np.random.rand(b.shape[0],1) 
# ---------------------------------------------------------
```
Make a matrix such that <code>Ax = b</code> can satisfy.
For the above example eq are:
x1+x2 = 8   # here assume 0*y1+0*y2
y1-y2 = 6   # assume 0*x1+0*x2
x1+y1 = 12  # assume 0*x2+x*y2
x2+y2 = 8   # assume 0*x1+0*y1

Then, 
Matrix A = [1 1 0 0
            0 0 1 -1
            1 0 1 0
            0 1 0 0
            ]
and b = [8 6 12 8]
# ---------------------------------------------------------

Now, you can play with learning_rate, tol, iteration etc



Also, you can visualize live error plot by uncomment these line of code
``` python
'''
 data = collections.defaultdict(list)
 for i in mse_:
     data['mse'].append(mse(Z))
     live_plot(data)
'''   
```
## Further you can try to error function, optimization, solving nonlinear equation etc.

