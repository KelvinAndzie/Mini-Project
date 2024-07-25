import pickle
from sklearn.ensemble import RandomForestClassifier


encode = {
    "not interested": 0,
    "poor": 1,
    "beginner": 2,
    "average": 3,
    "intermediate": 4,
    "excellent": 5,
    "professional": 6,
}


def get_recommendation(preferences: list) -> list:
    # load the model
    with open("resources/saved_models/random_forest_classifier.pkl", "rb") as model:
        randForestClf: RandomForestClassifier = pickle.load(model)

    # Encode the preferences
    for i in range(len(preferences)):
        preferences[i] = encode[preferences[i].lower()]

    # Set feature names to None to avoid the warning
    randForestClf.feature_names_in_ = None

    # Predict probabilities for each class for each instance in the test set
    probabilities = randForestClf.predict_proba([preferences])

    # Get the top 5 predictions for each instance
    top5_predictions = []
    for prob in probabilities:
        top5_indices = prob.argsort()[-5:][
            ::-1
        ]  # Get the indices of the top 5 probabilities
        top5_classes = [
            randForestClf.classes_[i] for i in top5_indices
        ]  # Map indices to class labels
        top5_predictions.append(top5_classes)

    return top5_predictions[0]


# User's preferences
# preferences = ["Beginner" for i in range(17)]

# print(get_recommendation(preferences))
