---
title: Week Six Assignment Problem Statement v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="week-six-assignment-problem-statement">Week Six Assignment Problem Statement v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<div>In this assignment, you have to create a RESTful API, database models using Flask-RESTful  and     flask-SQLAlchemy. We list below instructions to be followed in  preparing and submitting the solution. <h3>General instructions:</h3> <ol> 
  <li> Submit a single .zip file containing all your submission files and folders, the name of which should be "roll_number.zip". E.g.: 21f1000000.zip </li>
  <li>The folder structure inside the zip file should be as follows:</li>
  <ol type = "I">
    <li>The Python program must be written inside a file named "app.py". This file must reside inside the root folder.</li>
    <li> The database file named "api_database.sqlite3". You are not required to submit this database file with your submission.</li>
  </ol>
<li> You should not keep any code inside the scope of the condition " if __name__ == '__main__' " except run() call. </li> <li> Allowed Python packages: flask, flask-sqlalchemy, flask-restful, and any standard Python3 package.</li> <li> The database URI must be the same as: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'.</li> <li> You should not use create_all() call in your program to create a database.</li> </ol> </div>
<h3> Course Table Schema </h3>  <table>
  <thead>
    <th>Column Name</th>
    <th>Column Type</th>
    <th>Constraints</th>
  </thead>
  <tbody>
  <tr>
    <td>course_id</td>
    <td>Integer</td>
    <td>Primary Key, Auto Increment</td>
  </tr>
  <tr>
    <td>course_name</td>
    <td>String</td>
    <td>Not Null</td>
  </tr>
  <tr>
    <td>course_code</td>
    <td>String</td>
    <td>Unique, Not Null</td>
  </tr>      
  <tr>
    <td>course_description</td>
    <td>String</td>
    <td></td>
  </tr>         
</tbody> </table>
<h3> Student Table Schema </h3>  <table>
  <thead>
    <th>Column Name</th>
    <th>Column Type</th>
    <th>Constraints</th>
  </thead>
  <tbody>
  <tr>
    <td>student_id</td>
    <td>Integer</td>
    <td>Primary Key, Auto Increment</td>
  </tr>
  <tr>
    <td>roll_number</td>
    <td>String</td>
    <td>Unique, Not Null</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>String</td>
    <td>Not Null</td>
  </tr>      
  <tr>
    <td>last_name</td>
    <td>String</td>
    <td></td>
  </tr>         
</tbody> </table>

<h3> Enrollment Table Schema </h3>  <table>
  <thead>
    <th>Column Name</th>
    <th>Column Type</th>
    <th>Constraints</th>
  </thead>
  <tbody>
  <tr>
    <td>enrollment_id</td>
    <td>Integer</td>
    <td>Primary Key, Auto Increment</td>
  </tr>
  <tr>
    <td>student_id</td>
    <td>Integer</td>
    <td>Foreign Key (student.student_id), Not Null</td>
  </tr>
  <tr>
    <td>course_id</td>
    <td>Integer</td>
    <td>Foreign Key (course.course_id), Not Null</td>
</tbody> </table>
<h3> Error Codes </h3>  <table>
  <thead>
    <th>Resource</th>
    <th>Error Code</th>
    <th>Message</th>
  </thead>
  <tbody>
  <tr>
    <td>Course</td>
    <td>COURSE001</td>
    <td>Course Name is required</td>
  </tr>
  <tr>
    <td>Course</td>
    <td>COURSE002</td>
    <td>Course Code is required</td>
  </tr>
  
  <tr>
    <td>Student</td>
    <td>STUDENT001</td>
    <td>Roll Number required</td>
  </tr>
  <tr>
    <td>Student</td>
    <td>STUDENT002</td>
    <td>First Name is required</td>
  </tr>
  
  <tr>
    <td>Enrollment</td>
    <td>ENROLLMENT001</td>
    <td>Course does not exist</td>
  </tr>
  <tr>
    <td>Enrollment</td>
    <td>ENROLLMENT002</td>
    <td>Student does not exist.</td>
  </tr>  
</tbody> </table>

Base URLs:

* <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>

<h1 id="week-six-assignment-problem-statement-default">Default</h1>

