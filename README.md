# Master of Engineering project at Cornell.
## Title: Automatic Assessment Generation via Machine Learning using StackOverflow Dataset.

### Dataset
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/stackexchange.png "Dataset")

### Model Structure
Scripts are in ver2 folder. Call "python ver2/main.py -h" for more help.
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/dotGraph/fileTreedetail.png "ModelStructure")

### Poster
![alt text](https://github.com/arjunjauhari/meng-project/blob/master/documentation/AJPoster/AJPoster.png "Poster")

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
