curl -X 'POST' \
  'http://localhost:40111/documents/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@2.pdf;type=application/pdf'
