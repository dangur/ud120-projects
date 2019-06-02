#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from sklearn.covariance import EllipticEnvelope
    # ee = EllipticEnvelope()
    # ee.fit(ages)
    # ee.fit(net_worths)
    cleaned_data = []
    diffs = []

    ### your code goes here
    # print 'predictions'
    # print predictions
    # Get diffs
    i = 0
    for prediction in predictions:
        net_worth = float(net_worths[i])
        age = int(ages[i])
        diff = float(prediction - net_worth)
        tupe = (age, net_worth, diff)
        # print tupe
        cleaned_data.append(tupe)
        i = i + 1

    # Sort
    cleaned_data.sort(key=lambda x: x[2])

    # Find threshold
    data_that_is_cleaned = []
    i = 0
    for cleaned_datum in cleaned_data:
        if i < 81:
            print cleaned_datum
            data_that_is_cleaned.append(cleaned_datum)
        i = i + 1

    cleaned_data = data_that_is_cleaned
    # Build list of tuples

    # cleaned_data = [(5, 100, 1), (9, 200, 2)]

    # print cleaned_data

    return cleaned_data
