from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from tm_extended_module_copy import calculate_tm

app = FastAPI(
    title="DNA Sequence Analysis API",
    description="An API to calculate Tm, GC content, and GC clamp of a DNA sequence.",
    version="1.0.0"
)

class SequenceRequest(BaseModel):
    sequence: str = Field(..., json_schema_extra={"example": "ATCGATCGATCGATCG"})

@app.get("/", response_class=HTMLResponse)
def home():
    """
    Serves the modern Dark Mode frontend interface.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DNA Sequence Analyzer</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { 
                background-color: #121212; 
                color: #e0e0e0; 
                padding-top: 60px; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            }
            .card { 
                background-color: #1e1e1e; 
                border-radius: 12px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.8); 
                border: 1px solid #333; 
            }
            .form-control { 
                background-color: #2d2d2d; 
                color: #00adb5; 
                border: 1px solid #444; 
                font-family: 'Courier New', Courier, monospace; 
                letter-spacing: 2px;
                font-size: 1.1em;
            }
            .form-control:focus { 
                background-color: #2a2a2a; 
                color: #00adb5; 
                border-color: #00adb5; 
                box-shadow: 0 0 0 0.25rem rgba(0, 173, 181, 0.25); 
            }
            .form-control::placeholder {
                color: #666;
                letter-spacing: normal;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            h2 { color: #ffffff; font-weight: 600; letter-spacing: 1px; }
            .btn-primary { 
                background-color: #00adb5; 
                border: none; 
                padding: 12px 20px; 
                border-radius: 8px; 
                font-weight: bold; 
                color: #121212; 
                transition: all 0.3s ease;
            }
            .btn-primary:hover { 
                background-color: #007a80; 
                color: #ffffff; 
                transform: translateY(-2px);
            }
            .result-box { 
                background-color: #252526; 
                border-left: 4px solid #00adb5; 
                padding: 25px; 
                border-radius: 8px; 
                margin-top: 25px; 
                display: none; 
            }
            .border-bottom { border-color: #444 !important; }
            .badge-custom { font-size: 0.9em; padding: 8px 12px; border-radius: 6px; font-weight: 500; }
            .text-muted { color: #9e9e9e !important; }
            .spinner-border { 
                display: none; 
                width: 1.2rem; 
                height: 1.2rem; 
                border-width: 0.2em;
                vertical-align: middle;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8 col-lg-7">
                    <div class="card p-5">
                        <h2 class="text-center mb-4">DNA Sequence Analyzer</h2>
                        <div class="mb-4">
                            <label for="sequenceInput" class="form-label text-muted">INPUT SEQUENCE (5' &rarr; 3')</label>
                            <textarea class="form-control text-uppercase" id="sequenceInput" rows="4" placeholder="e.g. ATCGATCGATCGATCG"></textarea>
                        </div>
                        <div class="d-grid">
                            <button class="btn btn-primary" onclick="analyzeSequence()" id="analyzeBtn">
                                ANALYZE SEQUENCE 
                                <span class="spinner-border text-dark" id="loadingSpinner" role="status"></span>
                            </button>
                        </div>
                        
                        <div id="errorBox" class="alert alert-danger mt-4" style="display: none; background-color: #4a1919; color: #ffb3b3; border: 1px solid #800000;"></div>

                        <div id="resultBox" class="result-box shadow-sm">
                            <h5 class="mb-3 border-bottom pb-3 text-light">Analysis Results</h5>
                            <div class="row mb-3 align-items-center">
                                <div class="col-7 text-muted">Melting Temperature (Tm):</div>
                                <div class="col-5 fs-5 fw-bold text-light" id="resTm"></div>
                            </div>
                            <div class="row mb-3 align-items-center">
                                <div class="col-7 text-muted">Sequence Length:</div>
                                <div class="col-5 fw-bold text-light" id="resLength"></div>
                            </div>
                            <div class="row mb-3 align-items-center">
                                <div class="col-7 text-muted">GC Content:</div>
                                <div class="col-5 fw-bold text-light" id="resGcContent"></div>
                            </div>
                            <div class="row mb-3 align-items-center">
                                <div class="col-7 text-muted">GC Content Status:</div>
                                <div class="col-5" id="resGcStatus"></div>
                            </div>
                            <div class="row mb-3 align-items-center">
                                <div class="col-7 text-muted">3' GC Clamp Check:</div>
                                <div class="col-5" id="resGcClamp"></div>
                            </div>
                            <div class="row mt-4 pt-3 border-top border-secondary text-muted" style="font-size: 0.85em;">
                                <div class="col-12">Calculation Method: <span id="resMethod" class="text-light"></span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            async function analyzeSequence() {
                const sequence = document.getElementById('sequenceInput').value;
                const resultBox = document.getElementById('resultBox');
                const errorBox = document.getElementById('errorBox');
                const spinner = document.getElementById('loadingSpinner');
                const btn = document.getElementById('analyzeBtn');
                
                resultBox.style.display = 'none';
                errorBox.style.display = 'none';

                if (!sequence.trim()) {
                    errorBox.innerText = "Error: Please enter a sequence.";
                    errorBox.style.display = 'block';
                    return;
                }

                // Show spinner and disable button
                spinner.style.display = 'inline-block';
                btn.disabled = true;

                try {
                    const response = await fetch('/analyze', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ sequence: sequence.toUpperCase() })
                    });
                    
                    const data = await response.json();
                    
                    if (!response.ok) {
                        errorBox.innerText = data.detail;
                        errorBox.style.display = 'block';
                    } else {
                        document.getElementById('resTm').innerText = data.tm + ' °C';
                        document.getElementById('resLength').innerText = data.length + ' bp';
                        document.getElementById('resGcContent').innerText = data.gc_content + '%';
                        
                        const statusColor = data.gc_status === 'Optimal' ? 'bg-success' : 'bg-warning text-dark';
                        document.getElementById('resGcStatus').innerHTML = `<span class="badge ${statusColor} badge-custom">${data.gc_status}</span>`;
                        
                        const clampColor = data.clamp_status === 'Good' ? 'bg-success' : 'bg-warning text-dark';
                        document.getElementById('resGcClamp').innerHTML = `<span class="badge ${clampColor} badge-custom">${data.clamp_status}</span>`;
                        
                        document.getElementById('resMethod').innerText = data.method;
                        
                        // Small delay to make the loading animation visible
                        setTimeout(() => {
                            resultBox.style.display = 'block';
                        }, 300);
                    }
                } catch (error) {
                    errorBox.innerText = "Network error: Could not connect to the server.";
                    errorBox.style.display = 'block';
                } finally {
                    // Hide spinner and enable button
                    setTimeout(() => {
                        spinner.style.display = 'none';
                        btn.disabled = false;
                    }, 300);
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/analyze")
def analyze_sequence_get(sequence: str):
    result, error = calculate_tm(sequence)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return result

@app.post("/analyze")
def analyze_sequence_post(request: SequenceRequest):
    result, error = calculate_tm(request.sequence)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return result