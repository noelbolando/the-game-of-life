"""
Defines an interactive visualization using solara.
To initialize the app: 
    solara run app.py 
"""

from model import ConwaysGameOfLife
from mesa.visualization import SolaraViz, make_space_component
import solara

"""Function that defines how the agents appear in the solara app."""
def agent_portrayal(agent):
    return {
        # Black = DEAD cells, white = ALIVE cells
        "color": "white" if agent.state == 0 else "black",
        "marker": "s",
        "size": 20,
    }

"""Function that proceses the game of life."""
def post_process(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])


model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 40,
        "label": "Width",
        "min": 5,
        "max": 40,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 40,
        "label": "Height",
        "min": 5,
        "max": 40,
        "step": 1,
    },
    "initial_fraction_alive": {
        "type": "SliderFloat",
        "value": 0.2,
        "label": "Cells initially alive",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
}

# Create initial model instance
model1 = ConwaysGameOfLife()

# Create visualization elements. The visualization elements are solara components
# that receive the model instance as a "prop" and display it in a certain way.
# Under the hood these are just classes that receive the model instance.
# You can also author your own visualization elements, which can also be functions
# that receive the model instance and return a valid solara component.
SpaceGraph = make_space_component(
    agent_portrayal, post_process=post_process, draw_grid=False
)


# Create the SolaraViz page. This will automatically create a server and display the
# visualization elements in a web browser.
# Display it using the following command in the example directory:
# solara run app.py
# It will automatically update and display any changes made to this file
page = SolaraViz(
    model1,
    components=[SpaceGraph],
    model_params=model_params,
    name="Game of Life"
)
page  # noqa
