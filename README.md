# Master of Engineering project at Cornell.
## Title: Automatic Assessment Generation via Machine Learning using StackOverflow Dataset.

### Abstract
This project is part of Machine Learning and Education Research aimed to build an automatic system for generation of test/assessment. The project uses data dumps from 130+ stack-exchange websites, with ∼5 million users ∼30 million posts, to learn interesting hidden variables like difficulty of question, quality of answers, ability of users in a particular specialization. The goal is to use these learned parameters to build applications like generating an assessment, tracking the learning curve of a student, ranking all the users. Data on these 130+ stack-exchange websites is huge, therefore a careful review is done to understand how data is arranged, what different attributes mean. It is then processed to extract out the important attributes. Various approaches like Linear system of equations, Naive Bayes, Probabilistic Graphical models have been explored to learn the hidden variables. It is found that Graphical models give best results on both simulation and real world data. We are able to achieve ∼ 20% better than the baselines.

This project is part of Machine Learning and Education Research aimed to build an automatic system for generation of test/assessment. The project uses data dumps from 130+ stack-exchange websites to learn interesting hidden variables  like difficulty of question, quality of answers, ability of users in a particular specialization. The goal is to use these learned parameters to build applications like generating an assessment, tracking the learning curve of a student, ranking all the users. Data on these 130+ stack-exchange websites is huge, therefore a careful review is required to understand how data is arranged, what different attributes mean, so that it can be processed to extract out the information of interest. Various approaches like Linear system of equations, Naive Bayes, Graphical models have been explored and it is found that Graphical models give best results.

### Poster
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/AJPoster.png "Poster")

### Dataset
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/stackexchange.png "Dataset")

### Model Structure
Scripts are in ver2 folder. Call "python ver2/main.py -h" for more help.
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/dotGraph/fileTreedetail.png "ModelStructure")

### Project Notes
[Click Here!!](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/ProjectNotes.pdf)

### Description of Other scripts present in ver2 folder

1. [**check_grad.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/check_grad.py)       ==>        script to check the gradient
2. [**preprocess.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/preprocess.py)       ==>        Important script: preprocess the data and structure it into following form for each question-
  * voteHist = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [5, [0, 1, 2, 3, 4, 5]]]
3. [**simulation.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/simulation.py)       ==>        Main script to solve for theta parameters(contains all the optimization functions)
4. [**runTestSim.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/runTestSim.py)       ==>        Just a test script to run a test case from simulation and visualize
5. [**visualize.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/visualize.py)        ==>        Contains implementation of all visualization functions
6. [**runModelSim.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/runModelSim.py)      ==>        A test script which takes a particular voteHist and solve it with runModel in simulation script and visualizes data and output
