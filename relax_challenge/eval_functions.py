# Evaluation Funcitons

from sklearn.metrics import classification_report, roc_curve, auc, confusion_matrix, accuracy_score, recall_score
import matplotlib.pyplot as plt
        

def roccurve(trainedevaluator,plotting=False,X,y,Xtest,ytest):
    """ Plots ROC Curve and return area under the curve """

    #fit
    trainedevaluator.fit(X,y)
    
    #Find probabilities
    preds = trainedevaluator.predict_proba(Xtest)[:,1]
    
    #ROC
    fpr, tpr, _ = roc_curve(ytest, preds)
    
    #Area Under the curve
    area = auc(fpr,tpr)
    
    #Plot
    if plotting == True:
        plt.figure(figsize=(6,6))
#            plt.xlim([0,1])
#            plt.ylim([0,1])
        plt.title("ROC",fontsize=12)
        plt.xlabel("False Positive Rate")
        plt.ylabel("Ttrue Positive Rate")
        plt.plot(fpr,tpr)
        plt.plot([0,1],[0,1],'--',alpha=0.5)
    
    return area



def prediction(clf,X=X,y=y,Xtest=Xtest,ytest=ytest):
    
    """ Prints out an evaluation report """
    
    preds = clf.predict(Xtest)
    cm = confusion_matrix(ytest, preds)
    
    print ("\nClassification Report on the Training data -\n", classification_report(y, clf.predict(X)))
    
    print("\n-------------------------------------------------------------------")
    print("Evaluation of test run\n")
    
    print("Accuracy Score =", accuracy_score(ytest, preds))
    print("Recall Score = ", recall_score(ytest,preds))
    
    print("\nConfusion Matrix -\n",cm)
    print("\nClassification Report -\n",classification_report(ytest, preds))
    try:
        print("Area under the ROC curve = {}".format(roccurve(clf)))
    except AttributeError:
        print ("Cannot draw ROC - predict_proba is not an attribute")