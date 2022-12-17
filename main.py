# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date, datetime

from PriceHistoryExtraction import getPrice, extractcloseData, calculateMVA, calculateEMA
import sys

from com.nsema.symbols.Symbols import Symbols
from nsepy.symbols import get_symbol_list
import pandas as pd


def mvaCaculator(symbol, today):
    # Calculate Moving Average of a stock
    symbolData = Symbols()
    symboldf = get_symbol_list()
    print(symboldf)
    for ind in symboldf.index:
        symbolforExtraction = symboldf['SYMBOL'][ind]
        #symbolforExtraction = 'DTIL'
        symbol = symbolforExtraction
        if symbol == 'DVL':
            print('Skip DVL stock')
        else:
            print(symbolforExtraction)
            date_object = datetime.strptime(today, '%Y-%m-%d').date()
            finaldta = getPrice(symbol=symbolforExtraction,
                                today=date_object, numdays=20)
            if finaldta.empty:
                print('Skipping all further process for symbol ' + symbol + ' as the price data is empty')
            else:
                finaldf = finaldta.tail(1)
                print(finaldf['Close'].item())
                close = finaldf['Close'].item()
                print("Value of close => " + str(close))
                # print("Any of close => "+ any(close))
                sma = calculateMVA(finaldta).astype('float')
                print("Simple Moving average: " + str(sma))
                extractcloseData(finaldta)
                # finaldta.to_csv(str(symbol) + '.csv')
                ema = calculateEMA(symbol=symbolforExtraction, df=finaldta, numdays=20)
                if ema == None:
                    print('Skipping all further process for symbol ' + symbol + ' as the price data is empty')
                else:
                    print("------------Final Results------------")
                    print("| SMA 20 for " + symbol + " is " + str(sma) + "  |")
                    print("| EMA 20 for " + symbol + " is " + str(ema) + " |")
                    print("| Close Rate for " + symbol + " is " + str(close) + " |")
                    print("|The data is available in " + str(symbol) + ".csv |")
                    print("-------------------------------------")
                    if close > ema:
                        data = [{'Symbol': symbolforExtraction, 'Close': str(close), 'sma': sma, 'ema': ema}]
                        df = pd.DataFrame(data, columns=['Symbol', 'Close', 'sma', 'ema'])
                        print(df)
                        symbolData.add_to_list(symbol=df)
                    else:
                        print("Close price is not greater than EMA for " + symbolforExtraction)
                        print("------------Final Details below------------")
                        print("| SMA 20 for " + symbol + " is " + str(sma) + "  |")
                        print("| EMA 20 for " + symbol + " is " + str(ema) + " |")
                        print("| Close Rate for " + symbol + " is " + str(close) + " |")
                        print("|The data is available in " + str(symbol) + ".csv |")
                        print("-------------------------------------")
    symbolData.extract_data_to_csv()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = len(sys.argv)
    print("Total arguments passed:", n)
    mvaCaculator(sys.argv[1], sys.argv[2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
