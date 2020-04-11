'''
Description:
Simple neural network with one percepton to do a liear regression. 
Used example: multiplying by 3 
Method of optimization (finding parameters for linear function): gradient descent (in each step it adds (or not) learning rate to params)
'''


# returns linear function result 
def predict(x, params):
    return params['b'] + x*params['w']

# calculate square errors for training inputs x_t in comparison to traning outputs y_t using linear params
def calc_error(x_t,y_t,params):
    cum_error = 0
    for x,y in zip(x_t,y_t):
        cum_error += pow(((params['b'] + x*params['w']) - y),2)
    return cum_error

#traning data
x_t = [i for i in range(10)]
y_t = [y*3 for y in x_t]

#initials linear params
mod_params = {'w':0,'b':0}

#number of learning rounds
epochs = 1000

#change during one learning round
learning_rate = 0.03

#some data to exam after learning
x_test = [1,2,3,0,-5,1.5,13]

for i in range(epochs):
    candidates = list()
    
    #calculating all possibilities of changing linear parameters
    #1 w+ b-
    cand_params = mod_params.copy()
    cand_params['w'] += learning_rate
    cand_params['b'] -= learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #2 w+ b0
    cand_params = mod_params.copy()
    cand_params['w'] += learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #3 w+ b+
    cand_params = mod_params.copy()
    cand_params['w'] += learning_rate
    cand_params['b'] += learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #4 w0 b-
    cand_params = mod_params.copy()
    cand_params['b'] -= learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #5 w0 b0
    cand_params = mod_params.copy()
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #6 w0 b+
    cand_params = mod_params.copy()
    cand_params['b'] += learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #7 w- b-
    cand_params = mod_params.copy()
    cand_params['w'] -= learning_rate
    cand_params['b'] -= learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #8 w- b0
    cand_params = mod_params.copy()
    cand_params['w'] -= learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    #9 w- b+
    cand_params = mod_params.copy()
    cand_params['w'] -= learning_rate
    cand_params['b'] += learning_rate
    cand_error = calc_error(x_t,y_t, cand_params)
    candidates.append({"params":cand_params,"error":cand_error})
    
    #crapy hardcoded value
    min_cand_error = 9999999999
    go_params = mod_params.copy()
    
    #looking for candidate with lowest error
    for cand in candidates:
      if cand['error'] < min_cand_error:
        go_params = cand['params'].copy()
        min_cand_error = cand['error']
    
    if i%100 == 0:
      print('params: ' + str(go_params) + ' error:' + str(min_cand_error))
      
    mod_params = go_params.copy()
    
#exam it!
for x in x_test:
    print(str(x) + ' * 3 =' + ' ' + str(predict(x,mod_params)))