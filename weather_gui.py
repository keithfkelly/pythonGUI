import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


def fetch_weather(location_code: str) -> str:
    """Fetch the current temperature from weather.com given a location code.

    Parameters
    ----------
    location_code : str
        A location code recognized by weather.com (e.g., "USNY0996:1:US" for New York).

    Returns
    -------
    str
        A human-readable description of the current weather.
    """
    url = f"https://weather.com/weather/today/l/{location_code}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch weather data: {exc}") from exc

    soup = BeautifulSoup(response.text, "html.parser")

    temp_tag = soup.find(class_="CurrentConditions--tempValue--3KcTQ")
    desc_tag = soup.find(class_="CurrentConditions--phraseValue--2xXSr")

    if not temp_tag or not desc_tag:
        raise RuntimeError("Could not parse weather data from weather.com")

    temperature = temp_tag.text.strip()
    description = desc_tag.text.strip()

    return f"{description}, {temperature}"


def show_weather():
    loc = location_entry.get().strip()
    if not loc:
        messagebox.showwarning("Input required", "Please enter a location code")
        return

    try:
        result = fetch_weather(loc)
    except Exception as exc:
        messagebox.showerror("Error", str(exc))
        return

    weather_var.set(result)


# Build GUI
root = tk.Tk()
root.title("Weather.com Viewer")

frm = tk.Frame(root, padx=10, pady=10)
frm.pack()

location_label = tk.Label(frm, text="Location code:")
location_label.grid(row=0, column=0, sticky="w")

location_entry = tk.Entry(frm, width=20)
location_entry.grid(row=0, column=1, sticky="we", padx=(5, 0))
location_entry.insert(0, "USNY0996:1:US")

fetch_button = tk.Button(frm, text="Fetch Weather", command=show_weather)
fetch_button.grid(row=0, column=2, padx=(5, 0))

weather_var = tk.StringVar(value="Weather info will appear here")
weather_label = tk.Label(frm, textvariable=weather_var, wraplength=300)
weather_label.grid(row=1, column=0, columnspan=3, pady=(10, 0))

root.mainloop()
