# run_in_hpc
Examples and tutorials for running your Python based code in High Power Computing (HPC) clusters

# Workflow for running a Python script
![](https://img.shields.io/badge/Python-3.10.8-181717?style=for-the-badge&logo=python) 
![](https://img.shields.io/badge/Conda-4.12.0-red?style=for-the-badge&logo=anaconda) 

## Logging into DelftBlue
Enter the following command in terminal (Mac OS) or in the command prompt (Windows).
```bash
ssh <netid>@login.delftblue.tudelft.nl
```
Press Enter, you will be asked to enter your NetID password:
```bash
<netid>@login.delftblue.tudelft.nl's password:
```
Please note, that you will not see any characters appearing on the screen as you type your password. This is normal, and is designed to increase security, so that people watching over your shoulder don't even know how many characters your password contains. Once you typed in your password, press Enter again. You should see the following:
```console
    ____       ________  ____  __
   / __ \___  / / __/ /_/ __ )/ /_  _____
  / / / / _ \/ / /_/ __/ __  / / / / / _ \
 / /_/ /  __/ / __/ /_/ /_/ / / /_/ /  __/
/_____/\___/_/_/  \__/_____/_/\__,_/\___/

As DelftBlue is a new system and was newly installed and configured, some things might not be fully working yet, and are still in the process of being set up.

For information about using DelftBlue, see the documentation: https://www.tudelft.nl/dhpc/documentation (login using your TU Delft account)
When you have questions, you can ask them in the DHPC chat service: https://mattermost.tudelft.nl/dhpc/ (login using your TU Delft account)

Last login: Thu Jul 21 16:56:39 2022 from 145.90.36.181


Quota information for storage pool scratch (ID: 1):

      user/group     ||           size          ||    chunk files
     name     |  id  ||    used    |    hard    ||  used   |  hard
--------------|------||------------|------------||---------|---------
      <netid>|588559||   20.63 GiB|    5.00 TiB||   278772|  1000000

Quota information for storage pool home (ID: 2):

      user/group     ||           size          ||    chunk files
     name     |  id  ||    used    |    hard    ||  used   |  hard
--------------|------||------------|------------||---------|---------
      <netid>|588559||    3.44 GiB|    8.00 GiB||    48433|  1000000

 11:54:16 up 48 days, 19:22,  6 users,  load average: 0.09, 0.20, 0.15

 [<netid>@login04 ~]$
```
If you want to avoid entering password everytime you log in into DelftBlue, you can set up **SSH-key** generation by following this [website](https://kb.n0c.com/en/knowledge-base/how-to-create-an-ssh-key-and-connect-to-an-account/), and choose the correct operating system.
> **Note** This step is important and needs to be done only in ur private system, so that you can always connect to your remote server without authentication

## Setting up Python
### Create directories for libraries
In windows the general file structure is as follows: 
* C:\Windows
* C:\Users
* C:\Program Files

For Linux, the folder structure is:

* **/** : Root folder
* **~** : Personal home folder
* **.** : Current directory. Important for executing programs
* **..** : One folder up from the current directory

In Linux everything is represented as a *File*

You can create these directories on the scratch storage and link to them in your home directory. For example when using conda:
```python
mkdir -p /scratch/${USER}/.conda
ln -s /scratch/${USER}/.conda $HOME/.conda
```

When using pip:

 ```python
mkdir -p /scratch/${USER}/.local
ln -s /scratch/${USER}/.local $HOME/.local
```
### Clone your git-repository (The best way)
1. Type the folllowing code in \HOME directory to create a new folder
```python
mkdir ${dirname} 
```
2. Follow the instruction at https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token to generate the **personal access code** for your git account. Skip this step if you dont have 2FA turned on.
3. Type the following and then put your username and password
```python
git clone <repository name: full url address>
```
If using 2FA input the personal access code instead of your password.


#### Saving GIT credentials
It will be troublesome to enter your GIT credentials everytime for performing GIT PULL, PUSH , etc. To avoid this you could cache the git credentials by following the steps here: https://github.com/cli/cli

### Installing libraries using CONDA
First generate the required repository names from the local machine using a conda environment using follows:
```python
conda activate <my_env>
conda env export --from-history -f <file_name>.yml
```
Copy the <file_name>.yml to the delftblue and run the next commands.
Type this command to install all the required packages diirectly from a <file_name.yml> file created from a local computer:
```python
conda env create -f <full_path/environment.yml>
```
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
This command will create a sub-directory /opt/gurobixxx/linux64 that contains the complete Gurobi distribution (assuming you chose /opt). Your *installdir* (which we'll refer to throughout this document) will be /opt/gurobixxx/linux64.

**Setting up Path variables**

The Gurobi Optimizer makes use of several executable files. In order to allow these files to be found when needed, you will have to modify a few environment variables:

* GUROBI_HOME should point to your *installdir*.
* PATH should be extended to include *installdir*/bin.
* LD_LIBRARY_PATH should be extended to include *installdir*/lib.

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

**Connecting Gurobi installations to Python**
You need to run a script **setup.py** available with the gurobi installation files. For it follow the commands:
```
cd /home/netid/opt/gurobi952/linux64
python setup.py
```
### Running Python script on a remote server in background (without SLURM, e.g. delftblue)
You can use the nohup command to run the Python script in the background and disassociate it from the terminal session. This will allow the script to continue running even after you log out of the remote host.

Here are the steps to follow:

1. While you're still connected to the remote host via ssh, run the Python script using the nohup command like this:


    ```shell
    nohup python script.py &
    ```
The & at the end of the command runs the script in the background.

2. Press Enter to execute the command. The script will start running in the background.

3. Type exit to log out of the remote host. This will close the ssh connection, but the Python script will continue running in the background.

You can now disconnect from the remote host without interrupting the Python script. If you want to check on the status of the script later, you can log back in to the remote host and use the ps command to see a list of running processes. Look for the process ID (PID) of the Python script and use the kill command to stop it if needed.

4. To redirect the output of a Python script to a text file, you can use the command-line shell redirection operator > to send the output to a file.

```shell
nohup python script.py > output.txt 2>error.txt &
```
This command runs the script.py Python script and redirects its output to the output.txt file. The > operator creates a new file if it doesn't exist, or overwrites the file if it already exists. If you want to append the output to an existing file instead of overwriting it, you can use the >> operator. To redirect error output (stderr) to a file, you can use the 2> operator in the command-line shell.

> **Note** Note that the output that is redirected to the file depends on how the Python script is written. If the script prints output to the console using the print() function, that output will be redirected to the file. If the script writes output to a file using Python's file I/O functions, then the output will be written directly to the file without being redirected.

> **Note** Note that when you redirect error output, the script may continue running even if errors occur, and you may not see the error messages on the console. Therefore, it's important to check the error file for any error messages that were generated during the script's execution.


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
  
Create a test.py script in your HOME directory using:
```
vim test.py
```
Now type the code available in [opt_test.py](opt_test.py)
Save and quit Vim editor by typing- ":wq", hit enter. Run the file using:
```
module load miniconda3
conda activate "new_env"
python test.py
```

Remember to replace "new_env" by the actual name of the evironment. If the installations and license is correct you will get the following output in your Delftblue terminal:
```
>> Optimisation problem solved sucessfully

>> *** Solution *** :
>> x: 100.0
>> y: -29.0
```
> **Note** The code will take around 5 mins to run, so be patient
If it does not show any output or shows some error, you need to check if all the previous steps are correctly followed. For any questions feel free to contact [me](https://github.com/nkpanda97)


# Working with MPI (mpi4py)

What is MPI?
------------

*Message Passing Interface*, is a standardized and portable message-passing system designed to function on a wide variety of parallel computers. The standard defines the syntax and semantics of library routines and allows users to write portable programs in the main scientific programming languages (Fortran, C, or C++).
Since its release, the MPI specification [mpi-std1]_ [mpi-std2]_ has become the leading standard for message-passing libraries for parallel computers.  Implementations are available from vendors of high-performance computers and from well known open source projects like MPICH_ [mpi-mpich]_ and `Open MPI`_ [mpi-openmpi]_.

For official information on mpi4py, go [here](https://mpi4py.readthedocs.io/)


mpi4py on HPC Clusters 
-----------------------
The following is tested for [**Surf Snellius HPC cluster**](https://www.surf.nl/en/services/snellius-the-national-supercomputer)

NOTE: Do not use conda install mpi4py. This will install its version of MPI instead of using one of the optimized versions that exist on the cluster. The version with conda will work, but it will be very slow.

The proper way to install mpi4py is to use pip together with one of the MPI libraries that already exist on the cluster. What follows are step-by-step instructions on how to set up mpi4py on the Tiger cluster. 

1. Connect to HPC (Snellius or DelftBlue)
```
ssh <YourUserID>@snellius.surf.nl
```
where <YourUserID> is your login ID. You might need to be connected to your university VPN.

2. Create and Activate a Conda Environment

Load an Anaconda module and create a Python environment (see note below if using Python 3.9+):
```
module load 2023
module load module load Anaconda3/2023.07-2
onda create --name fast-mpi4py python=3.8 -y
source activate fast-mpi4py
```
You should list all your Conda packages on the "conda create" line above so that the dependencies can be worked out correctly from the start. Later in the procedure, we will use pip. One should carry out all the needed Conda installs before using pip.

3. Install mpi4py in the Conda Environment

Load the MPI version you want to use. We recommend using Open MPI in this case. In order to get a list of all the available Open MPI versions on the cluster, run "module avail openmpi".
The result will look something like:
```console
----------------------------- /sw/arch/RHEL8/EB_production/2023/modulefiles/cae ------------------------------
   Lumerical/2022-R1.1-OpenMPI-4.1.5    Lumerical/2023-R2.3-OpenMPI-4.1.5

----------------------------- /sw/arch/RHEL8/EB_production/2023/modulefiles/mpi ------------------------------
   OpenMPI/4.1.5-GCC-12.3.0

If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```
As we see there is only one version of openmpi i.e. 12.3.0, we will load that
```
module load OpenMPI/4.1.5-GCC-12.3.0
```
Set the loaded version of MPI to be used with mpi4py:

```
export MPICC=$(which mpicc)
```
> **Note** You can check that this variable was set correctly by running echo $MPICC and making sure that it prints something like: /usr/local/openmpi/<x.y.z>/gcc/x86_64/bin/mpicc.

Finally, we install mpi4py using pip:
```
pip install mpi4py --no-cache-dir
```
> **Note** If you receive a "Requirement already satisfied" message, you may have mistakenly pre-loaded the mpi4py environment module or already installed the package. Make sure you are not loading this environment module in your .bashrc file.

When the installation is finished, check that it was properly installed by running
$ python -c "import mpi4py"
If the above command gives no error, mpi4py was successfully installed.

> **NOTE** These instructions work when Python 3.8 is used in the conda environment. If you need Python 3.9 or above, then you will probably encounter this error: **"Could not build wheels for mpi4py"**. The solution is explained below:

The issue is related to Python provided by Conda. The flag "-B /home/pavan/miniconda3/envs/codelab/compiler_compat" will ask the compiler to pick up ld from that path. but the ld provided by conda will cause some issues when you are using different compiler toolchains.

Steps to fix it:
```
cd /home/<UserId>/.conda/envs/fast-mpi4py/compiler_compat
rm -f ld
ln -s /usr/bin/ld ld
```
and try to build mpi4py again.

after that, revoke that change:

```
cd /home/<UserId>/.conda/envs/fast-mpi4py/compiler_compat
rm -f ld
ln -s ../bin/x86_64-conda-linux-gnu-ld ld
```

