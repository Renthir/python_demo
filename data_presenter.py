data = open('CupcakeInvoices.csv', 'r')
# print(data.read())

for sale in data:
    sale = sale.split(',')
    print(sale[2])
    print(int(sale[3]) * float(sale[4].strip('\n')))

data.close()
