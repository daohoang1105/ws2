import pandas as pd

def testt(q):
    newStr = __file__.replace('functionX.py','SGVN.xlsx')
    dfz = pd.read_excel(newStr)
    detail = dfz[dfz.SN  == q].detail
    for de in detail:
        return de
    
    


if __name__ == "__main__":
    testt()