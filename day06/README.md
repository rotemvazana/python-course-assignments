# Day 06 

## UniProt:
This assignment uses the UniProt database:

- UniProt is a large web-based biological database containing detailed information about proteins.
- It provides protein sequences, functions, structural information, disease associations, mutations, and annotations.
- UniProt provides biological data in multiple formats, including JSON, FASTA, XML, RDF, and tabular text formats.
- The database is widely used in bioinformatics and molecular biology research.

## Description
Tumor suppressor proteins help prevent uncontrolled cell growth and cancer development.  
Proteins with many documented natural variants may be more frequently associated with disease and cancer-related mutations.

For example, TP53 is one of the most commonly mutated tumor suppressor genes in human cancers, which is reflected by its high number of documented variants in UniProt.

This program uses the UniProt REST API to retrieve information about human tumor suppressor proteins and analyze their documented natural variants (mutations).

The program downloads data for 50 reviewed human tumor suppressor proteins from UniProt and processes the data to determine:

- The number of documented mutations for each protein
- The average mutation count across all proteins
- Which protein has the highest mutational burden (the highest number of documented mutations)

The goal is to identify proteins that may be especially vulnerable to cancer-related dysfunction due to their high number of documented variants.


## How the Program Works

1. Sends a request to the UniProt REST API
2. Retrieves 50 reviewed human (Taxonomy ID: 9606) tumor suppressor proteins
3. Extracts the protein features from the JSON response
4. Counts all entries labeled as:
   - `Natural variant`
5. Calculates and displays:
   - mutation count per protein
   - average mutation count
   - the protein with the highest mutational burden
6. Prints a summary of the analysis


## Files:
* `cancer_mutations_analyzer.py`: The main python script. 
  
* `requirements.txt`: List of required third-party python libraries.


## Requirements
This program uses a third-party library that needs to be installed before running it:
```bash
   pip install -r requirements.txt
```
Or alternatively:
`pip install requests`

## AI Usage
I used [Gemini](https://gemini.google.com/app) to assist with the following things:

prompts:
1. היי, אני רוצה שתעזור לי לכתוב קוד בפייתון שמוריד נתונים מ-UniProt (דרך ה-REST API שלהם). ספציפית, אני רוצה תוכנית שתוריד נתונים של tumor suppressor proteins הומניים ותבצע ניתוח של מספר המוטציות שלהם על ידי ספירת מוטציות מסוג 'Natural variant' המתועדות לכל חלבון, ומציאת ה tumor suppressor proteinבעל מספר המוטציות המתועדות הגבוה ביותר. 
