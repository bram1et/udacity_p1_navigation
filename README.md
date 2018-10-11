# Intro
In this project we will use reinforcement learning to train a single agent to complete a simplified version of the [Banana Collector](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#banana-collector) using a Deep Q Network (DQN). This project will utilize [Unity-ML](https://github.com/Unity-Technologies/ml-agents) to create the environment for learning.

# Environment
The agent is navigating a 3-dimensional square world to collect yellow bananas for a reward of +1 and to avoid blue bananas give -1 reward. The state space of the environment is 37 dimensions and includes the agent’s velocity and ray-based perception of bananas forward of the agent. Using this, the agent must select the best actions to maximize the returned award. The four actions are:
* 0 - forward
* 1 - backward
* 2 - left
* 3 - right
To solve the environment the agent must score 13 over 100 episodes.

# Installation
### Step 1: Clone Repo
Grab this repo using: 

### Step 2: Install dependencies
Mac:
```
conda create --name drlnd_navigation python=3.6
source activate drlnd_navigation
conda install -y python.app
conda install -y pytorch -c pytorch
pip install torchsummary unityagents
```
 
### Step 3: Download Banana Environment
* Mac OSX: [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
Unzip in toplevel directory

# Training your agent
To train an agent open up `Navigation.ipynb`  and run all the cells until  the **Training Agent** header. This will load the environment and display the state space and action space with which the agent will interact. To experiment with different training parameters run one of the cells under in the **Training Agent** header to train an agent that is able to solve the environment and visualize some graphs that show the agent’s learning process. Normally it takes 130 - 250 episodes for the agent to solve the environment.

Lastly to visualize a trained agent interact with the environment run the last cell which will load the weights from a success training run and display the agent for 1 episode.

