import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder


def load_data(filepath='survey_lung_cancer.csv'):
    """Loads the dataset and raises an error if not found."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Could not find '{filepath}'.")

def preprocess_data(df, target_col='LUNG_CANCER'):
    """Preprocesses the data: handles target encoding and one-hot encoding."""
    if target_col not in df.columns:
        raise ValueError(f"Error: Target column '{target_col}' not found.")
        
    y = df[target_col]
    X = df.drop(columns=[target_col])

    # Encode target variable only (YES/NO to 1/0)
    le = LabelEncoder()
    if not pd.api.types.is_numeric_dtype(y):
        y = le.fit_transform(y)

    # Automatic encoding of all other categorical columns in X (One-Hot Encoding)
    X = pd.get_dummies(X, drop_first=True)
    
    return X, y, le

def main():
    print("Loading Lung Cancer dataset...")
    
    # 1. Load the data
    try:
        df = load_data('survey_lung_cancer.csv')
    except FileNotFoundError as e:
        print(e)
        return

    target_col = 'LUNG_CANCER'

    # --- Section 1: Basic Statistics ---
    print("\n--- Basic Statistics ---")
    print("Dataset Shape:", df.shape)
    print("\nStatistical Summary:")
    print(df.describe())
    print("\nTarget Variable Distribution:")
    print(df[target_col].value_counts())
    print("-" * 25)

    # --- Section 2: Exploratory Data Analysis (EDA) ---
    print("\nGenerating Data Visualizations and saving to files...")

    # Set global plot style
    sns.set_theme(style="whitegrid")
    
    # Plot 1: Target variable distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=target_col, hue=target_col, palette='Set2', legend=False)
    plt.title('Distribution of Lung Cancer Diagnosis')
    plt.savefig('distribution_plot.png', bbox_inches='tight')
    plt.close() 
    print("- Saved 'distribution_plot.png'")

    # Plot 2: Diagnosis by Smoking Status
    # 'SMOKING' column is coded as 1 (YES) / 2 (NO) in this dataset
    plt.figure(figsize=(6, 4))

    # Create a temporary dataframe for plotting so we don't alter the actual data
    plot_df = df.copy()
    # Map the numerical/technical values to human-readable strings
    plot_df['SMOKING'] = plot_df['SMOKING'].map({1: 'No', 2: 'Yes'})
    plot_df[target_col] = plot_df[target_col].map({'NO': 'Healthy', 'YES': 'Lung Cancer'})
    
    sns.countplot(data=plot_df, x='SMOKING', hue=target_col, palette='Set1',
                  order=['No', 'Yes'], hue_order=['Lung Cancer', 'Healthy'])
    plt.title('Lung Cancer Diagnosis by Smoking Status')
    plt.xlabel('Smoking Status')
    plt.ylabel('Number of Patients')
    plt.legend(title='Diagnosis', loc='upper left')
    plt.savefig('smoking_impact.png', bbox_inches='tight')
    plt.close()
    print("- Saved 'smoking_impact.png'")

    # Plot 3: Age Distribution by Diagnosis
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x=target_col, y='AGE', palette='Set3', hue=target_col, legend=False)
    plt.title('Age Distribution by Lung Cancer Diagnosis')
    plt.savefig('age_distribution.png', bbox_inches='tight')
    plt.close()
    print("- Saved 'age_distribution.png'")

    # --- Section 3: Data Preprocessing ---
    # Call our helper function to get the clean X and y
    try:
        X, y, le = preprocess_data(df, target_col)
    except ValueError as e:
        print(e)
        return

    # --- Section 4: Data Splitting ---
    # Split the data with stratify to maintain the class ratio
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # --- Section 5: Model Training ---
    print("\nTraining Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # --- Section 6: Model Evaluation and Predictions ---
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # --- Section 7: Post-Model Visualizations ---
    print("Generating post-model visualizations...")
    
    # Plot 4: Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    # Define custom, intuitive labels for the axes
    # 0 = 'NO' -> 'Healthy', 1 = 'YES' -> 'Lung Cancer'
    custom_labels = ['Healthy', 'Lung Cancer']

    # Pass the custom labels to the display function
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=custom_labels)
    disp.plot(cmap='Blues')

    plt.title('Confusion Matrix: Lung Cancer Prediction')
    plt.grid(False) # Remove background grid that interferes with the matrix display
    plt.savefig('confusion_matrix.png', bbox_inches='tight')
    plt.close()
    print("- Saved 'confusion_matrix.png'")

    # Plot 5: Feature Importance
    importances = model.feature_importances_
    features = X.columns

    # Create a DataFrame for the importances and sort them
    feature_df = pd.DataFrame({'Feature': features, 'Importance': importances})
    feature_df = feature_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=feature_df, x='Importance', y='Feature', palette='viridis', hue='Feature', legend=False)
    plt.title('Feature Importance in Random Forest Model')
    plt.xlabel('Importance Score')
    plt.ylabel('Clinical Feature')
    plt.tight_layout()
    plt.savefig('feature_importance.png', bbox_inches='tight')
    plt.close()
    print("- Saved 'feature_importance.png'")
    
    print("\nExecution finished successfully. Check your folder for the generated images.")

if __name__ == "__main__":
    main()





    