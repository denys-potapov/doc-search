# doc-search

Preview should be available at http://167.99.253.189:8000/docs

## Local run

### Install requirments

    sudo apt-get install postgresql tesseract-ocr tesseract-ocr-all
    pip3 install -r requirments.txt

### Prepare the DB

    psql -d documents -h localhost -U postgres < sql/schema.sql

### Start

    TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/ uvicorn main:app --reload --host 0.0.0.0

    TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/ uvicorn main:app --workers 4

## Endpoints

View the interactive docs http://localhost:8000/docs

### Add document

    curl -X 'POST' \
      'http://localhost:8000/documents/' \
      -H 'accept: application/json' \
      -H 'Content-Type: multipart/form-data' \
      -F 'file=@sample2.pdf;type=application/pdf'

Response body:

    {
      "id": "8070eba4-cc5b-4ba0-8a5e-9f290ef7c7ea",
      "status": "PENDING",
      "text": ""
    }

### Search documents

    curl -X 'GET' \
      'http://localhost:8000/search?query=%D0%BF%D0%B0%D0%BF%D0%B5%D1%80%D0%BE%D0%B2%D0%B8%D1%85%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%96%D0%B2' \
      -H 'accept: application/json'

Response body:

    [
      {
        "id": "1c71246b-1ac4-43fb-b5d7-634aa65e6ad4",
        "status": "OK",
        "text": "..."
      },
      {
        "id": "8070eba4-cc5b-4ba0-8a5e-9f290ef7c7ea",
        "status": "OK",
        "text": "..."
      }
    ]


## Deploy

    sudo systemctl start postgresql.service

To log in without a password:

    sudo -u postgres psql postgres
    ALTER USER postgres WITH PASSWORD '11';

