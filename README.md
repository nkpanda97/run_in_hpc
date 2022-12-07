# run_in_hpc
Examples and tutorials for running your Python based code in High Power Computing (HPC) clusters

# Solving Optimization using Pyomo and GUROBI
![](https://img.shields.io/badge/Python-3.10.8-181717?style=for-the-badge&logo=python) 
![](https://img.shields.io/badge/Conda-4.12.0-red?style=for-the-badge&logo=anaconda) 
![](https://img.shields.io/badge/Pyomo-6.4.3-yellow?style=for-the-badge&logo=)
![](https://img.shields.io/badge/Gurobi-9.5.2-EE3524?style=for-the-badge&logo=Gurobi) 


## Installing Gurobi (Using executable)
Download the gurobi software by logging in from: https://www.gurobi.com/downloads/gurobi-software/ in your **local computer**. Lets say you have it downloaded in the directory: /Users/matrix/Desktop/Downloads. The downloaded file will have a name: *tar xvfz gurobix.x.x_linux64.tar.gz*

> **Note** Guribi version 10.0.0 has a bug for Linux system where it cannot derive the host ids during installations. The following tutorial is tested with gurobi=9.5.2
#
**Copying the downloaded file to DelftBlue**
> **Note** Your next step is to choose a destination directory. I recommend /opt for a shared installation, but other directories will work as well.
Create a directory named opt in the HOME of Delftblue:
```
mkdir opt
```
Follow the following steps in the terminal/ bash of your local computer:
```
cd  /Users/matrix/Desktop/Downloads
rsync -v gurobix.x.x_linux64.tar.gz netid@login.delftblue.tudelft.nl:/home/netid/opt
```

Copy the Gurobi distribution to the destination directory and extract the contents. Extraction is done with the following command

```
tar xvfz gurobix.x.x_linux64.tar.gz
```

Make sure you replace x.x.x by the actual version name visible in the downloaded file.
This command will create a sub-directory /opt/gurobixxx/linux64 that contains the complete Gurobi distribution (assuming you chose /opt). Your **installdir** (which we'll refer to throughout this document) will be /opt/gurobixxx/linux64. The Gurobi Optimizer makes use of several executable files. In order to allow these files to be found when needed, you will have to modify a few environment variables:

* GUROBI_HOME should point to your <installdir>.
* PATH should be extended to include <installdir>/bin.
* LD_LIBRARY_PATH should be extended to include <installdir>/lib.

Users of the bash shell should add the following lines to their .bashrc files located in their HOME. This can be done in the Delftblue using ![](https://img.shields.io/badge/Vim-blue?style=for-the-badge&logo=Vim) editorby follwing commands:

```
cd
vim .bashrc
```
  
You will enter the Vim editor. Type i and you will go into **insert** mode. Now after the first line type the following:

```
export GUROBI_HOME="/opt/gurobi901/linux64"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"
```
  
Press **esc** key and then exit the editor by typing **:wq:** enter.
 

> **Note** More information abailable at: https://www.gurobi.com/documentation/9.0/quickstart_linux/software_installation_guid.html

  ### Installng Gurobi (Using conda) (Recomended)
```bash
module load miniconda3
conda env create "new_env" python=3.10.8
conda activate "new_env"
conda install -c gurobi=9.5.2 gurobi
```
  
 ## Installing Pyomo
 Install Pyomo using Conda in the Delftblue terminal.
 ```
 conda activate "new_env"
 conda install -c conda-forge pyomo
 ```
  
 ## Installing License
 On the terminal of Delftblue:
  ```
  touch gurobi.lic
  vim gurobi.lic
 ```
  In the gurobi.lic file, type the following:
  ```
  TOKENSERVER=flexserv-x1.tudelft.nl
  PORT=27099
  ```
Now your Gurobi installation setup is ready. Time for testing.
  ## Testing the installations
  
  
