def Run_index(r,b,t):
    Ri = r*(r/b)*(1+(r/t))
    return Ri

def Avg_run_index(Data):
    Total, outs = 0,0
    for i in range(len(Data)):
        Total += Run_index(Data[i]["r"],Data[i]["b"],Data[i]["t"])
        outs += 1 if not Data[i]["s"] else 0
    if outs == 0:
        return 'infinite'
    else:
        Ari = Total/outs
        return '%.4f'%Ari