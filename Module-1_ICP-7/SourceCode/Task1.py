import nltk
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn import metrics

# load the training and test data
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

# create the tfidf vectors as features
'''
 Details :
 https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
 ngram_range of(1, 1) means only unigrams, (1, 2) means unigrams and bigrams, and (2, 2) means only bigrams
'''
tfidf_Vect = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

# transforming the test date to features
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

# define the Classifier object and train the model
clf =LinearSVC()
'''
 alternative model
# https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
# clf = SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3)
'''
clf.fit(X_train_tfidf, twenty_train.target)

# Evaluation
prediction = clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, prediction)
print(f"Accuracy : {round(score,2)}")