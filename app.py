from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset with predictions
df = pd.read_csv('diamonds_with_predictions.csv')
df['ID'] = df.index  # Returns the ID column to find the needed diamond

# Define high-quality criteria
high_quality_criteria = {
    'Cut': ['Ideal', 'Signature-Ideal'],
    'Color': ['D', 'E', 'F'],
    'Clarity': ['VS1', 'VVS2', 'VVS1', 'IF', 'FL'],
    'Polish': ['EX','ID'],
    'Symmetry': ['EX','ID']
}

# Filter for high-quality diamonds
high_quality_df = df[
    (df['Cut'].isin(high_quality_criteria['Cut'])) &
    (df['Color'].isin(high_quality_criteria['Color'])) &
    (df['Clarity'].isin(high_quality_criteria['Clarity'])) &
    (df['Polish'].isin(high_quality_criteria['Polish'])) &
    (df['Symmetry'].isin(high_quality_criteria['Symmetry'])) &
    (df['Price_Difference'] > 0)  # Only include undervalued diamonds
]

print(f"Number of high-quality undervalued diamonds: {len(high_quality_df)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    top_diamonds = None
    error = None

    if request.method == 'POST':
        try:
            # Get user input
            n = int(request.form['n'])
            if n <= 0:
                error = "Please enter a positive integer."
                return render_template('index.html', top_diamonds=None, error=error)

            # Sort high-quality diamonds by Price_Difference (most undervalued first)
            sorted_df = high_quality_df.sort_values(by=['Price_Difference', 'Price', 'Carat Weight'], ascending=[False, False, False])
                                                        

            # Take the top n diamonds
            top_n_df = sorted_df.head(n)

            # Format Price_Difference as a string with 2 decimal places
            top_n_df['Price_Difference'] = top_n_df['Price_Difference'].apply(lambda x: f"{x:.2f}")

            # Convert to dictionary for rendering in HTML
            top_diamonds = top_n_df[[
                'Carat Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report',
                'Price', 'Predicted_Price', 'Price_Difference'
            ]].to_dict('records')

            # If no diamonds are found, set an error message
            if not top_diamonds:
                error = "No high-quality undervalued diamonds found in the dataset."

        except ValueError:
            error = "Please enter a valid integer."
            return render_template('index.html', top_diamonds=None, error=error)
        except Exception as e:
            error = f"An error occurred: {str(e)}"
            return render_template('index.html', top_diamonds=None, error=error)

    return render_template('index.html', top_diamonds=top_diamonds, error=error)

if __name__ == '__main__':
    app.run(debug=True)