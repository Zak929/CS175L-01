#CS175L-01
#Zak Ahmed
#stocks
COMMISSION_RATE = float(input('What was the commission rate?'))
NUM_SHARES = int(input("What was the number of shares?"))
PURCHASE_PRICE = float(input('What was the purchase price per stock?'))
SELLING_PRICE = float(input('What was the selling price? per stock'))
amountPaidForStock = 0
purchaseCommission = 0
totalPaid = 0
stockSoldFor = 0
sellingCommission = 0
totalReceived = 0
profitOrLoss = 0
totalCommission = 0
amountPaidForStock = NUM_SHARES*PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE*amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES*SELLING_PRICE
sellingCommission = COMMISSION_RATE*stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
totalCommission = purchaseCommission + sellingCommission
print(f'Amount paid for stock: ${amountPaidForStock}')
print(f'Commission paid on the purchase: ${purchaseCommission}')
print(f'Amount the stock sold for: ${stockSoldFor}')
print(f'Commission paid on the sale: ${sellingCommission}')
print(f'Total commission paid: ${totalCommission}')
print(f'Profit (or loss if negative): ${profitOrLoss}')
