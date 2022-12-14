# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date, datetime

from PriceHistoryExtraction import getPrice, extractcloseData, calculateMVA, calculateEMA
import sys

def mvaCaculator(symbol,today):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    date_object =datetime.strptime(today, '%Y-%m-%d').date()
    finaldta= getPrice(symbol='SBIN',
                   today=date_object ,numdays=20)
                   #expdt=date(2022,12,12))

    #print (finaldta)
    #extractcloseData(finaldta)
    sma=calculateMVA(finaldta)
    print("Simple Moving average: " + str(sma))
    extractcloseData(finaldta)
    finaldta.to_csv(str(symbol)+'.csv')
    ema=calculateEMA(symbol='SBIN',df=finaldta,numdays=20)
    print("------------Final Results------------")
    print("| SMA 20 for "+symbol+" is "+str(sma)+"  |")
    print("| EMA 20 for " + symbol + " is "+str(ema)+" |")
    print("|The data is available in "+str(symbol)+".csv |")
    print("-------------------------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = len(sys.argv)
    print("Total arguments passed:", n)
    mvaCaculator(sys.argv[1],sys.argv[2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
