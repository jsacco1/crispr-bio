steps:

- uses: actions/checkout@v2

- name: Set up JDK
  uses: actions/setup-java@v2
  with:
    java-version: '11'

- name: Install Nextflow
  run: |
    wget -qO- get.nextflow.io | bash
    sudo mv nextflow /usr/local/bin/

- name: Print Path 
  run: echo $PATH

- name: Run pipeline
  run: |  
    /usr/local/bin/nextflow run main.nf -resume

- name: Run pipeline
  env:
    NXF_VER: 23.10.3
  run: |
    nextflow run main.nf -resume

process generate_data {

  script:
  """
  python /src/scripts/generate_test_data.py
  """

}

workflow {

  main:
    generate_data()

}