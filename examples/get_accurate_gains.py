import robin_stocks as r

'''
Robinhood includes dividends as part of your net gain. This script removes
dividends from net gain to figure out how much your stocks/options have paid
off.

Note: load_portfolio_profile() contains some other useful breakdowns of equity.
Print profileData and see what other values you can play around with.

'''

login = r.login()

profileData = r.load_portfolio_profile()
#print(profileData)
allTransactions = r.get_bank_transfers()

deposits = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'deposit') and (x['state'] == 'completed'))
withdrawals = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'withdraw') and (x['state'] == 'completed'))
money_invested = deposits - withdrawals

dividends = r.get_total_dividends()
percentDividend = dividends/money_invested*100

totalGainMinusDividends =float(profileData['extended_hours_equity'])-dividends-money_invested
percentGain = totalGainMinusDividends/money_invested*100
newNetWorth = (1+(percentGain/100))*money_invested
print("The total money invested is ${:,.2f}".format(money_invested))
print("The net worth has increased {:0.2}% due to dividends".format(percentDividend))
print("The net worth has increased {:0.3}% due to other gains".format(percentGain))
print("Total current principal at risk: ${:,.2f}".format(newNetWorth))
