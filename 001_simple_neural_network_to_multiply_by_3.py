def predict(x, params):
    return params['b'] + x*params['w']

def calc_error(x_t,y_t,params):
    cum_error = 0
    for x,y in zip(x_t,y_t):
        cum_error += pow(((params['b'] + x*params['w']) - y),2)
    return cum_error

x_t = [i for i in range(10)]
y_t = [y*3 for y in x_t]
mod_params = {'w':0,'b':0}
epochs = 1000
learning_rate = 0.03

x_test = [1,2,3,0,-5,1.5,13]

for i in range(epochs):
    candidates = list()
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
    
    min_cand_error = 9999999999
    go_params = mod_params.copy()
    for cand in candidates:
      if cand['error'] < min_cand_error:
        go_params = cand['params'].copy()
        min_cand_error = cand['error']
    
    if i%100 == 0:
      print('params: ' + str(go_params) + ' error:' + str(min_cand_error))
      
    mod_params = go_params.copy()
    
for x in x_test:
    print(str(x) + ' * 3 =' + ' ' + str(predict(x,mod_params)))    