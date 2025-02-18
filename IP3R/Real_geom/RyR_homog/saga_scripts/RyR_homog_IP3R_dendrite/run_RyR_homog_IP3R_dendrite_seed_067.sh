#!/bin/bash
# Job name:
#SBATCH --job-name=Real_geom_homog_67

#
# Max running time (DD-HH:MM:SS)
#SBATCH --time=12-00:00:00 
#
# Project:
#SBATCH --partition=milanq
#SBATCH --output=/home/mariahernandez/D1/Spines/ActiveSA/IP3R/Real_geom/RyR_homog/IP3R_dendrite_files/mcell/output_data/simulations/outputs/%x-%j.txt
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

## Set up job environment:
set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error


srun python3.9 /home/mariahernandez/D1/Spines/ActiveSA/IP3R/Real_geom/RyR_homog/IP3R_dendrite_files/mcell/output_data/model.py -seed 67 
