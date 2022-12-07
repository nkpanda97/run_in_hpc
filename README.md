# run_in_hpc
Examples and tutorials for running your Python based code in High Power Computing (HPC) clusters

# Solving Optimization using Pyomo and GUROBI
![](https://img.shields.io/badge/Python-3.10.8-181717?style=for-the-badge&logo=python) 
![](https://img.shields.io/badge/Conda-4.12.0-red?style=for-the-badge&logo=anaconda) 
![](https://img.shields.io/badge/Pyomo-6.4.3-yellow?style=for-the-badge&logo=)
![](https://img.shields.io/badge/Gurobi-9.5.2-EE3524?style=for-the-badge&logo=Gurobi) 


## Installing Gurobi
Download the gurobi software by logging in from: https://www.gurobi.com/downloads/gurobi-software/ in your **local computer**. Lets say you have it downloaded in the directory: /Users/matrix/Desktop/Downloads. The downloaded file will have a name: *tar xvfz gurobix.x.x_linux64.tar.gz*

> **Note** Guribi version 10.0.0 has a bug for Linux system where it cannot derive the host ids during installations. The following tutorial is tested with gurobi=9.5.2

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
Copy the Gurobi distribution to the destination directory and extract the contents. Extraction is done with the following command:
```
tar xvfz gurobix.x.x_linux64.tar.gz
```
Make sure you replace x.x.x by the actual version name visible in the downloaded file.
This command will create a sub-directory /opt/gurobixxx/linux64 that contains the complete Gurobi distribution (assuming you chose /opt). Your <installdir> (which we'll refer to throughout this document) will be /opt/gurobixxx/linux64. The Gurobi Optimizer makes use of several executable files. In order to allow these files to be found when needed, you will have to modify a few environment variables:

* GUROBI_HOME should point to your <installdir>.
* PATH should be extended to include <installdir>/bin.
* LD_LIBRARY_PATH should be extended to include <installdir>/lib.

Users of the bash shell should add the following lines to their .bashrc files located in their HOME. This can be done in the Delftblue using 
<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Vim</title><path d="M24 11.986h-.027l-4.318-4.318 4.303-4.414V1.461l-.649-.648h-8.198l-.66.605v1.045L12.015.027V0L12 .014 11.986 0v.027l-1.29 1.291-.538-.539H2.035l-.638.692v1.885l.616.616h.72v5.31L.027 11.987H0L.014 12 0 12.014h.027l2.706 2.706v6.467l.907.523h2.322l1.857-1.904 4.166 4.166V24l.015-.014.014.014v-.028l2.51-2.509h.485c.111 0 .211-.07.25-.179l.146-.426c.028-.084.012-.172-.037-.239l1.462-1.462-.612 1.962c-.043.141.036.289.177.332.025.008.052.012.078.012h1.824c.106-.001.201-.064.243-.163l.165-.394c.025-.065.024-.138-.004-.203-.027-.065-.08-.116-.146-.142-.029-.012-.062-.019-.097-.02h-.075l.84-2.644h1.232l-1.016 3.221c-.043.141.036.289.176.332.025.008.052.012.079.012h2.002c.11 0 .207-.066.248-.17l.164-.428c.051-.138-.021-.29-.158-.341-.029-.011-.06-.017-.091-.017h-.145l1.131-3.673c.027-.082.012-.173-.039-.24l-.375-.504-.003-.005c-.051-.064-.127-.102-.209-.102h-1.436c-.071 0-.141.03-.19.081l-.4.439h-.624l-.042-.046 4.445-4.445H24L23.986 12l.014-.014zM9.838 21.139l1.579-4.509h-.501l.297-.304h1.659l-1.563 4.555h.623l-.079.258H9.838zm3.695-7.516l.15.151-.269.922-.225.226h-.969l-.181-.181.311-.871.288-.247h.895zM5.59 20.829H3.877l-.262-.15V3.091H2.379l-.1-.1V1.815l.143-.154h7.371l.213.214v1.108l-.142.173H8.785v8.688l8.807-8.688h-2.086l-.175-.188V1.805l.121-.111h7.49l.132.133v1.07L12.979 13.25h-.373c-.015-.001-.028 0-.042.001l-.02.003c-.045.01-.086.03-.119.06l-.343.295-.004.003c-.033.031-.059.069-.073.111l-.296.83-6.119 6.276zm14.768-3.952l.474-.519h1.334l.309.415-1.265 4.107h.493l-.08.209H19.84l1.124-3.564h-2.015l-1.077 3.391h.424l-.073.174h-1.605l1.107-3.548h-2.096l-1.062 3.339h.436l-.072.209H13.27l1.514-4.46H14.198l.091-.271h1.65l.519.537h.906l.491-.554h1.061l.489.535h.953z"/></svg>

export GUROBI_HOME="/opt/gurobi901/linux64"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"




### Install using gurobi executable
Follow this: https://www.gurobi.com/documentation/9.0/quickstart_linux/software_installation_guid.html

### Install using conda (Recomended)
```bash
module load miniconda3
conda env create "new_env" python=3.10.8
conda activate "new_env"
conda install -c gurobi=9.5.2 gurobi
```
module load miniconda3
conda env create <"new_env"> python=3.10.8
conda activate <new_env>
conda install -c gurobi=9.5.2 gurobi
```
