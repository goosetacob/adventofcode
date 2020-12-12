with open('./input','r') as fh:
    questionnaire = fh.readline()
    groupCnts = []

    currentGroupSet = set()
    while questionnaire:
        yesIDs = set(list(questionnaire.strip()))
        if len(yesIDs) == 0:
            groupCnts.append(len(currentGroupSet))
            currentGroupSet = set()

        currentGroupSet.update(yesIDs)

        questionnaire = fh.readline()

    print(f'sum of group counts: {sum(groupCnts)}')
