# RA Pain Predictor

RA Pain Predictor is a Flask web application that predicts the pain levels experienced by individuals with Rheumatoid Arthritis (RA) based on current weather conditions. This tool helps users understand how weather conditions may impact their pain levels and manage their symptoms more effectively.

## Features

- Predict RA pain levels based on current weather conditions.
- Real-time weather data fetched from WeatherAPI.
- Simple and user-friendly web interface.
- Configurable environment variables for secure API key management.

## Technologies Used

- Flask
- Python
- HTML/CSS
- JavaScript
- WeatherAPI
- Git/GitHub for version control

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/RA_Pain_Predictor.git
   cd RA_Pain_Predictor
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory of your project and add your WeatherAPI key:
     ```env
     WEATHER_API_KEY=your_actual_api_key
     ```

### Running the Application

1. **Start the Flask development server**:

   ```bash
   python app.py
   ```

2. **Open your browser and navigate to** `http://localhost:5000`.

### Usage

1. **Enter a location** in the input field.
2. **Click "Predict Pain Level"** to get the predicted RA pain level and current weather conditions.

## Contributing

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/your-feature-name`).
3. **Commit your changes** (`git commit -m 'Add some feature'`).
4. **Push to the branch** (`git push origin feature/your-feature-name`).
5. **Open a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [WeatherAPI](https://www.weatherapi.com/) for providing the weather data.
- Research studies on the impact of weather conditions on RA pain.
