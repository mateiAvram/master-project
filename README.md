# master-project

This repository contains the Master’s thesis and is meant to ask as a replication package. It includes:

* An **E-ticket platform** developed with **HTML, CSS, JavaScript, and Bootstrap**, backed by **Python and SQL** for the server and database.
* A **Jupyter Notebook** with the analysis of data collected from the platform experiments.

The goal of this project is to provide a reproducible environment for others to test the hypotheses and findings presented in the thesis.

---

## Repository Structure

```
master-project/
│── e-ticekt-platform/          # Source code of the E-ticket platform
│── analysis/                   # Jupyter notebook and data extracted from the experiment
│── experiment/                 # Raw experiment data
│── docs/                       # Thesis and presentation
```

---

## Running the Platform

The instructions to set up and run the E-ticket platform are as follows:
1. Create and activate a python virtual environment
```bash
# windows
python -m venv venv
venv\Scripts\activate

# linux or mac-os
python3 -m venv venv
source venv/bin/activate
```
2. Install required packages
```bash
pip install flask flask_cors
```
3. Navigate to the `e-ticket-platform/server/` directory
4. Run the server
```bash
# windows
python -m api.api

# linux or mac-os
python3 -m api.api
```
5. To access the platform navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Running the Analysis

The analysis is provided in a Jupyter Notebook inside the `analysis/` directory

To run it:

1. Install **Python** and **Jupyter Notebook**
2. Set-up a python virtual environment
3. Install the required dependencies
4. Open and run the notebook `results.ipynb`

---

## Running SonarQube

SonarQube can be run both locally and on cloud.

To run it, modify the **sonar-project.properties** file in any individual student implementation located in `experiment/implementaions/e-ticket-` directory

## Documentation

The full thesis and the presentation, can be found in the `docs/` folder.
