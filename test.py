---
# Your workflow content starts here
name: Linter Workflow

on:
  push:
    branches:
      - main

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run linter
        run: |
          print('Hello, world!')
