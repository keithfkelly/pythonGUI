# pythonGUI

This repository now includes a simple Tkinter application that fetches weather
information from **OpenWeatherMap**. The GUI allows you to type a city name or
location and displays the current condition and temperature in Celsius. The
script uses the API key `748d6ed0cb9c0c3bc8d3cdadb904af2b` which is embedded in
the code for convenience.

## Usage

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application
   ```bash
   python weather_gui.py
   ```

The program queries the OpenWeatherMap API for the current conditions. If the
API call fails (for example due to network settings), an error dialog will be
displayed.
