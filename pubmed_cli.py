import argparse
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Base URL for NCBI E-utilities
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query, retmax=10):
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "usehistory": "y"
    }
    url = BASE_URL + "esearch.fcgi?" + urllib.parse.urlencode(params)
    
    with urllib.request.urlopen(url) as response:
        data = response.read()
    
    root = ET.fromstring(data)
    id_list = [id_elem.text for id_elem in root.findall(".//Id")]
    return id_list

def fetch_details(id_list):
    if not id_list:
        return ""
    
    params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "rettype": "abstract",
        "retmode": "text"
    }
    url = BASE_URL + "efetch.fcgi?" + urllib.parse.urlencode(params)
    
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description="PubMed CLI Connector (Standard Lib)")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("--retmax", type=int, default=2, help="Number of results to retrieve")
    args = parser.parse_args()

    id_list = search_pubmed(args.query, args.retmax)
    if id_list:
        details = fetch_details(id_list)
        print(json.dumps({"ids": id_list, "details": details}))
    else:
        print(json.dumps({"error": "No results found"}))

if __name__ == "__main__":
    main()
