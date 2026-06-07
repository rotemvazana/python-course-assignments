# test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint_returns_html():
    """
    Verify that the home endpoint returns a valid HTML page and the application title instead of an error or a raw file.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "DNA Sequence Analyzer" in response.text

def test_analyze_valid_sequence_short_get():
    """
    Test a short sequence (Wallace formula) via a GET request.
    """
    response = client.get("/analyze?sequence=ATCGATCG")
    assert response.status_code == 200
    data = response.json()
    assert data["length"] == 8
    assert data["method"] == "Short primer formula"
    assert "tm" in data

def test_analyze_valid_sequence_long_post():
    """
    Test a long sequence via a POST request with a JSON body. 
    """
    payload = {"sequence": "ATCGATCGATCGATCGATCG"}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["length"] == 20
    assert data["method"] == "Long primer formula"
    assert data["gc_status"] == "Optimal"
    assert data["gc_clamp"] is True

def test_analyze_empty_sequence():
    """
    Verify that the system returns a 400 error when an empty sequence is sent.    
    """
    response = client.get("/analyze?sequence=")
    assert response.status_code == 400
    assert "Error: Sequence is empty" in response.json()["detail"]

def test_analyze_invalid_characters():
    """
    Verify that the system detects non-nucleotide characters (A, T, C, G) and returns an error.
    """
    payload = {"sequence": "ATCGXATCG"}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 400
    assert "Error: Invalid sequence" in response.json()["detail"]