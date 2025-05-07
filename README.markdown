# Diamond Price Prediction

This project predicts diamond prices using a LightGBM model trained on a dataset of 6,000 diamonds, inspired by the "Diamond for Sarah" case study from Darden Business Publishing. It includes a Flask web application to display the top *n* undervalued high-quality diamonds based on predicted prices, helping users identify cost-effective, high-quality diamonds for purchases like engagement rings.

## Table of Contents
- [Project Background](#project-background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Background
This project is inspired by the "Diamond for Sarah" case study, where Greg, an MBA student, seeks to purchase an ideal diamond for his fiancée Sarah’s engagement ring. After struggling to find a perfect ring setting, Greg decides to buy a loose diamond and design a custom setting with Sarah post-proposal. To optimize his purchase, he analyzes a dataset of 6,000 diamonds to build a predictive model that identifies high-quality diamonds priced below their estimated value. The dataset includes features like carat weight, cut, color, clarity, polish, symmetry, and certification (GIA or AGSL). This project replicates Greg’s approach, using machine learning to predict diamond prices and a Flask app to present undervalued diamonds meeting specific quality criteria.

## Features
- Data cleaning and feature engineering (e.g., encoding categorical variables, creating interaction terms like `Carat_Clarity`).
- Hyperparameter tuning with Optuna for the LightGBM model.
- Flask web app to display the top *n* undervalued high-quality diamonds based on user input.
- Visualizations of feature importance and data distributions in the Jupyter notebook.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diamond-price-prediction.git
   cd diamond-price-prediction
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the dataset and model files:
   - [diamonds.csv](link-to-dataset) → Place in `data/`
   - [diamond_price_model_boxcox.pkl](link-to-model) → Place in `models/`
   - [boxcox_lambda.pkl](link-to-lambda) → Place in `models/`

## Usage
1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000/`.
3. Enter the number of top undervalued diamonds to display.

To explore the data and model training, open `notebooks/notebook.ipynb` in Jupyter Notebook:
```bash
jupyter notebook
```

## Data
The dataset (`diamonds.csv`) contains 6,000 diamonds with the following features:
- **Carat Weight**: Weight of the diamond (e.g., 0.83 to 2.19 carats).
- **Cut**: Quality of the cut (Poor, Fair, Good, Very Good, Ideal, Signature-Ideal).
- **Color**: Color grade (D to I, with D being colorless).
- **Clarity**: Clarity grade (I1 to FL, with FL being flawless).
- **Polish**: Polish quality (Good, Very Good, Excellent, Ideal).
- **Symmetry**: Symmetry quality (Good, Very Good, Excellent, Ideal).
- **Report**: Certification body (GIA or AGSL).
- **Price**: Actual price (e.g., $3,171 to $30,507).

The processed dataset with predictions is saved as `diamonds_with_predictions.csv` in the `data/` directory.

## Model
- **Algorithm**: LightGBM with Box-Cox transformation for price normalization.
- **Features**: Engineered features like `Carat_Clarity`, `Log_Carat_Weight`, and encoded categorical variables.
- **Performance**:
  - Test RMSE: 1250.17
  - Test MAE: 640.56
  - Test R²: 0.9859

The model is saved as `diamond_price_model_boxcox.pkl`, and the Box-Cox lambda parameter is saved as `boxcox_lambda.pkl` in the `models/` directory.

## Results
The Flask app identifies high-quality undervalued diamonds based on the following criteria:
- **Cut**: Ideal or Signature-Ideal
- **Color**: D, E, or F
- **Clarity**: VS1, VVS2, VVS1, IF, or FL
- **Polish/Symmetry**: Excellent or Ideal
- **Price Difference**: Predicted Price > Actual Price

Example output:
```
Top 20 Undervalued High-Quality Diamonds:
Carat Weight  Cut    Color  Clarity  Report  Price    Price_Difference
2.11          Ideal  D      VVS2     GIA     43770.0  6374.91
...
```

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: The project background is inspired by the "Diamond for Sarah" case study (UV0869) by Darden Business Publishing, used for educational purposes.