![Alt text](https://github.com/xdityagr/Project-AirDex/blob/main/banner_airdex.png?raw=true "Banner Image")


# AirDex

AirDex is a beautiful and functional weather application that provides real-time weather updates, including temperature, humidity, pressure, and more. The app uses data from the OpenWeatherMap API and offers a user-friendly interface with a dynamic background that changes based on the time of day.

## Features

- **Real-Time Weather Updates:** Displays current weather conditions, including temperature, pressure, humidity, and visibility.
- **Dynamic Backgrounds:** The background color and images change based on the time of day (morning, afternoon, evening, night).
- **System Tray Integration:** Provides system tray functionality to minimize the app and keep it running in the background.
- **Customizable Interface:** Allows you to customize the app's appearance with various fonts and icons.

## Installation

1. **Download the Executable:**
   - Download `AirDex Home Edition.exe` from the [releases page](#).

2. **Run the Application:**
   - Double-click `AirDex Home Edition.exe` to start the application.

3. **Fonts and Assets:**
   - Ensure the following fonts and assets are included in the `assets/` directory:
     - Fonts: `Comfortaa-Light.ttf`, `Comfortaa-medium.ttf`, `Comfortaa-Regular.ttf`, `OpenSans-SemiBold.ttf`
     - Icons: `ic.ico`, `stateMorn.png`, `stateAfter.png`, `stateEve.png`, `stateNight.png`
     - Splash Screen: `icHome.png`

## Usage

- **Launching the App:**
  - When you start the application, a splash screen will appear, and then the main weather window will open.
  
- **System Tray Options:**
  - **Open:** Show the main application window.
  - **Minimize:** Minimize the application to the system tray.
  - **Keep app running in background:** Toggle whether the app continues to run in the background when closed.
  - **Exit:** Close the application.

## File Structure

- **HomeDataInit.py:** Contains the main logic for fetching and displaying weather data.
- **RunAir.py:** Manages the splash screen and application startup.
- **ui_main.py:** UI definitions for the main weather window.
- **ui_splash.py:** UI definitions for the splash screen.
- **ui_warningdialog.py:** UI definitions for the warning dialog.

## Configuration

- **API Key:**
  - Ensure you have a valid API key from OpenWeatherMap. Update the `WAPI` variable in `HomeDataInit.py` with your API key.

## Troubleshooting

- **No Connection:**
  - If you encounter issues with connectivity, ensure you have a stable internet connection and that the OpenWeatherMap API is accessible.

- **Application Not Starting:**
  - Check if all required fonts and assets are present in the `assets/` directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, please contact:

- **Email**: adityagaur.home@gmail.com
- **GitHub**: [xdityagr](https://github.com/xdityagr)
  
---

Enjoy using AirDex!
