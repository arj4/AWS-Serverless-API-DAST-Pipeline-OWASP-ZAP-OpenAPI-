# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 1 |
| Low | 1 |
| Informational | 2 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Info | Informational | https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com | Percentage of responses with status code 4xx | 100 % |
| Info | Informational | https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com | Count of total endpoints | 18    |
| Info | Informational | https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com | Percentage of slow responses | 1 % |




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Cross-Domain Misconfiguration | Medium | 4 |
| Strict-Transport-Security Header Not Set | Low | 4 |
| A Client Error response code was returned by the server | Informational | 19 |
| Storable and Cacheable Content | Informational | 4 |




## Alert Detail



### [ Cross-Domain Misconfiguration ](https://www.zaproxy.org/docs/alerts/10098/)



##### Medium (Medium)

### Description

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `access-control-allow-origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `access-control-allow-origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `access-control-allow-origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `access-control-allow-origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`


Instances: 4

### Solution

Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).
Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

### Reference


* [ https://vulncat.fortify.com/en/detail?category=HTML5&subcategory=Overly%20Permissive%20CORS%20Policy ](https://vulncat.fortify.com/en/detail?category=HTML5&subcategory=Overly%20Permissive%20CORS%20Policy)


#### CWE Id: [ 264 ](https://cwe.mitre.org/data/definitions/264.html)


#### WASC Id: 14

#### Source ID: 3

### [ Strict-Transport-Security Header Not Set ](https://www.zaproxy.org/docs/alerts/10035/)



##### Low (High)

### Description

HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.

* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 4

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)
* [ https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security ](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
* [ https://caniuse.com/stricttransportsecurity ](https://caniuse.com/stricttransportsecurity)
* [ https://datatracker.ietf.org/doc/html/rfc6797 ](https://datatracker.ietf.org/doc/html/rfc6797)


#### CWE Id: [ 319 ](https://cwe.mitre.org/data/definitions/319.html)


#### WASC Id: 15

#### Source ID: 3

### [ A Client Error response code was returned by the server ](https://www.zaproxy.org/docs/alerts/100000/)



##### Informational (High)

### Description

A response code of 404 was returned by the server.
This may indicate that the application is failing to handle unexpected input correctly.
Raised by the 'Alert on HTTP Response Code Error' script

* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/573303427076450402
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/573303427076450402`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/actuator/health
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/actuator/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/computeMetadata/v1/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/computeMetadata/v1/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/latest/meta-data/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/latest/meta-data/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/metadata/instance
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/metadata/instance`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/opc/v1/instance/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/opc/v1/instance/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/4271157331852608018
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/4271157331852608018`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health/
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``


Instances: 19

### Solution



### Reference



#### CWE Id: [ 388 ](https://cwe.mitre.org/data/definitions/388.html)


#### WASC Id: 20

#### Source ID: 4

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/admin`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/debug`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/error`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health
  * Node Name: `https://rq2r4ufdl5.execute-api.ap-south-1.amazonaws.com/prod/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`


Instances: 4

### Solution

Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:
Cache-Control: no-cache, no-store, must-revalidate, private
Pragma: no-cache
Expires: 0
This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3