## get__api_course_{course_id}

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:5000/api/course/{course_id} \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:5000/api/course/{course_id} HTTP/1.1
Host: 127.0.0.1:5000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/course/{course_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:5000/api/course/{course_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:5000/api/course/{course_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:5000/api/course/{course_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/course/{course_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:5000/api/course/{course_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/course/{course_id}`

Operation to Read course resource.

<h3 id="get__api_course_{course_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|course_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "course_id": 201,
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}
```

<h3 id="get__api_course_{course_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request Successful|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Course not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get__api_course_{course_id}-responseschema">Response Schema</h3>

Status Code **200**

*course object*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» course_id|integer|false|none|none|
|» course_name|string|false|none|none|
|» course_code|string|false|none|none|
|» course_description|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## put__api_course_{course_id}

> Code samples

```shell
# You can also use wget
curl -X PUT http://127.0.0.1:5000/api/course/{course_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT http://127.0.0.1:5000/api/course/{course_id} HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/course/{course_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put 'http://127.0.0.1:5000/api/course/{course_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:5000/api/course/{course_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://127.0.0.1:5000/api/course/{course_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/course/{course_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://127.0.0.1:5000/api/course/{course_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/course/{course_id}`

Operation to update the course resource.

> Body parameter

```json
{
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}
```

<h3 id="put__api_course_{course_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|course_id|path|integer|true|none|
|body|body|object|false|none|
|» course_name|body|string|false|none|
|» course_code|body|string|false|none|
|» course_description|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "course_id": 201,
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}
```

<h3 id="put__api_course_{course_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfuly updated|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Course not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="put__api_course_{course_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» course_id|integer|false|none|none|
|» course_name|string|false|none|none|
|» course_code|string|false|none|none|
|» course_description|string|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_course_{course_id}

> Code samples

```shell
# You can also use wget
curl -X DELETE http://127.0.0.1:5000/api/course/{course_id}

```

```http
DELETE http://127.0.0.1:5000/api/course/{course_id} HTTP/1.1
Host: 127.0.0.1:5000

```

```javascript

fetch('http://127.0.0.1:5000/api/course/{course_id}',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete 'http://127.0.0.1:5000/api/course/{course_id}',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('http://127.0.0.1:5000/api/course/{course_id}')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://127.0.0.1:5000/api/course/{course_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/course/{course_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://127.0.0.1:5000/api/course/{course_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/course/{course_id}`

Operation to delete the course resource

<h3 id="delete__api_course_{course_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|course_id|path|integer|true|none|

<h3 id="delete__api_course_{course_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully Deleted|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Course not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Intenal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_course

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:5000/api/course \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://127.0.0.1:5000/api/course HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/course',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://127.0.0.1:5000/api/course',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:5000/api/course', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:5000/api/course', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/course");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:5000/api/course", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/course`

Operation to create the course resource

> Body parameter

```json
{
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}
```

<h3 id="post__api_course-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» course_name|body|string|false|none|
|» course_code|body|string|false|none|
|» course_description|body|string|false|none|

> Example responses

> 201 Response

```json
{
  "course_id": 201,
  "course_name": "Maths1",
  "course_code": "MA101",
  "course_description": "Course Description Example"
}
```

<h3 id="post__api_course-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|Inline|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|course_code already exist|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="post__api_course-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» course_id|integer|false|none|none|
|» course_name|string|false|none|none|
|» course_code|string|false|none|none|
|» course_description|string|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_student_{student_id}

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:5000/api/student/{student_id} \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:5000/api/student/{student_id} HTTP/1.1
Host: 127.0.0.1:5000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/student/{student_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:5000/api/student/{student_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:5000/api/student/{student_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:5000/api/student/{student_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student/{student_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:5000/api/student/{student_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/student/{student_id}`

Operation to read student resource

<h3 id="get__api_student_{student_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "student_id": 101,
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
```

<h3 id="get__api_student_{student_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request Successful|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Student not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="get__api_student_{student_id}-responseschema">Response Schema</h3>

Status Code **200**

*student object*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» student_id|integer|false|none|none|
|» first_name|string|false|none|none|
|» last_name|string|false|none|none|
|» roll_number|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## put__api_student_{student_id}

> Code samples

```shell
# You can also use wget
curl -X PUT http://127.0.0.1:5000/api/student/{student_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT http://127.0.0.1:5000/api/student/{student_id} HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/student/{student_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put 'http://127.0.0.1:5000/api/student/{student_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:5000/api/student/{student_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://127.0.0.1:5000/api/student/{student_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student/{student_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://127.0.0.1:5000/api/student/{student_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/student/{student_id}`

Operation to update the student resource

> Body parameter

```json
{
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
```

<h3 id="put__api_student_{student_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|path|integer|true|none|
|body|body|object|false|none|
|» first_name|body|string|false|none|
|» last_name|body|string|false|none|
|» roll_number|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "student_id": 101,
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
```

<h3 id="put__api_student_{student_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully updated|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Student not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="put__api_student_{student_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» student_id|integer|false|none|none|
|» first_name|string|false|none|none|
|» last_name|string|false|none|none|
|» roll_number|string|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_student_{student_id}

> Code samples

```shell
# You can also use wget
curl -X DELETE http://127.0.0.1:5000/api/student/{student_id}

```

```http
DELETE http://127.0.0.1:5000/api/student/{student_id} HTTP/1.1
Host: 127.0.0.1:5000

```

```javascript

fetch('http://127.0.0.1:5000/api/student/{student_id}',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete 'http://127.0.0.1:5000/api/student/{student_id}',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('http://127.0.0.1:5000/api/student/{student_id}')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://127.0.0.1:5000/api/student/{student_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student/{student_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://127.0.0.1:5000/api/student/{student_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/student/{student_id}`

Operation to delete the course resource

<h3 id="delete__api_student_{student_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|path|integer|true|none|

<h3 id="delete__api_student_{student_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully Deleted|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Student not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_student

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:5000/api/student \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://127.0.0.1:5000/api/student HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/student',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://127.0.0.1:5000/api/student',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:5000/api/student', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:5000/api/student', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:5000/api/student", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/student`

Operation to create the student resource

> Body parameter

```json
{
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
```

<h3 id="post__api_student-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» first_name|body|string|false|none|
|» last_name|body|string|false|none|
|» roll_number|body|string|false|none|

> Example responses

> 201 Response

```json
{
  "student_id": 101,
  "first_name": "Narendra",
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
```

<h3 id="post__api_student-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|Inline|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Student already exist|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="post__api_student-responseschema">Response Schema</h3>

Status Code **201**

*student object*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» student_id|integer|false|none|none|
|» first_name|string|false|none|none|
|» last_name|string|false|none|none|
|» roll_number|string|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_student_{student_id}_course

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:5000/api/student/{student_id}/course \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:5000/api/student/{student_id}/course HTTP/1.1
Host: 127.0.0.1:5000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/student/{student_id}/course',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:5000/api/student/{student_id}/course',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:5000/api/student/{student_id}/course', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:5000/api/student/{student_id}/course', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student/{student_id}/course");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:5000/api/student/{student_id}/course", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/student/{student_id}/course`

URL to get the list of enrollments, the student is enrolled in. This path belongs to the Enrollment table.

<h3 id="get__api_student_{student_id}_course-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|path|integer|true|none|

> Example responses

> 200 Response

```json
[
  {
    "enrollment_id": 10,
    "student_id": 101,
    "course_id": 201
  }
]
```

<h3 id="get__api_student_{student_id}_course-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request Successful|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid Student Id|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Student is not enrolled in any course|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get__api_student_{student_id}_course-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» enrollment_id|integer|false|none|none|
|» student_id|integer|false|none|none|
|» course_id|integer|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_student_{student_id}_course

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:5000/api/student/{student_id}/course \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://127.0.0.1:5000/api/student/{student_id}/course HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "course_id": 12345
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/student/{student_id}/course',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://127.0.0.1:5000/api/student/{student_id}/course',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:5000/api/student/{student_id}/course', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:5000/api/student/{student_id}/course', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student/{student_id}/course");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:5000/api/student/{student_id}/course", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/student/{student_id}/course`

Add student enrollment aka enroll the student to the course. This path belongs to the Enrollment table.

> Body parameter

```json
{
  "course_id": 12345
}
```

<h3 id="post__api_student_{student_id}_course-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|path|integer|true|none|
|body|body|object|false|none|
|» course_id|body|integer|false|none|

> Example responses

> 201 Response

```json
[
  {
    "enrollment_id": 10,
    "student_id": 101,
    "course_id": 201
  }
]
```

<h3 id="post__api_student_{student_id}_course-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Enrollment successful|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Student not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="post__api_student_{student_id}_course-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» enrollment_id|integer|false|none|none|
|» student_id|integer|false|none|none|
|» course_id|integer|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_student_{student_id}_course_{course_id}

> Code samples

```shell
# You can also use wget
curl -X DELETE http://127.0.0.1:5000/api/student/{student_id}/course/{course_id} \
  -H 'Accept: application/json'

```

```http
DELETE http://127.0.0.1:5000/api/student/{student_id}/course/{course_id} HTTP/1.1
Host: 127.0.0.1:5000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:5000/api/student/{student_id}/course/{course_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete 'http://127.0.0.1:5000/api/student/{student_id}/course/{course_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('http://127.0.0.1:5000/api/student/{student_id}/course/{course_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://127.0.0.1:5000/api/student/{student_id}/course/{course_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:5000/api/student/{student_id}/course/{course_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://127.0.0.1:5000/api/student/{student_id}/course/{course_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/student/{student_id}/course/{course_id}`

URL to delete enrollment of the student in the course. This path belongs to the Enrollment table.

<h3 id="delete__api_student_{student_id}_course_{course_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|student_id|path|integer|true|none|
|course_id|path|integer|true|none|

> Example responses

> 400 Response

```json
{
  "error_code": "string",
  "error_message": "string"
}
```

<h3 id="delete__api_student_{student_id}_course_{course_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully deleted|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid Student Id or Course Id.|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Enrollment for the student not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="delete__api_student_{student_id}_course_{course_id}-responseschema">Response Schema</h3>

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error_code|string|false|none|none|
|» error_message|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

