target_sum = 2020
with open('./input','r') as fh:
    expenses = fh.read().splitlines()
    expenses = [int(expense) for expense in expenses]
    expenses_set = set(expenses)

    for expense in expenses:
        expense_pair = target_sum - expense
        if expense_pair in expenses_set:
            print(expense * expense_pair)
            break
