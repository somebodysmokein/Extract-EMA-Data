from nsepy import get_history
from datetime import date, timedelta
import pandas as pd
def getPrice( symbol, today,  numdays):
    startdt=today- timedelta(days=numdays*2)
    data = get_history(symbol=symbol, start=startdt, end=today)
    print("Price History of " + symbol + " from " + str(data.tail(numdays).index[0]) + " to expiry date: " + str(today))
    print (data.tail(numdays))
    #print(data.columns)
    #print(data["Close"])
    return data.tail(numdays)


def extractcloseData(df):
    print("Closing data for last 20 days ")
    print (df['Close'])

def calculateMVA(df):
    #print(df.columns)
    mva=df["Close"].mean()
    #print("Simple Moving average: "+str(mva))
    return mva

def calculateEMA(symbol,df,numdays):
    lastRow=df.tail(1)
    #print(lastRow)
    closingPriceToday=lastRow["Close"]
    #print("closingPriceToday : "+str(closingPriceToday))
    #print("Index"+ str(df.index[0]))
    priordf = getPrice(symbol=symbol, today=df.index[0]-timedelta(days=1)
                                          , numdays=numdays)
    #extractcloseData(priordf)
    #print(priordf)
    #print(priordf.count)
    prevEMA=calculateMVA(priordf)
    #print("First EMA => "+str(prevEMA))
    finalEMA=0
    for ind in df.index:
        currentEMA=emaforDate(prevEMA,df['Close'][ind],numdays)
        #print("EMA for "+str(ind)+"  "+str(currentEMA))
        #cummulativeEMA=prevEMA+currentEMA
        prevEMA=currentEMA
        finalEMA=currentEMA

    print("Final EMA :"+ str(finalEMA))
    return finalEMA





def emaforDate(emayesterDay, today, numdays):
        multiplier = 2 / (numdays + 1)
        emaToday=today*multiplier+emayesterDay*(1-multiplier)
        return emaToday
