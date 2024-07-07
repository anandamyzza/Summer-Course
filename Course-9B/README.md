# Waste Generation Data Visualization in Indonesia

This project utilizes Flask to create visualizations of waste generation data in Indonesia based on province and category. The data used is sourced from the [National Waste Management Information System (SIPS) of the Ministry of Environment and Forestry](https://sipsn.menlhk.go.id/sipsn/public/data/timbulan) and is stored in waste_data.xlsx.

## Project Description

This project leverages Flask as a web framework to present data visualizations in the form of graphs using Matplotlib and Seaborn. It includes several key features:

- **Island-Based Visualization**: Users can select an island (Java, Sumatra, Kalimantan, Sulawesi, Maluku & Papua, Bali & Nusa Tenggara) to view graphs showing the annual waste generation from provinces within that island.
- **Waste Category Graphs**: These graphs depict the categorization of provinces based on average annual waste generation, color-coded by category (Green, Orange, Red).
- **Province Count per Category**: This graph illustrates the number of provinces falling into each waste category (Green, Orange, Red).

## Setup

To run this project locally, follow these steps:

1. **Install Dependencies**:
   Ensure Python and pip are installed. Then, install all required dependencies by running the following command in your terminal:

2. **Run Flask Application**:
Launch the Flask application by executing the following command in your terminal:

The application will run at `http://127.0.0.1:5000/`.

3. **Access the Application**:
Open your web browser and navigate to http://127.0.0.1:5000/ to view the data visualizations.

## Project Structure

- `app.py`: The main Flask file containing application definitions and API routes.
- `data/waste_data.xlsx`: Excel file containing waste generation data per province and year.
- `templates/index.html`: HTML template for the main application view.
- `static/js/script.js`: JavaScript file to handle requests and display charts.

## Google Colab

You can access the Google Colab notebook used for data analysis and initial data preparation [here](https://colab.research.google.com/drive/1tfkHJZSyuctcJet-qifhphA6F3sZiqw0?usp=sharing).

## Preview Video of the flask-based web

https://github.com/anandamyzza/Summer-Course/assets/147605722/a3593791-68ca-4c77-96ca-a2ffda8d4e6e

