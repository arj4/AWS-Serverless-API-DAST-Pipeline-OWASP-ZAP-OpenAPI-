# AWS Serverless API DAST Pipeline (OWASP ZAP + OpenAPI)

## Overview
This project demonstrates a simple DevSecOps workflow for API security testing on AWS.

I built a small serverless API using AWS Lambda and API Gateway (HTTP API), documented the endpoints using an OpenAPI (Swagger) file, scanned the API using OWASP ZAP running in Docker, and enabled CloudWatch access logging to track requests.

The API is intentionally kept weak in a few safe ways (for learning) so that OWASP ZAP can detect issues like missing security headers, permissive CORS, verbose errors, and unauthenticated sensitive endpoints. Do not use these insecure patterns in real production systems.

## What you will learn
- What AWS Lambda is and how it runs backend code without servers
- What API Gateway is and how it exposes a public API URL
- What a stage is (prod or default) and why deployment matters
- Why OpenAPI (Swagger) helps tools discover and test endpoints
- How to run OWASP ZAP API scans using Docker
- How to enable CloudWatch access logs and count API requests
- How to store scan reports in S3 

## Architecture
- API Gateway (HTTP API) receives requests
- API Gateway forwards requests to Lambda
- Lambda returns JSON responses
- OpenAPI file lists endpoints and base URL
- OWASP ZAP reads OpenAPI and scans endpoints
- ZAP generates HTML and JSON reports locally
- CloudWatch stores API Gateway access logs and Lambda logs
- S3 stores reports 

## AWS services used
### AWS Lambda
Lambda runs your API code. You upload code and AWS executes it only when the API is called.

### API Gateway (HTTP API)
API Gateway provides a public URL for your API and routes requests like GET /health to your Lambda function.

### CloudWatch Logs
CloudWatch stores logs. Lambda logs are created automatically. API Gateway access logs must be enabled on the stage.

### Amazon S3 
S3 is cloud storage used to keep scan reports with history.

## API endpoints in this lab
- GET /health  
  Returns a simple ok response.

- GET /admin  
  Intentionally unauthenticated for demo purposes.

- GET /debug  
  Intentionally returns debug-style information for demo purposes.

- GET /error  
  Intentionally returns a verbose error response for demo purposes.

## Repository structure
- lambda/lambda_function.py  
  Lambda code for the API

- openapi.json  
  OpenAPI (Swagger) file describing the API endpoints

- zap-output/  
  Generated ZAP scan reports (HTML and JSON)

- screenshots/ (optional)  
  Screenshots of API Gateway routes, stage, ZAP report, and CloudWatch logs

## Prerequisites
- AWS account
- Docker installed
- AWS CLI installed (optional, only needed for uploading to S3 using terminal)

## Step 1: Create the Lambda function
1. Open AWS Console and go to Lambda
2. Create a function named (give any name )
3. Choose Python runtime 
4. Paste the code from lambda/lambda_function.py
5. Click Deploy

## Step 2: Create the HTTP API in API Gateway
1. Open AWS Console and go to API Gateway
2. Create API and choose HTTP API
3. Add integration and select your Lambda function zap-lab-api
4. Create routes:
   - GET /health
   - GET /admin
   - GET /debug
   - GET /error
5. Create a stage:
   - Use $default stage or create prod stage
   - Enable auto-deploy if available
6. Copy the Invoke URL from the stage page

## Step 3: Test the API
Open these URLs in the browser or Postman:
- https://YOUR_INVOKE_URL/health
- https://YOUR_INVOKE_URL/admin
- https://YOUR_INVOKE_URL/debug
- https://YOUR_INVOKE_URL/error

If health works, the API deployment is successful.

## Step 4: Update openapi.json
Open openapi.json and set the servers url to your Invoke URL.

Example:
```json
{
  "servers": [
    { "url": "https://YOUR_INVOKE_URL" }
  ]
}
````md
## Step 5: Run OWASP ZAP API scan using Docker
This step runs an automated API security scan against your deployed AWS API using the OpenAPI file.

1. Open Terminal and go to your project folder (the folder that contains openapi.json):
   ```bash
   cd "/your path"
````

2. Create an output folder for reports (only needed once):

   ```bash
   mkdir -p zap-output
   ```

3. Run the OWASP ZAP API scan using Docker:

   
```bash
mkdir -p zap-output

docker run --rm -t \
  -v "$(pwd)/openapi.json:/zap/wrk/openapi.json" \
  -v "$(pwd)/zap-output:/zap/wrk/out" \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-api-scan.py \
    -t /zap/wrk/openapi.json \
    -f openapi \
    -r /zap/wrk/out/zap_report.html \
    -J /zap/wrk/out/zap_report.json \
    -w /zap/wrk/out/zap_warnings.md \
    -z "-config api.disablekey=true"
````


4. After the scan completes, open the HTML report:

   * zap-output/zap_report.html

## Step 6: Enable API Gateway access logging in CloudWatch

This step enables API Gateway access logs so you can see each request and count how many requests were made to the API.

1. Create a CloudWatch log group:

   * Open AWS Console and go to CloudWatch
   * Go to Logs and then Log groups
   * Click Create log group
   * Name it: owasplogs
   * Create the log group

2. Enable access logging on your API stage:

   * Open AWS Console and go to API Gateway
   * Select your HTTP API
   * Go to Stages
   * Click your stage (prod or $default)
   * Open the Logging section and click Edit
   * Enable Access logging
   * Set Log destination to your CloudWatch log group (owasplogs)
   * Set Log format to the JSON below
   * Save changes (if auto deploy is off, click Deploy)

   Example log format:

   ```json
   {
     "requestId":"$context.requestId",
     "ip":"$context.identity.sourceIp",
     "requestTime":"$context.requestTime",
     "httpMethod":"$context.httpMethod",
     "routeKey":"$context.routeKey",
     "path":"$context.path",
     "status":"$context.status",
     "responseLength":"$context.responseLength"
   }
   ```

3. Generate requests so logs appear:

   * Open these endpoints in your browser and refresh a few times:

     * https://YOUR_INVOKE_URL/health
     * https://YOUR_INVOKE_URL/debug

4. Verify logs are being written:

   * Go back to CloudWatch
   * Open Log groups and select owasplogs
   * Open the latest log stream and confirm you see log entries

