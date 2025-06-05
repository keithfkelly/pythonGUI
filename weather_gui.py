import os
import tkinter as tk
from tkinter import messagebox

import requests
from tkintermapview import TkinterMapView


API_KEY = os.environ.get("WEATHER_API_KEY")


def fetch_weather(lat: float, lon: float) -> str:
    """Fetch current weather from weather.com API using latitude/longitude."""
    if not API_KEY:
        raise RuntimeError("WEATHER_API_KEY environment variable not set")

    url = "https://api.weather.com/v3/wx/conditions/current"
    params = {
        "geocode": f"{lat},{lon}",
        "format": "json",
        "language": "en-US",
        "apiKey": API_KEY,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch weather data: {exc}") from exc

    data = response.json()
    temperature = data.get("temperature")
    description = data.get("narrative") or data.get("wxPhraseLong")

    if temperature is None or description is None:
        raise RuntimeError("Unexpected response from weather API")

    return f"{description}, {temperature}°"


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Map Viewer")
        self.geometry("800x650")

        self.map_widget = TkinterMapView(self, width=800, height=600)
        self.map_widget.pack(fill="both", expand=True)
        self.map_widget.add_left_click_map_command(self.on_map_click)

        self.selected_marker = None
        self.weather_var = tk.StringVar(value="Click on the map to select a location.")
        label = tk.Label(self, textvariable=self.weather_var, wraplength=780)
        label.pack(pady=5)

    def on_map_click(self, coords):
        lat, lon = coords
        if self.selected_marker:
            self.map_widget.delete(self.selected_marker)
        self.selected_marker = self.map_widget.set_marker(lat, lon)
        try:
            weather = fetch_weather(lat, lon)
        except Exception as exc:
            messagebox.showerror("Error", str(exc))
            return
        self.weather_var.set(f"Weather at {lat:.4f}, {lon:.4f}: {weather}")


def main():
    app = WeatherApp()
    app.mainloop()


if __name__ == "__main__":
    main()
