# Day 09 

## Description
This project focuses on predicting lung cancer presence based on various clinical features, lifestyle habits, and demographic factors using a Machine Learning pipeline. The workflow includes Exploratory Data Analysis (EDA), basic statistical analysis, data visualization, automated data preprocessing, and training a **Random Forest Classifier**. The final model achieves an accuracy of over 90%, and the repository includes automated pipeline testing to ensure code reliability and robustness.

You can find more information about the dataset [here](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer/data).

## Files:
* `survey_lung_cancer.csv`: The primary dataset containing clinical survey metrics of patients, including age, gender, smoking status, and various physical symptoms.

* `main.py`: The core pipeline script that loads the data, runs the preprocessing function, trains the Random Forest model, and generates all evaluation metrics and plots.

* `distribution_plot.png`: A bar chart showcasing the distribution of the target variable (`LUNG_CANCER`).

* `smoking_impact.png`: A bar chart evaluating the impact of smoking status on lung cancer diagnosis.
  
* `age_distribution.png`: A box plot showing the age distribution across healthy individuals and lung cancer patients.

* `confusion_matrix.png`: A visually descriptive matrix mapping True Positives, True Negatives, False Positives, and False Negatives.

* `feature_importance.png`: A sorted horizontal bar plot displaying which clinical features and symptoms were most critical for the Random Forest model's predictions.

* `test_main.py`: Contains tests powered by `pytest` to validate the `load_data` function and the logic of the `preprocess_data` function.
  
* `requirements.txt`: List of required third-party python libraries.


## Requirements
This program uses several third-party libraries that need to be installed before running it:
```bash
   pip install -r requirements.txt
```


## How to Download the Data
The dataset is already included in the current folder under the name `survey_lung_cancer.csv`, so no further action is required to run the code.

However, you can also download the data directly from Kaggle:
1. Visit the [Lung Cancer dataset page on Kaggle](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer/data).
2. Download the dataset archive (`.zip` file).
3. Extract the contents of the archive.
4. Rename the extracted file to `survey_lung_cancer.csv` and place it directly in the same directory as `main.py`.


## How to Run

### Running the main script:

```bash
python main.py
```

### Running the Tests:

```bash
pytest test_main.py
```


## AI Usage
I used [Gemini](https://gemini.google.com/app) to assist with the following things:

prompts:

1.	היי מצאתי בkaggle  דאטה סט של סרטן ריאות (צירפתי את הקישור) – תוכל בבקשה לעזור לי לכתוב קוד בפייתון שמאמן מודל ML על הנתונים  ואז חוזה את הדיאגנוזה? https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer/data
2.	אני חושבת שיהיה נחמד להוסיף קצת סטטיסטיקה בסיסית על הנתונים, קצת graphical visualization של הדאטה, וגם confusion matrix - תוכל בבקשה לעזור לי?
3.	תעזור לי לכתוב טסטים לקוד


