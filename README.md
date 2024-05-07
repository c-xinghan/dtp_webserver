# A very simple Flask web server + HTML frontend
Facilitates temporary data storage and 2-way communication between two RPI units.

https://github.com/c-xinghan/dti_webserver/assets/23093512/9e4f3cd8-f5ea-4db3-b290-93e5561ffc40

## Background
For a [design course](https://www.sutd.edu.sg/Admissions/Undergraduate/Unique-Curriculum/Freshmore-Subjects/Design-Thinking-and-Innovation)'s project, we built two functional prototypes of our proposed product to serve as a proof-of-concept. 

Each prototype includes a Raspberry Pi running this web server, which enables both prototypes to communicate via calling each other's API endpoints.

The frontend was used for prototype showcase/presentation purposes and provides a visual representation of the data that is being stored on one prototype's web server and retrieved by the other prototype unit.

## Documentation

### Global variables
Used for temporary storage of data within the web server.
| Name | Type | Description |
| ------------- | ------------- | ------------- |
| `speed` | <code>*Float*</code> | Represents a user's speed in km/h. |
| `time` | <code>*Datetime*</code> | Represents a specific time. |

### REST APIs
| Endpoint | Method | Description | Parameter(s) | Returned value(s) |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| **/speed** | `GET` | Returns `speed` in <code>*String*</code> type | NIL | <code>*String* speed</code> | 
| **/updatespeed** | `POST` | Updates `speed` with the value within the request header. Returns a <code>*Response*</code> object for redirecting to the home page. | Request header:<br><code>{'speed': *Integer*}</code> | <code>*Response* redirect()</code> |
| **/time** | `GET` | Returns `time`, formatted to HHMM and in <code>*String*</code> type | NIL | <code>*String* time</code> |
| **/decreasetime** | `POST` | Rolls back `time` by 1 hour. Returns a <code>*Response*</code> object for redirecting to the home page. | NIL | <code>*Response* redirect()</code> |
| **/increasetime** | `POST` | Advances `time` by 1 hour. Returns a <code>*Response*</code> object for redirecting to the home page. | NIL | <code>*Response* redirect()</code> |
| **/decreasespeed** | `POST` | Decreases `speed` by 3. Returns a <code>*Response*</code> object for redirecting to the home page. | NIL | <code>*Response* redirect()</code> |
| **/increasespeed** | `POST` | Increases `speed` by 3. Returns a <code>*Response*</code> object for redirecting to the home page. | NIL | <code>*Response* redirect()</code> |
