# Project Title

## Overview
This project aims to analyze a dataset of reviews to identify terms strongly associated with specific categories within the reviews. By leveraging the chi-square statistic and MapReduce paradigm, the project preprocesses the data, calculates term-category associations, and merges top terms associated with each category.

## Features
- Preprocessing of raw review data including tokenization and removal of stopwords.
- Calculation of chi-square statistic for term-category association.
- Merging of top terms associated with each category into a single list.

## Usage
1. **Preprocessing**: Run `preprocess.py` to preprocess the raw data.
2. **Chi-Square Analysis**: Execute `chi_square.py` to calculate term-category associations.
3. **Merging Top Terms**: Run `combine_output.py` to merge top terms associated with each category.

   Example:
$ python preprocess.py < reviews_devset.json > processed_output.txt
$ python chi_square.py processed_output.txt > chi_output.txt
$ python combine_output.py chi_output.txt > merged.txt


## Requirements
- Python
- mrjob library

## License
This project is licensed under the [MIT License](link-to-license).

## Author
[Your Name](link-to-profile) - [Your Email](mailto:your-email@example.com)
