# Usage

curl -X POST http://127.0.0.1:5000/landing-zone \
     -d "appcode=aaa3" \
     -d "tier=nonp" \
     -d "label=nothing"
curl -X GET http://localhost:5000/landing-zone
curl -X GET http://localhost:5000/landing-zone/bb2f9caf-52fb-46f3-8434-05fe8f8ce2f0
