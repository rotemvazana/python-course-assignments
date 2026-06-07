# Day 08 

## Description

This project is based on the DNA primer analysis project developed in Day 04.

The original business logic from Day 04 was copied and reused in this project without modifying its functionality. The same business logic is now integrated into a FastAPI web application.

The application analyzes DNA primer sequences and performs several quality-control checks commonly used in molecular biology, including:

- Melting Temperature (Tm) calculation
- GC Content calculation and validation
- GC Clamp evaluation
- DNA sequence validation

* More detailed information about the business logic can be found in the README.md of day04.

The project includes automated tests for both the original business logic (copy from dy04) and the new web application.

## Files:
* `tm_extended_module_copy.py`: A copy of the day04 business logic module. Contains the core primer sequence analysis functions used by both the original project and the web application.

* `test_tm_extended_module_copy.py`: A copy of the day04 tests. Verifies that the original business logic behaves correctly.

* `main.py`: FastAPI web application that provides both a graphical user interface and API endpoints for primer sequence analysis. The application uses the function from tm_extended_module_copy.py to perform all calculations.

* `test_main.py`: Contains tests for the FastAPI application. The tests verify endpoint behavior, valid responses, and error handling.
  
* `requirements.txt`: List of required third-party python libraries.


## Requirements
This program uses several third-party libraries that need to be installed before running it:
```bash
   pip install -r requirements.txt
```

## How to Run

### Start the Web Application:
Run the FastAPI server using:

```bash
uvicorn main:app --reload
```

After the server starts, open your browser and navigate to:

```text
http://127.0.0.1:8000
```

### Running the Tests

#### Business Logic Tests

```bash
pytest test_tm_extended_module_copy.py
```

#### Web Application Tests

```bash
pytest test_main.py
```

#### Run All Tests

```bash
pytest
```


## AI Usage
I used [Gemini](https://gemini.google.com/app) to assist with the following things:

prompts:

1. היי, צירפתי לך קוד של תוכנית שכתבתי בעבר בפייתון, תוכל בבקשה לעזור לי לבנות לו web application מבלי לשנות את הbusiness logic. ספציפית, אני רוצה שתכתוב לי web application שמקבל מחרוזת של רצף דנ״א ומחזיר את הדברים כמו בקוד הבא. אני מעדיפה שלא תשתמש בflask. ותכתוב בבקשה גם טסטים לweb application.
2. תוכל בבקשה לשפר את הנראות של האתר? אני גם מעדיפה dark mode.




