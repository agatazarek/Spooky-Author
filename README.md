# Spooky-Author

### Table of Contents

1. [Project summary](#summary)
2. [Application overview](#overview)
2. [Requirements](#requirements)
6. [Instructions](#instructions)
5. [Licensing and Acknowledgements](#licensing)

### Project summary:<a name="summary"></a>
A month ago it came out that I inherited an old haunted Library which was closed since around 1900. When I visited the library and opened the door it turned out that the area's been a mess. Since I love books I decided to clean the place and open it for everyones usage. The problem was that half of the books did not have a cover so I was not able to categorize them in any way. In the will it was written that the books were only written by one of the three authors - Edgar Allan Poe, Mary Shelley, HP Lovecraft. To create covers and organize the library I need to create a machine learning model that will predict the author base on the content of the book.

Files descriptions:
books.csv - the training set

Data:

id - a unique identifier for each sentence
text - some text written by one of the authors
author - the author of the sentence (EAP: Edgar Allan Poe, HPL: HP Lovecraft; MWS: Mary Wollstonecraft Shelley)

### Application overview:<a name="overview"></a>

- `app` directory contains python script for running the app,
- `Spooky-Author.ipynb` contains notebook with problem description, data analysis and training the model.

### Requirements:<a name="requirements"></a>

- `pandas`
- `pickle`
- `nltk`
- `sklearn`
- `plotly`

### Instructions:<a name="instructions"></a>

1. Go to project app directory `cd app`.

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Licensing and Acknowledgements<a name="licensing"></a>:

Must give credit to Udacity courses for some of code ideas, and to kaggle for the data. You can find the Licensing for the data and other descriptive information at the [Kaggle link](https://www.kaggle.com/c/spooky-author-identification). Otherwise, feel free to use the code here as you would like!