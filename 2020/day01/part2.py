target_sum = 2020
with open('./input','r') as fh:
    expenses = fh.read().splitlines()
    expenses = [int(expense) for expense in expenses]
    expensesCnt = len(expenses)

    for firstIdx in range(0, expensesCnt-1):
        tripletSet = set()
        first = expenses[firstIdx]
        twinsTarget = target_sum - first
        for secondIdx in range(firstIdx+1, expensesCnt):
            second = expenses[secondIdx] 
            third = twinsTarget - expenses[secondIdx] 
            if third in tripletSet:   
                print(first * second * third) 
                break
            tripletSet.add(second)
