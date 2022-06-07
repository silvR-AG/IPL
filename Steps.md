# Data representation project

### Prerequsites:
* Download the data sets from source
* Create and convert the YAML file if necessary.
* Install python3
* Install pip/pip3
* Install virtualenv

#### Steps to follow
1. Import the required libraries i.e matplotlib, csv
2. Open the file using file1 = open ('file.csv') \\Open all files
3. Use fileobj=csv.reader(filename) to create objects for the files.
4. Extract field names using the field = next(fileobj).

###### Steps for Total runs
1. Import data under batting_team and total_runs rows.
2. Create a list 'x' using batting_team, where - only new team names will be added, skip already saved names.
3. Create another list 'y', using total_runs, where if the corresponding batting_value does not change, summate the values and put it under that index.
4. plot a graph of x and y.
5. Or create another csv file with sorted datas.

###### Steps for Top batsmen
1. Repeat the previous steps, where instead of batting_team rows, use batsmen rows.

###### Steps for Foreign empire
1. to be worked on later.
