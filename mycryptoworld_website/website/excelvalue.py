import pandas as pd

def getvalue(exid):
    pf = pd.read_excel('C:/Users/carme/Documents/mycryptoworld_website/mycryptoworld_website/website/ProfileData.xlsx')
    return(pf.loc[exid, 'value1'], pf.loc[exid, 'value2'])