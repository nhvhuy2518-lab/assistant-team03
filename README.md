# Study Assistant - starter
A starter repository for the CSC10014 Smart Virtual Assistant project.

## Setup
To set up this project on a fresh machine, follow these steps:

1. Clone the repository:
`git clone https://github.com/taolagautruc3001/lab01-lhphieu2531-collab.git`
`cd lab01-lhphieu2531-collab`

2. Create and activate a virtual environment:
- On **macOS/Linux**:
  `python -m venv .venv`
  `source .venv/bin/activate`

- On **Windows**:
  `python -m venv .venv`
  `.venv\Scripts\activate`

3. Install dependencies:
`pip install -r requirements.txt`
`pip install -e .`

## Run
To run the assistant, use the following command:
`python -m assistant "where is the IT helpdesk?"`

## Test
To run the automated tests, execute:
`pytest -q`