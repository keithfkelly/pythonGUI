# pythonGUI

This repository now includes a simple Tkinter application that fetches weather
information from **weather.com** for a provided location code. The GUI allows
you to type a location code such as `USNY0996:1:US` and displays the current
condition and temperature as reported on the site.

## Usage

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application
   ```bash
   python weather_gui.py
   ```

The program attempts to fetch the HTML from weather.com and parse it for the
current conditions and temperature. Depending on your network settings or the
site's restrictions, this may fail with an error.
