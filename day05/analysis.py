import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def analyze_protocol_efficiency(filepath, group_a, group_b):
    """
    Loads the Excel file and counts the number of identified proteins per sample
    and per protocol group to compare detection efficiency.
    """
    df = pd.read_excel(filepath)
    all_cols = group_a + group_b
    
    # Ensure all intensity columns are forced to numeric type
    for col in all_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Create a clean DataFrame with Gene names as index (or Protein Group as fallback)
    df['Display_Name'] = df['Genes'].fillna(df['Protein.Group'])
    df_data = df.set_index('Display_Name')[all_cols]
    
    # Aggregate duplicate genes if any by taking their mean
    df_data = df_data.groupby(level=0).mean()
    
    # A protein is considered successfully identified if it is not NaN and greater than 0
    binary_matrix = (df_data.notna() & (df_data > 0)).astype(int)
    
    # Count how many proteins were detected in each individual sample
    protein_counts = binary_matrix.sum()
    
    # Prepare data for plotting and statistical summary
    results = []
    for sample in group_a:
        results.append({'Protocol': 'Lab Protocol (50 cells, n=5)', 'Protein_Count': protein_counts[sample]})
    for sample in group_b:
        results.append({'Protocol': 'Other Protocol (100 cells, n=2)', 'Protein_Count': protein_counts[sample]})
        
    summary_df = pd.DataFrame(results)
    return summary_df

def plot_efficiency(summary_df, output_path="protocol_comparison.png"):
    """
    Generates a professional bar plot comparing the number of identified proteins
    between the two protocols, including error bars for consistency.
    """
    plt.figure(figsize=(8, 6))
    
    # Create bar plot with error bars (representing standard deviation across technical replicates)
    sns.barplot(
        data=summary_df, 
        x='Protocol', 
        y='Protein_Count', 
        hue='Protocol',
        errorbar='sd', 
        palette='Set2',
        capsize=0.1
    )
    
    # Add individual sample points on top of the bars to show raw data transparency
    sns.stripplot(
        data=summary_df, 
        x='Protocol', 
        y='Protein_Count', 
        color='black', 
        size=6, 
        jitter=0.1,
        dodge=False
    )
    
    plt.xticks([0, 1], ['Lab Protocol\n(50 cells, n=5)', 'Other Protocol\n(100 cells, n=2)'])
    plt.title("Comparison of Identified Proteins per Protocol", fontsize=13, fontweight='bold')
    plt.ylabel("Mean Number of Identified Proteins (±SD)", fontsize=11)
    plt.xlabel("Experimental Protocol", fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Save the generated benchmarking plot
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Success! Protocol efficiency comparison graph saved to: {output_path}")

if __name__ == "__main__":
    # Exact column names from your mass spec file
    protocol_a_samples = [
        r"E:\Astral_data_backup\AP_20260426_Human_DIA_Direct_50SPD_noTCEPCAA-2.raw",
        r"E:\Astral_data_backup\AP_20260426_Human_DIA_Direct_50SPD_noTCEPCAA-3.raw",
        r"E:\Astral_data_backup\AP_20260426_Human_DIA_Direct_50SPD_noTCEPCAA-5.raw",
        r"E:\Astral_data_backup\AP_20260426_Human_DIA_Direct_50SPD_noTCEPCAA-1.raw",
        r"E:\Astral_data_backup\AP_20260426_Human_DIA_Direct_50SPD_noTCEPCAA-4.raw"
    ]
    
    protocol_b_samples = [
        r"Z:\astral_rawdata\AP_20260415_Human_DIA_Direct_50SPD_Plate1MM-2.raw",
        r"Z:\astral_rawdata\AP_20260415_Human_DIA_Direct_50SPD_Plate1MM-1.raw"
    ]
    
    # Your clean filename
    input_filename = "data.xlsx"
    
    if os.path.exists(input_filename):
        print("Analyzing file to count identified proteins per protocol...")
        summary_data = analyze_protocol_efficiency(input_filename, protocol_a_samples, protocol_b_samples)
        
        # Display the printout table in the terminal so you can see the exact numbers immediately
        print("\n--- Summary Table ---")
        print(summary_data.to_string(index=False))
        print("----------------------\n")
        
        print("Generating comparison plot...")
        plot_efficiency(summary_data)
    else:
        print(f"Error: Could not find the file '{input_filename}' in the current directory.")