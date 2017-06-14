import tensorflow as tf
import tensorflow.contrib
import numpy as np
IRIS_TRAINING = "TrainingData1.csv"
IRIS_TEST = "TestingData1.csv"
#returns False if the index is outside the array bounds or if the array value at that index isn’t searchterm
def arraysearch(a, searchterm, sindex):
    if sindex>=len(a):
        return False
    elif a[sindex]==searchterm:
        return True
    else:
        return False
#returns the lexicographically next term in the sequence of possible nodes and layers
def testincrements(a, start, end, increment):
    c=0
    while arraysearch(a, end, c) and c<len(a):
        a[c]=start
        c+=1
    if c==len(a):
        a.append(start)
        return a
    else:
        a[c]=a[c]+increment
        return a

# Load datasets.
training_set = tf.contrib.learn.datasets.base.load_csv_without_header(filename=IRIS_TRAINING, features_dtype=np.float64, target_dtype=np.float64)
test_set = tf.contrib.learn.datasets.base.load_csv_without_header(filename=IRIS_TEST, features_dtype=np.float64, target_dtype=np.float64)

x_train, x_test, y_train, y_test = training_set.data, test_set.data, \
  training_set.target, test_set.target
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=31)]
pos=0
#get and print the number of positive examples(parse check)
print(y_train)
print(y_test)
for a in y_train:
    if a==1:
        pos=pos+1
print(pos)
pos=0
for a in y_test:
    if a==1:
        pos=pos+1
print(pos)
#number of times over which to average the network
ba=20
# initializing relevant variables(ba=number of loops per avg f1, all else self explanatory)
avgauc = 0
avgf1 = 0
avgprecision=0
avgrecall=0
ba = 20
optimizerarraystart = [20, 20, 20]
optimizerarraycurrent = [20, 20, 20];
maxoptimizerarray = optimizerarraystart;
maxavgf1 = 0


def model_fn(features, targets, mode, params):

  """Model function for Estimator."""

  # Connect the first hidden layer to input layer
  # (features) with relu activation
  first_hidden_layer = tf.contrib.layers.relu(features, 20)


  # Connect the second hidden layer to first hidden layer with relu
  second_hidden_layer = tf.contrib.layers.relu(first_hidden_layer, 20)

  third_hidden_layer = tf.contrib.layers.relu(second_hidden_layer, 20)

  # Connect the output layer to second hidden layer (no activation fn)
  output_layer = tf.contrib.layers.linear(second_hidden_layer, 2)

  # Reshape output layer to 1-dim Tensor to return predictions

  labels = tf.one_hot(indices=tf.cast(targets, tf.int32), depth=2)
  predictions = output_layer

  # Calculate loss using mean squared error
  #weight = tf.multiply(5.0, tf.cast(tf.equal(labels, [1, 0]), tf.float32))
  #weight=0.5

  loss = tf.losses.sigmoid_cross_entropy(labels, predictions)
  ''', weights=tf.constant([[1], [5]]))'''
  weight=1.0

  # Calculate root mean squared error as additional eval metric
  eval_metric_ops = {
      "rmse":
          tf.metrics.root_mean_squared_error(
              tf.cast(labels, tf.float64), predictions),
      "recall":
        tf.metrics.recall(labels, predictions, weights=weight),
      "precision":
        tf.metrics.precision(labels, predictions, weights=weight),
      "auc":
        tf.metrics.auc(labels, predictions, weights=weight),
      "tp":
          tf.metrics.true_positives(labels, predictions, weights=weight),
      "fn":
          tf.metrics.false_negatives(labels, predictions, weights=weight),
      "fp":
          tf.metrics.false_positives(labels, predictions, weights=weight)

  }

  train_op = tf.contrib.layers.optimize_loss(
      loss=loss,
      global_step=tf.contrib.framework.get_global_step(),
      learning_rate=.005,
      optimizer="SGD")

  from tensorflow.contrib.learn import ModelFnOps
  return ModelFnOps(
      mode=mode,
      predictions=predictions,
      loss=loss,
      train_op=train_op,
      eval_metric_ops=eval_metric_ops)
# Build multilayer DNN with current array of layers and nodes, set <x to 6 on server.


while len(optimizerarraycurrent)==3:
    for i in range(ba):
        # create model
        #weight = tf.multiply(15.0, tf.cast(tf.equal(y_train, 1), tf.float32) + 1)

        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, hidden_units=optimizerarraycurrent, n_classes=2)
        #nn = tf.contrib.learn.Estimator(model_fn=model_fn)
        print("Hi")
        # Fit model.
        classifier.fit(x=x_train, y=y_train, steps=1000)
        y=classifier.predict_classes(x_test)
        y=list(y)
        tn=0
        tp=0
        fn=0
        fp=0
        for c in range(len(y)):
            #print(y_test[c])
            if y[c]==0 and y_test[c]==0.0:
               tn+=1
            if y[c]==1 and y_test[c]==0.0:
                fp+=1
            if y[c]==1 and y_test[c]==1.0:
                tp+=1
            if y[c]==0 and y_test[c]==1.0:
                fn+=1
        trueprecision=tp/(tp+fp)
        avgprecision+=trueprecision
        truerecall=tp/(tp+fn)
        avgrecall+=truerecall
        truef1=trueprecision*truerecall
        avgf1+=truef1
        print("True precision: %s" % trueprecision)
        print("True recall: %s" % truerecall)
        print("True f1: %s" % truef1)
        print("true fp: %s" % fp)
        print("true tp: %s" % tp)
        print("true fn: %s" % fn)
        print("true tn: %s" % tn)

        '''nn.fit(x=x_train, y=y_train, steps=1000)
        ev = nn.evaluate(x=x_test, y=y_test, steps=1)
        print("Loss: %s" % ev["loss"])
        print("Precision: %s" % ev["precision"])
        p=ev["precision"]
        avgprecision+=p
        print("Recall: %s" % ev["recall"])
        r=ev["recall"]
        avgrecall+=r
        f1=p*r
        print("F1: %s" % f1)
        avgf1+=f1
        print("Auc: %s" % ev["auc"])
        print("TP: %s" % ev["tp"])
        print("FP: %s" % ev["fp"])
        print("FN: %s" % ev["fn"])'''

    # at this point the program calculates the average f1 and auc for this setup of layers and nodes
    avgf1 = avgf1 / ba
    avgprecision = avgprecision / ba
    avgrecall = avgrecall / ba
    print("Average f1: " + str(avgf1))
    print("Average precision(Fraction of emails marked as nonspam that were nonspam): " + str(avgprecision))
    print("Average recall(fraction of emails that are nonspam marked as nonspam): " + str(avgrecall))
    # here's the maximization code
    if avgf1 > maxavgf1:
        maxoptimizerarray = optimizerarraycurrent
        maxavgf1 = avgf1
    # change these values as needed(20, 50, 15) are suggested for last 3 params
    # here we get the lexicographically next setup of nodes and layers
    optimizerarraycurrent = testincrements(optimizerarraycurrent, 20, 20, 15)
# after the program has tested every setup of nodes and layers given it's starting params, we print out the best setup and its average f1
print(str(maxoptimizerarray))
print(str(maxavgf1))