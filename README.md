# The Game of Life #

https://github.com/user-attachments/assets/aae33998-ae24-47ef-aaf1-74fdddd2e440

## Project Description ##
I made this little project as a way to practice simulation tools with Python, specifically with mesa. I found the outline for this example from the mesa documentation site which I'll list below as a reference. 

## Project Details ##
As you'll see, there are three files in this repo:
1. agents.py: this file defines the behavior of an agent, or in the case of this example, an individual cell, which can be defined in one of two states: DEAD or ALIVE.
2. app.py: using Solara, this file defines an interactive visualization so that users can play the role of some high-ordered entity, possibly even what some would consider 'God', in The Game of Life. 
3. model.py: this file defines the model itself, and it is initialized with a random configuration of the two possible states of the agents. That is, it initalizes random configiruations for DEAD and ALIVE cells.


## How to Use ##
NOTE: You will need to use a newer version of Python (3.13.X) to run this model.

I've tried to make this as simple as possible for those with little to no coding experience:
1. Clone all three files in this projet.
2. Make sure all your packages are installed. Note that I had to manually 
```` $ pip install mesa ````
```` $ pip install solara ````
```` $ pip install matplotlib ````
```` $ pip install altair ````
```` $ pip install networkx ````
3. Initiate your app with the following command:
```` $ solara run app.py ````
ENJOY! =D

## The Nerd Corner ##
The Game of Life is a classic computation method used to understand how discrete systems evolve over time. In nerd terms, it's a cellular automaton (CA) model that uses a 2D grid structure which is comprised of individual cells. These cells are assigned discrete states before the model initiates. These states are binary, where cells are identified as having an identity in one state or another. CA models don't deal with coupled states, they're very basic in this way. You can think of each cell being 'on' or 'off' or, in The Game of Life, each cell is defined as being DEAD or ALIVE. This is defined in the first file listed above: agents.py

What happens next? Well, the model itself has rules by which the agents, or cells, need to abide by in order to understand how the interact, and influence, one another. In CA models, we care about what's happening in the relationship between the nearest neighbors of each cell. That is, for any given cell in the grid, we care about how the state of any given cell effects the state of any of it's nearest neighbors, which also have assigned states. The evolution of this relationships are studied over time, where each timestampe (from time t=0 to t=1) indicates a new generation. Each generation is a pure function of the preceding generation, meaning that no outside influence can change the altered states of the next generation. It's a closed system. 

For The Game of Life, in order to have some sort of structured study for these relationships, a couple rules are defined for how neighbors interact with each other:

1. Any ALIVE cell with fewer than two ALIVE neighbors dies. This simulates underpopulation.
2. Any ALIVE cell with two or three ALIVE neighbors lives on to the next generation/iteration of the simulation.
3. Any ALIVE cell with more than three ALIVE neighbors dies. This simulates overpopulation.
4. Any DEAD cell with exactly three ALIVE neighbors becomes ALIVE. This simulates reproduction.

These rules can be found in one of the files I mentioned above: model.py

The Game of Life continues on until the model runs through all the generations defined or until you intervene and stop the model early. Either way, the result of this beautifully simple model is to understand how the changing state of agents, or cells, influences the future states of neighboring agents. Properties emerge from this study, patterns unfolded, and maybe, just maybe, a little bit of insight is gained. Or maybe I'm just reading into it deeper than this little README entails. Either way, thanks for coming to my TedTalk. Refererences for more learning can be found below.

## Refererences ##
Please visit the [docs](https://mesa.readthedocs.io/stable/examples/basic/conways_game_of_life.html) to access this example for yourself to you too, can create The Game of Life.

Also, if you're a nerd like me and want to learn more about Life, please visit [this](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) wikipedia article.

You can also learn more about cellular automaton, which is the entire premise behind Life, [here](https://en.wikipedia.org/wiki/Cellular_automaton).

