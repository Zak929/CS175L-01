#expensePieChart.py
#Zak Ahmed
#CS-175L-01
#Spring 2022

import matplotlib.pyplot as plt

def main():
    costs = openfile()
    piechart(costs)

def openfile():
    try:
        costs = []
        costlist = open('expenses.txt','r')
        for cost in costlist:
            datalist = cost.strip('\n')
            cols = datalist.split('\t')
            costs.append(cols)
        return costs
    except Exception as e:
        print(e)
        
def piechart(costs):
    values = []
    labels = []
    for item in costs:
        values.append(item[1])
        labels.append(item[0])
    plt.pie(values,labels=labels)
    plt.title('Monthly Expenses')
    plt.show()
    
main()
