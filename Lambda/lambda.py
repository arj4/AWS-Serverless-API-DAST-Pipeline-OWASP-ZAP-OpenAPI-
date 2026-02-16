import json
import traceback

def _resp(status, body, add_cors=True):
    # Intentionally missing many security headers (ZAP will flag):
    # - Strict-Transport-Security
    # - Content-Security-Policy
    # - X-Frame-Options
    # - X-Content-Type-Options
    # Also intentionally permissive CORS (ZAP will flag)
    headers = {
        "Content-Type": "application/json",
    }

    if add_cors:
        headers.update({
            "Access-Control-Allow-Origin": "*",      # intentionally wide open
            "Access-Control-Allow-Methods": "*",     # intentionally wide open
            "Access-Control-Allow-Headers": "*",     # intentionally wide open
        })

    return {"statusCode": status, "headers": headers, "body": json.dumps(body)}

def lambda_handler(event, context):
    path = event.get("rawPath", "/")
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    
    if path == "/health" and method == "GET":
        return _resp(200, {"ok": True})

    
    if path == "/admin" and method == "GET":
        return _resp(200, {
            "message": "Admin data (intentionally unauthenticated for demo)",
            "secrets": ["internal-config", "service-urls", "debug-flags"]
        })


    if path == "/debug" and method == "GET":
        return _resp(200, {
            "message": "Debug info (intentionally exposed for demo)",
            "requestId": context.aws_request_id,
            "path": path,
            "method": method,
            "event_keys": list(event.keys())
        })


    if path == "/error" and method == "GET":
        try:
            1 / 0
        except Exception:
            return _resp(500, {
                "error": "Something went wrong (intentionally verbose for demo)",
                "stacktrace": traceback.format_exc()   # intentionally leaking stack trace
            })
    return _resp(404, {"error": "Not found"})
