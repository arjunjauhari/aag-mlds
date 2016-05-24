# Master of Engineering project at Cornell.
## Title: Automatic Assessment Generation via Machine Learning using StackOverflow Dataset.

### Abstract
This project is part of Machine Learning and Education Research aimed to build an automatic system for generation of test/assessment. The project uses data dumps from 130+ stack-exchange websites, with ∼5 million users ∼30 million posts, to learn interesting hidden variables like difficulty of question, quality of answers, ability of users in a particular specialization. The goal is to use these learned parameters to build applications like generating an assessment, tracking the learning curve of a student, ranking all the users. Data on these 130+ stack-exchange websites is huge, therefore a careful review is done to understand how data is arranged, what different attributes mean. It is then processed to extract out the important attributes. Various approaches like Linear system of equations, Naive Bayes, Probabilistic Graphical models have been explored to learn the hidden variables. It is found that Graphical models give best results on both simulation and real world data. We are able to achieve ∼ 20% better than the baselines.

### Executive Summary
The goal of this design project was to solve the problem of assessment generation. Currently available method for generating a test requires an excessive amount of human (generally a teacher or domain expert) effort. Our method provides an automated way of generating test with almost no human effort. Moreover, our method can generate new assessments instantly and even personalize them. It can have a mix of both theoretical as well as practical questions. To achieve this goal the main challenge was to learn interesting latent variables like difficulty of question, quality of answers, and ability of users from the observed clicks captured in the StackExchange dataset.

The dataset was huge, which was beneficial for learning task but posed serious processing issues which required critical thinking during the design process of the system. We developed a new algorithm, which is slightly modified version of MapReduce algorithm, to process these data files with million of lines. We successfully processed these files to extract useful attributes and that too in very efficient and fast manner. For instance, we were able to process \verb|Votes.xml| file from StackOverflow.com with ~99 million lines in ~15 minutes and memory usage of ~3 GB. Our modified MapReduce algorithm can trade-off very effectively between time and memory requirements.

The above algorithm compressed the files by throwing away attributes which were not useful to us but still the data was not in format which can be used directly by any learning algorithm. Therefore, next we formatted data into various useful Data Structures. Most of these Data Structures were based on HashMap.

For the learning task, we explored couple of models but spent most of the time on Probabilistic Graphical Model based approach. Graphical models are natural choice for Data Science problems similar to the one we are trying to solve. This design choice proved to be quite successful and we were able to achieve good results. We used a simple graphical model which captures the intuition behind the data generation. The intuition it captures is that every user has some ability (φ) and he generates answers (θ) which are normally (Gaussian) distributed around the user's ability. Now the observed clicks are modelled with intuition that a better answer is more probable of getting an UpVote. We used SoftMax function to capture this intuition.

Even for this simple looking model the implementation was very complex as the number of parameters in the model are equal to number of answers + number of users, which for StackOverflow are in the range of ~10 million even after filtering. This poses both memory and time constraint. Therefore, we first chose dataset like Maths, Physics and Chemistry where the number of parameters were in range of thousands. We used Maximum Likelihood Estimation to learn the most likely parameters given the observed data. To solve this optimization problem we used gradient descent. Specifically, we used L-BFGS for smaller datasets and for larger dataset we used AdaGrad which is an adaptive stochastic gradient descent method.

The planning and implementation of the project went well and smoothly. We were able to train the model and do predictions from the learned model with an accuracy of order ~50% which was 20% better than random guessing. This accuracy is quite good as this problem is a varying multi-class classification problem.

### Detailed Project Report
[Click Here!!](https://github.com/arjunjauhari/meng-project/blob/master/documentation/FinalReport/report/MEngFinalReport-ArjunJauhari.pdf)

### Poster
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/AJPoster.png "Poster")

### Dataset
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/stackexchange.png "Dataset")

### Model Structure
Scripts are in ver2 folder. Call "python ver2/main.py -h" for more help.
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/dotGraph/fileTreedetail.png "ModelStructure")

### Description of Other scripts present in ver2 folder

1. [**check_grad.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/check_grad.py)       ==>        script to check the gradient
2. [**preprocess.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/preprocess.py)       ==>        Important script: preprocess the data and structure it into following form for each question-
  * voteHist = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [5, [0, 1, 2, 3, 4, 5]]]
3. [**simulation.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/simulation.py)       ==>        Main script to solve for theta parameters(contains all the optimization functions)
4. [**runTestSim.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/runTestSim.py)       ==>        Just a test script to run a test case from simulation and visualize
5. [**visualize.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/visualize.py)        ==>        Contains implementation of all visualization functions
6. [**runModelSim.py**](https://github.com/arjunjauhari/meng-project/blob/master/ver2/runModelSim.py)      ==>        A test script which takes a particular voteHist and solve it with runModel in simulation script and visualizes data and output
