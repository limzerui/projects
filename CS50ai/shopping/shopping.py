import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")



def load_data(filename):
    
    evidence=[]
    labels=[]
    months = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}
    visitors = {'Returning_Visitor':1, 'New_Visitor':0, 'Other': 0}
    bools = {'TRUE':1, 'FALSE':0}
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            line=[]
            line.append(int(row['Administrative']))
            line.append(float(row['Administrative_Duration']))
            line.append(int(row['Informational']))
            line.append(float(row['Informational_Duration']))
            line.append(int(row['ProductRelated']))
            line.append(float(row['ProductRelated_Duration']))
            line.append(float(row['BounceRates']))
            line.append(float(row['ExitRates']))
            line.append(float(row['PageValues']))
            line.append(float(row['SpecialDay']))
            line.append(months[row['Month']])
            line.append(int(row['OperatingSystems']))
            line.append(int(row['Browser']))
            line.append(int(row['Region']))
            line.append(int(row['TrafficType']))
            line.append(visitors[row['VisitorType']])
            line.append(bools[row['Weekend']])

            evidence.append(line)

            labels.append(bools[row['Revenue']])

        return evidence, labels



def train_model(evidence, labels):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """


def evaluate(labels, predictions):

    #labels have 0 and 1, 1 being that they bought and 0 being didnt buy
    #predictions have 0 and 1 too

    #sensitivity means those that correctly predicted / total that are 0
    #specificity means that correctly predicted/ total that are 1
    total_0 = 0
    total_1 = 0
    correct_0 = 0
    correct_1 = 0
    for i in range(len(predictions)):
        if labels[i] == 0:
            total_0 +=1
            if labels[i] == predictions[i]:
                correct_0 +=1
        elif labels[i] == 1:
            total_1 +=1
            if labels[i] == predictions[i]:
                correct_1 +=1
        
        i+=1
    specificity = correct_0/total_0
    sensitivity = correct_1/total_1
    return sensitivity, specificity 



    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """


if __name__ == "__main__":
    main()
