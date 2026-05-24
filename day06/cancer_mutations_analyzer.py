import requests

def fetch_tumor_suppressors():
    # Query the UniProt API to download 50 human tumor-suppressor proteins
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
        
        # Safely extract the protein name
        try:
            name = p['proteinDescription']['recommendedName']['fullName']['value']
        except KeyError:
            name = accession
            
        # Scan protein features to find genetic mutations/variations
        features = p.get('features', [])
        
        # Filter and count only 'Natural variant' features (natural/disease-related mutations)
        variants = [f for f in features if f.get('type') == 'Natural variant']
        mutation_count = len(variants)
        
        # Short printout for each protein
        short_name = name[:30] + "..." if len(name) > 30 else name
        print(f"ID: {accession} | Protein: {short_name:33} | Documented Mutations: {mutation_count}")
        
        # Update variables for the summary
        total_mutations += mutation_count
        if mutation_count > most_mutated_protein["mutation_count"]:
            most_mutated_protein = {
                "name": name,
                "mutation_count": mutation_count,
                "id": accession
            }
            
    # --- Processing Summary ---
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