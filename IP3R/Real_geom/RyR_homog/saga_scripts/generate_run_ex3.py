import numpy as np 

Geometries = ["RyR_homog_IP3R_dendrite",]
seeds = np.arange(251, 501)
for x in Geometries:
	for i in seeds:
		# Open file for writing
		fileObject = open('/Users/mariahernandezmesa/Documents/Models/Spines/SpineApparatus/MCell4.nosync/Mushroom/Spine_dendrite_geometry/paper_simulations/IP3R/Real_geom/RyR_homog/saga_scripts/{}/run_{}_seed_{}.sh'.format(x,x,str(i).zfill(3)), "w")
		# Add some text
		fileObject.write("#!/bin/bash\n")
		fileObject.write("# Job name:\n")
		fileObject.write('#SBATCH --job-name=Real_geom_homog_{}\n'.format(i))
		fileObject.write("\n")
		fileObject.write("#\n")
		fileObject.write("# Max running time (DD-HH:MM:SS)\n")
		fileObject.write("#SBATCH --time=12-00:00:00 \n")
		fileObject.write("#\n")
		fileObject.write("# Project:\n")
		fileObject.write("#SBATCH --partition=habanaq\n")
		fileObject.write("#SBATCH --output=/home/mariahernandez/D1/Spines/ActiveSA/IP3R/Real_geom/RyR_homog/IP3R_dendrite_files/mcell/output_data/simulations/outputs/%x-%j.txt\n")
		fileObject.write("#SBATCH --nodes=1\n")
		fileObject.write("#SBATCH --ntasks-per-node=1\n")
		fileObject.write("#SBATCH --cpus-per-task=1\n")

		fileObject.write("\n")
		fileObject.write("## Set up job environment:\n")
		fileObject.write("set -o errexit  # Exit the script on any error\n")
		fileObject.write("set -o nounset  # Treat any unset variables as an error\n")
		
		fileObject.write("\n")
		fileObject.write("\n")
		fileObject.write('srun python3.9 /home/mariahernandez/D1/Spines/ActiveSA/IP3R/Real_geom/RyR_homog/IP3R_dendrite_files/mcell/output_data/model.py -seed {} \n'.format(i))

		# Close the file
		fileObject.close()
				