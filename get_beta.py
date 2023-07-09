from datetime import datetime

# simulate lockdown
def get_beta(t):
    ind = 0

    # first day of simulation
    day0 = datetime.strptime('1-jan-2020', '%d-%b-%Y')

    # state of emergency and such [2]
    tlock = []
    tunlock = []
    scale = []
    
    dates = ['23-mar-2020', '17-jul-2020', '17-jul-2020', '9-oct-2020', '9-oct-2020', '23-nov-2020', 
             '23-nov-2020', '5-jan-2021', '5-jan-2021', '5-mar-2021', '5-mar-2021', '13-apr-2021', 
             '13-apr-2021', '11-jun-2021', '11-jun-2021', '2-jul-2021', '2-jul-2021', '16-jul-2021', 
             '16-jul-2021', '1-sep-2021', '1-sep-2021', '1-nov-2021', '1-nov-2021', '1-jan-2022', 
             '1-jan-2022', '1-jan-2023']
    
    scales = [0.4, 0.55, 0.6, 0.55, 0.3, 0.4, 0.15, 0.2, 0.3, 0.35, 0.4, 0.5, 0.4]
    
    for i in range(0, len(dates), 2):
        tlock.append((datetime.strptime(dates[i], '%d-%b-%Y') - day0).days)
        tunlock.append((datetime.strptime(dates[i+1], '%d-%b-%Y') - day0).days)
        scale.append(scales[ind])
        ind += 1

    ilock = [i for i, x in enumerate(tlock) if x <= t]
    iunlock = [i for i, x in enumerate(tunlock) if t < x]
    ii = list(set(ilock) & set(iunlock))
    
    if len(ii) > 1:
        print(t, ii)
    if not ii:
        beta_scale = 1
    else:
        beta_scale = scale[ii[0]]
    
    return beta_scale
