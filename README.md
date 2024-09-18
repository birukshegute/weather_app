# Weather App
This weather web app was built as part of the ALX Software Engineering program, specifically for the backend specialization portfolio project. The app allows users to search for current and future weather conditions in any city worldwide. It integrates data from the OpenWeather API to deliver up-to-date weather details, including current weather and a 3-day forecast.

## Features
1) Search by City and Country: Users can search for real-time weather conditions by entering a city and country name.
2) Current Weather Information: Displays current temperature, weather description, and icon, along with high and low temperatures for the day.
3) 3-Day Forecast: Provides maximum and minimum temperature forecasts for the next three days.
4) Responsive Design: The app adjusts to different screen sizes, ensuring a smooth experience on mobile, tablet, and desktop.

## Technologies Used
### Backend:
Flask: A lightweight Python web framework used to build the server-side functionality of the app, handle form requests, and integrate with the OpenWeather API.
OpenWeather API: The app retrieves real-time weather data and forecasts using this API. This includes geocoding to convert city names into geographic coordinates, and weather data retrieval based on those coordinates.
### Frontend:
Tailwind CSS: A utility-first CSS framework used to design the front end of the app. It provides flexibility in styling the search form, weather cards, and overall layout.
HTML5: Used to structure the web pages.
Jinja2 Templating: Flask’s templating engine, used to dynamically display weather data fetched from the backend on the web page.

## External Resources:
Pixabay: Free background images were sourced from Pixabay.com, ensuring an aesthetic and professional design.
OpenWeather API: Provides the weather data, including current conditions and a 3-day forecast for any city in the world.

## How to Use the App

### Search for a City:

Enter the city name in the first text box.
Enter the country name (or code) in the second text box. Both fields are required.
Click on the "Show Weather" button to display the weather.

### View the Results:

After submitting the form, the app will display:
1) Current Weather: Including the temperature, weather description, and an icon representing the weather (e.g., clouds, rain, sunshine).
2) Today’s High and Low: The maximum and minimum temperatures expected for the day.
3) 3-Day Forecast: Displayed below the current weather, this section shows the high and low temperatures for the next three days. Each day is labeled with the month and day.
If a city is not found or an invalid city/country combination is entered, a formal and friendly error message will appear.

### Responsive Design:

The app is designed to work on both mobile and desktop devices. The layout adjusts accordingly for an optimal viewing experience on any screen size.

## Credits
Weather Data: This app uses the OpenWeather API to retrieve weather data.
Background Image: The background image was sourced from Pixabay.com, a repository of high-quality, free-to-use images.
Project Developer: This app was built by Biruk Shegute as part of the ALX Software Engineering program, specifically for the Backend Specialization Webstack Portfolio project.
