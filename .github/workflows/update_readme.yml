# update_readme.yml

name: Update README

on:
  schedule:
    - cron: '* * * * *'  # Run every minute

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: pip install requests

    - name: Run script to update README
      run: python update_readme.py
