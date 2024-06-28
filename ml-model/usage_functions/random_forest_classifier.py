import pickle
from sklearn.ensemble import RandomForestClassifier

    
encode = {
    "Not Interested" : 0,
    "Poor" : 1,
    "Beginner" : 2,
    "Average" : 3,
    "Intermediate" : 4,
    "Excellent" : 5,
    "Professional" : 6
}
def get_recommendation(preferences: list) -> list:
    # load the model
    with open('../saved_models/random_forest_classifier.pkl', 'rb') as file:
        randForestClf: RandomForestClassifier = pickle.load(file)
        
    # encode the preferences
    for i in range(len(preferences)):
        preferences[i] = encode[preferences[i]]
        
    # Predict probabilities for each class for each instance in the test set
    probabilities = randForestClf.predict_proba([preferences])

    # Get the top 5 predictions for each instance
    top5_predictions = []
    for prob in probabilities:
        top5_indices = prob.argsort()[-5:][::-1]  # Get the indices of the top 5 probabilities
        top5_classes = [randForestClf.classes_[i] for i in top5_indices]  # Map indices to class labels
        top5_predictions.append(top5_classes)
        
    return top5_predictions

# user's preferences
preferences = list("Beginner" for i in range(17))

print(get_recommendation(preferences))