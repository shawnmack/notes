'''
DEEP LEARNING VS MACHINE LEARNING

deep learning is good for uncovering more intricate patterns
tend to underperform less complex patterns
both can process big data

all these do is uncover patterns with probabilities

supervised learning, labelled data, task

unsupervised labelled data shows clusters, not patterns

reinforcement, labelled data win/lose, defined rules










***LINEAR REGRESSION****

Linear regression attempts to model the relationship between two variables by fitting
a linear equation to observed data. One variable is considered to be an explanatory variable,
 and the other is considered to be a dependent variable.

line of best fit y= wx+b
weight and bias, make the line fit the best

COST AND LOSS
cost is the difference between the data point and the line of best fit

y is the real data point
y^ is the predicated point based on the line of best fit 
J= SIGMA(yi-y^i)^2
    __________
        N

SIGMA= SUM
N= SAMPLE SIZE

choose weight + bias
check loss
if lower then keep going that way
if higher than do the opposite

GLOBAL MINIMUM LINE OF BEST FIT

the amount of precision you use can affect your results

with neural networks you don't need to use straight lines you can have
methods that generate very complex functions easily that actually match the data

OVERDESCRIBING OVERFITTING
    you can run the problem of having an equation that is TOO specific and will
    fall apart when you introduce/find more data
    you can never have enough data if we are dealing with real world
    there will be a parameter or factor that you don't know about


TRAIN AND TEST/VALUATION

neural net


input- hidden layers - output

NON linearity SIGMOID = curve of values between 0-1
activation function

y = wx + b     y--->zed      z=h(y1)  y2=wz1+b2

                    
                    
y2 = wzsub1 + b

each input will have a different w, and bias should be the same


so a neural net does linear regression then adding an activation function, to turn the number into a value between 0-1
it does that over and over until the output layer


in each hidden row each node will have a different 


'''
