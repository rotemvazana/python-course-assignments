import requests

def fetch_tumor_suppressors():
    # פנייה ל-API של יוניפרוט להורדת 50 חלבונים אנושיים מדכאי-סרטן
    url = "https://rest.uniprot.org/uniprotkb/search"
    params = {
        "query": "tumor suppressor AND (taxonomy_id:9606) AND (reviewed:true)",
        "format": "json",
        "size": 50 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_mutation_data(data):
    if not data or 'results' not in data or len(data['results']) == 0:
        print("No proteins found.")
        return

    proteins = data['results']
    print(f"Successfully downloaded {len(proteins)} Tumor Suppressor proteins.\n")
    
    total_mutations = 0
    most_mutated_protein = {"name": "", "mutation_count": 0, "id": ""}
    
    print("--- Analyzing Mutational Burden ---")
    
    for p in proteins:
        accession = p['primaryAccession']
        
        # חילוץ שם החלבון בצורה בטוחה
        try:
            name = p['proteinDescription']['recommendedName']['fullName']['value']
        except KeyError:
            name = accession
            
        # סריקת מאפייני החלבון (features) כדי למצוא מוטציות/וריאציות גנטיות
        features = p.get('features', [])
        
        # סינון וספירה רק של מאפיינים מסוג 'Natural variant' (מוטציות טבעיות/קשורות למחלה)
        variants = [f for f in features if f.get('type') == 'Natural variant']
        mutation_count = len(variants)
        
        # הדפסה קצרה לכל חלבון
        short_name = name[:30] + "..." if len(name) > 30 else name
        print(f"ID: {accession} | Protein: {short_name:33} | Documented Mutations: {mutation_count}")
        
        # עדכון משתנים לצורך הסיכום
        total_mutations += mutation_count
        if mutation_count > most_mutated_protein["mutation_count"]:
            most_mutated_protein = {
                "name": name,
                "mutation_count": mutation_count,
                "id": accession
            }
            
    # --- סיכום העיבוד ---
    avg_mutations = total_mutations / len(proteins)
    
    print("\n--- Data Processing Insights ---")
    print(f"Average documented mutations per tumor suppressor: {avg_mutations:.1f}")
    
    if most_mutated_protein["mutation_count"] > 0:
        print("\n🧬 Protein with the Highest Mutational Burden:")
        print(f"Name: {most_mutated_protein['name']}")
        print(f"UniProt ID: {most_mutated_protein['id']}")
        print(f"Total Documented Variants/Mutations: {most_mutated_protein['mutation_count']}")
        print("(Proteins with high mutation counts are often central drivers in cancer development when they fail, such as TP53).")

if __name__ == "__main__":
    print("Starting Tumor Suppressor Mutational Analyzer...")
    json_data = fetch_tumor_suppressors()
    process_mutation_data(json_data)