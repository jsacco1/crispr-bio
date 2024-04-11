#!/usr/bin/env nextflow

/*
 * Define your process
 */

process generate_data {
  script:
  """
  python src/scripts/generate_test_data.py
  """
}

/*
 * Define your workflow
 */

workflow {
  // Specify the process(es) to be executed
  generate_data
}
