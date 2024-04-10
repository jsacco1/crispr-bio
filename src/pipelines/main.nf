process generate_data {

  script:
  """
  python ../scripts/generate_test_data.py
  """

}