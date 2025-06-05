# pythonGUI

This repository contains a Tkinter application that displays weather
information from **weather.com** using their public API. The user selects
a location by clicking on a map.

## Usage

1. Obtain a weather.com API key and export it as `WEATHER_API_KEY`:
   ```bash
   export WEATHER_API_KEY=YOUR_KEY_HERE
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application
   ```bash
   python weather_gui.py
   ```

Click on a location on the map to fetch and display the current
conditions and temperature for that point. The map uses OpenStreetMap
tiles via `tkintermapview`.
