with open('./input','r') as fh:
    questionnaire = fh.readline()
    currentGroupSet = set(list(questionnaire.strip()))
    groupCnts = []

    while questionnaire:
        if questionnaire.strip() == '':
            groupCnts.append(len(currentGroupSet))
            questionnaire = fh.readline()
            currentGroupSet = set(list(questionnaire.strip()))
            continue

        currentGroupSet = currentGroupSet.intersection(set(list(questionnaire.strip())))
        questionnaire = fh.readline()

    print(f'sum of group counts: {sum(groupCnts)}')

