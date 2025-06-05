import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "748d6ed0cb9c0c3bc8d3cdadb904af2b"


def fetch_weather(location: str) -> str:
    """Fetch the current weather from OpenWeatherMap for a city or location.

    Parameters
    ----------
    location : str
        City name or location code understood by OpenWeatherMap.
    Returns
    -------
    str
        A human-readable description of the current weather in Celsius.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch weather data: {exc}") from exc

    data = response.json()
    if "weather" not in data or "main" not in data:
        raise RuntimeError("Unexpected response structure from OpenWeatherMap")

    description = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]

    return f"{description}, {temperature:.1f} \N{DEGREE SIGN}C"


def show_weather():
    loc = location_entry.get().strip()
    if not loc:
        messagebox.showwarning("Input required", "Please enter a location")
        return

    try:
        result = fetch_weather(loc)
    except Exception as exc:
        messagebox.showerror("Error", str(exc))
        return

    weather_var.set(result)


# Build GUI
root = tk.Tk()
root.title("OpenWeatherMap Viewer")

frm = tk.Frame(root, padx=10, pady=10)
frm.pack()

location_label = tk.Label(frm, text="Location:")
location_label.grid(row=0, column=0, sticky="w")

location_entry = tk.Entry(frm, width=20)
location_entry.grid(row=0, column=1, sticky="we", padx=(5, 0))
location_entry.insert(0, "London")

fetch_button = tk.Button(frm, text="Fetch Weather", command=show_weather)
fetch_button.grid(row=0, column=2, padx=(5, 0))

weather_var = tk.StringVar(value="Weather info will appear here")
weather_label = tk.Label(frm, textvariable=weather_var, wraplength=300)
weather_label.grid(row=1, column=0, columnspan=3, pady=(10, 0))

root.mainloop()
