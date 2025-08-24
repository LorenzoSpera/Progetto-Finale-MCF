# Final Project – MCF

## Index
1. [Content](#content)
2. [Running the Simulation](#running-the-simulation)
3. [Analysis of Results](#analysis-of-results)
4. [Package Installation](#package-installation)

### Content

Repository containing the final project of the course *Computational Methods for Physics (2023–2024)*, consisting of the simulation of an electromagnetic shower based on the Rossi model.  
Inside the repository there are two Python scripts: _sciame_def.py_ and _run_sciame.py_.  
The first contains the definition of the various classes used to build the simulation; that is, the particle classes and a shower class in which the simulation is carried out according to the required model.  

### Running the Simulation  

The result of the simulation and the presentation of the results are in the second file.  
The first script is imported into the second through the _sys_ library.  
Once both files are downloaded, the first is imported into the second with the command:  
python
import sys
sys.path.append("path/to/sciame_def.py")
```

To run the simulation, you can proceed as follows:

Choose the simulation parameters: type of the initial particle, particle energy, critical energy of the materials, ionization energy loss, step size, and radiation length of the material.
In the initial part of the script there are already two simulations: one for the two materials (water and bismuth silicate) with values taken from the Particle Data Group, and another with different values for comparison.
The user is free to change these parameters.
Once the simulation is executed, the ionization energy lost after the entire process is printed and the requested quantities are reported in a table.
These quantities are also studied graphically, with additional plots to fully analyze the physical phenomenon. The content of each plot is specified, and the user is asked whether they want to view it by entering the indicated command.

### Analysis of the results 


In the final part, there is a comparison between simulations with different energies for the materials.
To speed up visualization, it is recommended to enter 0 whenever the program asks whether to display results, except when it explicitly refers to the comparison between simulations.

The repository also contains a .pdf file that was useful for building the simulation (to keep track of the various points) and especially for comparing results. The file outlines the structure of the simulation and describes the results obtained for different runs, focusing on the sensitivity of the simulation to quantities and parameters that can be varied.
Since the code has been updated, a section was added to the .pdf file to compare with the new results, while two sections related to the outdated version of the simulation (which contained some inconsistencies) were removed.


### Package Installation

For displaying the requested quantities, the Python library rich was used.
If this library is not already installed, move to the working directory and install it from the terminal with the following command:

```
pip install rich
```
Per l'installazione si richiede una versione di Python pari o superiore alla 3.7.
