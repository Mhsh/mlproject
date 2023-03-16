Project to take any csv and try to generate model by selecting multiple models with their best parameter using GridSearch.

Usage:
python src/main.py /opt/dataset/settings.yml

settings.xml need to place at location 'opt/dataset/settings.yml'

Contents of settings.yml

dataset:
   /opt/dataset/stud.csv

target_feature:
   - "math_score"
numerical_columns:
   - "writing_score"
   - "reading_score"
categorical_columns:
   - "gender"
   - "race_ethnicity"
   - "parental_level_of_education"
   - "lunch"
   - "test_preparation_course"


numerical and categorical column depends on dataset. For stud.cvs above are the values.

For sample - stud.cvs and settings.xml are committed in data folder. You can use this location and pass the relative location to the program.
