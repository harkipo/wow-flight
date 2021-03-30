# wow-flight
A flight search app that finds all the possible flights between two destinations.


## Installation
  Clone the repository
  # Backend
    1. go to project directory and go to backend folder
    2. run `pip install -r requirements.txt`
    3. run `python manage.py migrate`
    4. run `python manage.py runserver`
  # Frontend
    1. Go to Frontend folder
    2. run `npm install` (install 'npm' if not installed)
    3. run `npm install --save axios`
    4. run `npm start`
    5. Open `http://localhost:3000/`

## API endpoints
  Postman collection is added for reference in the backend folder
  # Important API's (refer postman collection for other api's)
    1. Create flight
        url : http://127.0.0.1:8000/create-flight/
        method : POST
        payload={
                'number': 'SSG-15',
                'departure_city': 'Delhi',
                'departure_time': '1617177600000',
                'arrival_city': 'Jaipur',
                'arrival_time': '1617188400000'
                }
     2. Search Flight
        url : http://127.0.0.1:8000/search-flight/
        method : POST
        payload : {
                    'departure_city': 'Delhi',
                    'arrival_city': 'Jaipur',
                    'departure_time': '1617177400000'
                    }
