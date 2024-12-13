# CVS_to_JSON
Have a CSV file you want to be a JSON file? Well shit - do I have the code for you!

We start by *Importing Libraries*. We import the `csv` module to read the CSV file and the `json` module to write JSON.

Next, we define the `csv_to_json` function which takes two arguments: the path to the CSV file and the path where the JSON file will be saved.

We then read the CSV file into a dictionary where keys are the header names from the CSV's first row. This ensures each row is read as a dictionary where keys are column names.

`list(csv_reader)` then converts the CSV data into a list of dictionaries.

`json.dump()` writes this list of dictionaries to a JSON file. The indent=4 parameter makes the output pretty-printed with an indentation of 4 spaces, and ensure_ascii=False allows for non-ASCII characters to be written correctly.

Note: I also added a `wd` allowing you to set up your working directory path. 
