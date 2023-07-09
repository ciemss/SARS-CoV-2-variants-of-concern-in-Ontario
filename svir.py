import numpy as np

def svir(t, y, beta, beta_v1, beta_v2, beta_R, gamma, nu_v1, nu_v2, nu_R, mu, mu_I, mu_IV):
    # retrieve current populations
    nv = 2  # number of viruses simulated
    ind = 0
    S = y[ind]; ind += 1  # original susceptible
    SVR = y[ind]; ind += 1  # lost immunity after vaccination or recovery
    V1 = y[ind:ind+2]; ind += 2  # one-dose vaccination
    V2 = y[ind:ind+2]; ind += 2  # fully vaccinated
    I = y[ind:ind+nv]; ind += nv  # infected
    IV = y[ind:ind+nv]; ind += nv  # infected even with vaccination
    IR = y[ind:ind+nv]; ind += nv  # infected again after recovery
    R = y[ind:ind+nv]; ind += nv  # recovered
    R2 = y[ind]; ind += 1  # recovered after getting both variants

    # get time-dependent parameters
    vr1, vr2 = get_vaccine_rate(t)
    beta_scale = get_beta(t)
    beta *= beta_scale
    beta_v1 *= beta_scale
    beta_v2 *= beta_scale
    beta_R *= beta_scale

    # compute time derivatives
    dSdt = - np.sum(beta * S * (I + IV + IR)) - np.sum(vr1 * S) + mu * (1 - S)
    dSVRdt = nu_v1 * np.sum(V1) + nu_v2 * np.sum(V2) + np.sum(nu_R * R) + nu_R * R2 - np.sum(beta * SVR * (I + IV + IR)) - mu * SVR
    dV1dt = vr1 * S - vr2 * V1 - nu_v1 * V1 - np.sum(beta_v1 * (V1 @ (I + IV + IR))) - mu * V1
    dV2dt = vr2 * V1 - nu_v2 * V2 - np.sum(beta_v2 * (V2 @ (I + IV + IR))) - mu * V2
    dIdt = beta * S * (I + IV + IR) + beta * SVR * (I + IV + IR) - gamma * I - mu_I * I
    dIVdt = np.sum(beta_v1 * (V1 @ (I + IV + IR))) + np.sum(beta_v2 * (V2 @ (I + IV + IR))) - gamma * IV - mu_IV * IV
    dIRdt = beta_R * np.flip(R) * (I + IV + IR) - gamma * IR - mu * IR
    dRdt = gamma * (I + IV + IR) - nu_R * R - beta_R * np.flip(R) * (I + IV + IR) - mu * R
    dR2dt = np.sum(gamma * IR) - nu_R * R2 - mu * R2

    # simulate mutation of WT into variants and importation
    if 300 < t < 360:  # alpha appears
        dWTtoA = 0e-5 * dIdt[0]  # don't assume mutation
        dIdt[0] -= dWTtoA
        dIdt[1] += dWTtoA + ((t - 250) / 60) * 10 / 14570000  # people enter Ontario with alpha
    elif 385 < t < 445:
        dIdt[2] = ((t - 385) / 60) * 40 / 14570000  # delta was born

    yp = np.concatenate([dSdt, dSVRdt, dV1dt, dV2dt, dIdt, dIVdt, dIRdt, dRdt, dR2dt])

    return yp
