import pandas as pd

def testt(q):
    newStr = __file__.replace('functionX.py','test.csv')
    dfz = pd.read_csv(newStr)
    detail = dfz[dfz.SN  == q].detail
    for de in detail:
        return de
    
    


if __name__ == "__main__":
    testt()