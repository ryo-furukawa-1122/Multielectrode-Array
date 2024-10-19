# Multielectrode-Array
You can plot local field potentials recorded with a 64-ch multielectrode array (MED probe).

# Enviroment
Python 3.12.1

# Directory structure
```
.
└── LFP
    ├── 20240101
    │   ├── slice1
    │   │   ├── 20240101_slice1_ch28.csv
    │   ├── slice2
    ├── 20240102
    ├── 20240103
```

# Preparation
You need to prepare a json file below.
```:config.json
{
    "main_directory": "/Users/.../LFP",
    "date": "20240101",
    "slice": "1",
    "stim_ch": 28,
    "scale": 150
}
```
