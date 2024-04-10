steps:

- uses: actions/checkout@v2

- name: Set up JDK 
  uses: actions/setup-java@v2
  with: 
    java-version: '11'

- name: Run pipeline
  env:
    NXF_VER: 23.10.3 
  run: |
    nextflow run main.nf -resume