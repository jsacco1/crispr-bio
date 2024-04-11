# cas12
Project overview and instructions.

## Usage

Run this command in `cas12/src/pipelines/`:

nextflow run main.nf

### To add a process

Edit the main.nf file and add a process to the workflow:

    ```
    workflow {

    myWorkflow {
        firstProcess()
        secondProcess(firstProcess.out)
    }
    
    }
    ```

### Github Actions

Use GitHub Actions for:

Checking out code
Setting up environments
Running the Nextflow pipeline
Deploying results

The key points of main.yml: 

nextflow will refers to the version installed in the workflow
Specify the full path to your main.nf script
No need to specify path to the Nextflow executable
Can set the NXF_VER env variable to pin version