# Spine apparatus modulates Ca2+ in spines through spatial localization
of sources and sinks

The simulations used to generate the results in this paper were created with MCell4. This software is available as a Python library and includes a user-friendly interface as an add-on for Blender. Running our simulations and reproducing our results require prior knowledge of MCell4. We encourage readers to explore the official MCell4 tutorials, available at https://mcell.org and https://mcell.org/tutorials/index.html.

## Installation

Please follow the installatioin guidelines for MCell4 described in https://mcell.org

## Usage
In order to run the simulations and reproduce the results decide whether you want to run simulations contianing both IP3RS and RyRs or only RyRs. Choose the corresponding folder. Within each folder you will fin the code for the different geometries used in our manuscript. For each geometry simulations were ran assuming different RyR (and IP3R) distributions (head, homog, and neck). You can either run for the corresponding experiment the simulation on the blender user interface, or in python. The files needed to run on the Blender user interface are the ones ending with the extension '.blend'. On the other hand for running the files directly on python, please look for the files called 'model.py'. For example for running the idealized geometry with idealized SA assuming the RyRs to be distributed in the head in python, the user would need to navigate to the folder 'RyR/Ideal_geom/RyR_head_files/mcell/output_data/' and run the python code model.py. In the terminal introduce the following command:
'python3.9 model.py'

In case the user wants to run multiple seeds this can be done in the following way:
'for i in {1..5}; do python3.9 model.py -seed $i &  done '


## Data
The data used for generating the figures in this manuscript is saved under the folder Data

## License

[MIT](https://choosealicense.com/licenses/mit/)