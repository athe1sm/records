import json
import pandas as pd
from fastapi import FastAPI

# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts
DATA = pd.read_csv(
    "https://eaton-lab.org/data/iris-data-dirty.csv",
    names=["trait1", "trait2", "trait3", "trait4", "species"],
)

# create a root endpoint that say's hello
@app.get("/")
def root(name="person"):
    "returns a hello world message in JSON"
    return {"message": f"Hello World to you, {name}"}

# create another endpoint for returning iris data
@app.get("/iris")
def iris(species=None):
    """
    returns iris data in JSON with option to subselect a species
    """
    # get subset or full data
    if species is not None:
        data = DATA.loc[DATA.species == species, :]
    else:
        data = DATA

    # convert to JSON and return to endpoint
    sdata = data.to_json(orient="index")
    jdata = json.loads(sdata)
    return jdata