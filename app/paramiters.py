import numpy as np

def calc_daily_sigma_mu(data:np.ndarray)->list:
    data = np.array(data).astype(float)
    
    log_ret = np.log(data[1:]/ data[:-1])
    mu_day = np.mean(log_ret)
    sigma_day = np.std(log_ret)
    
    return [mu_day,sigma_day]
    