#!/bash/bash
# Send a request to the URL and display only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
