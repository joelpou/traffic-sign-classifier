# **Traffic Sign Recognition**

## Writeup

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

I'm submitting this assignment incomplete because I need help. I know I'm behind schedule submitting this, but I'm willing to work extra hard in order to understand my mistakes and do a better job on next assignments. The problem I'm having is with training and calculating the accuracy. I've read some of the posts regarding this issue but no matter what hyperparameter values I change (EPOCHS, learning rate, etc), I keep getting the same values on accuracy. Its as if my model is not learning anything, like if its stuck at a local minima. I'm really getting frustrated by this and I wish to understand why is this happening. Any help is truly appreciated. The following is the results I'm getting in the last section of Step 2:

Training...

EPOCH 1 ...
Test Accuracy = 0.036
Validation Accuracy = 0.034

EPOCH 2 ...
Test Accuracy = 0.047
Validation Accuracy = 0.048

EPOCH 3 ...
Test Accuracy = 0.057
Validation Accuracy = 0.054

EPOCH 4 ...
Test Accuracy = 0.047
Validation Accuracy = 0.048

EPOCH 5 ...
Test Accuracy = 0.058
Validation Accuracy = 0.054

EPOCH 6 ...
Test Accuracy = 0.057
Validation Accuracy = 0.054

EPOCH 7 ...
Test Accuracy = 0.038
Validation Accuracy = 0.034

EPOCH 8 ...
Test Accuracy = 0.051
Validation Accuracy = 0.048

EPOCH 9 ...
Test Accuracy = 0.037
Validation Accuracy = 0.034

EPOCH 10 ...
Test Accuracy = 0.047
Validation Accuracy = 0.048

EPOCH 11 ...
Test Accuracy = 0.058
Validation Accuracy = 0.054

EPOCH 12 ...
Test Accuracy = 0.036
Validation Accuracy = 0.034

EPOCH 13 ...
Test Accuracy = 0.058
Validation Accuracy = 0.054

EPOCH 14 ...
Test Accuracy = 0.047
Validation Accuracy = 0.048

EPOCH 15 ...
Test Accuracy = 0.010
Validation Accuracy = 0.014

EPOCH 16 ...
Test Accuracy = 0.051
Validation Accuracy = 0.048

EPOCH 17 ...
Test Accuracy = 0.629
Validation Accuracy = 0.646

EPOCH 18 ...
Test Accuracy = 0.036
Validation Accuracy = 0.034
