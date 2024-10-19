import json
import numpy as np

class Loadings():
    def __init__(self):
        self.directory: str
        self.date: str
        self.slice: str
        self.stim_ch: int
        self.scale: float
        self.path: str

    def read_config(self):
        """Return the path of the csv file, stim. ch, and scale of the signals"""
        f = open("config.json")
        config = json.load(f)

        self.main_directory = config["main_directory"]
        self.date = config["date"]
        self.slice = config["slice"]
        self.stim_ch = config["stim_ch"]
        self.scale = config["scale"]

        return self.main_directory, self.date, self.slice, self.stim_ch, self.scale
    
    def read_csv(self, file:str):
        """Return the data from the csv file"""
        self.file:str = file
        return np.loadtxt(self.file, skiprows=4, delimiter=",", encoding="utf-8")[:, 1:]
    