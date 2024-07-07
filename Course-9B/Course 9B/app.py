from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Baca file Excel
file_path = 'data/waste_data.xlsx'
df = pd.read_excel(file_path, header=1)  # Mengatur header pada baris ke-2 (indeks 1)

df = df[df['Provinsi'] != 'Papua Pegunungan']

# Update the year for "Papua Barat" from 2018 to 2019
df.loc[(df['Provinsi'] == 'Papua Barat') & (df['Tahun'] == 2018), 'Tahun'] = 2019

# Fill the missing 2019 data for "Nusa Tenggara Timur" with the average of 2020-2023
average_ntt = df[(df['Provinsi'] == 'Nusa Tenggara Timur') & (df['Tahun'].between(2020, 2023))]['Timbulan Sampah Tahunan(ton)'].mean()
if not ((df['Provinsi'] == 'Nusa Tenggara Timur') & (df['Tahun'] == 2019)).any():
    new_row = {'Provinsi': 'Nusa Tenggara Timur', 'Tahun': 2019, 'Timbulan Sampah Tahunan(ton)': average_ntt}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Fill the missing 2019 and 2020 data for "Papua Tengah"
average_papuatengah = df[(df['Provinsi'] == 'Papua Tengah') & (df['Tahun'].between(2021, 2023))]['Timbulan Sampah Tahunan(ton)'].mean()
if not ((df['Provinsi'] == 'Papua Tengah') & (df['Tahun'] == 2019)).any():
    new_row1 = {'Provinsi': 'Papua Tengah', 'Tahun': 2019, 'Timbulan Sampah Tahunan(ton)': average_papuatengah}
    df = pd.concat([df, pd.DataFrame([new_row1])], ignore_index=True)
if not ((df['Provinsi'] == 'Papua Tengah') & (df['Tahun'] == 2020)).any():
    new_row2 = {'Provinsi': 'Papua Tengah', 'Tahun': 2020, 'Timbulan Sampah Tahunan(ton)': average_papuatengah}
    df = pd.concat([df, pd.DataFrame([new_row2])], ignore_index=True)

avg_annual_waste = df.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()

# Function to categorize provinces
def categorize_province(avg_waste):
    if avg_waste <= 100000:
        return 'GREEN'
    elif avg_waste <= 700000:
        return 'ORANGE'
    else:
        return 'RED'

avg_annual_waste['Category'] = avg_annual_waste['Timbulan Sampah Tahunan(ton)'].apply(categorize_province)

# Define provinces by island
islands = {
    'Jawa': ['Banten', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'D.I. Yogyakarta', 'Jawa Timur'],
    'Sumatra': ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi', 'Sumatera Selatan', 'Bengkulu', 'Lampung', 'Kepulauan Bangka Belitung', 'Kepulauan Riau'],
    'Kalimantan': ['Kalimantan Barat', 'Kalimantan Tengah', 'Kalimantan Selatan', 'Kalimantan Timur', 'Kalimantan Utara'],
    'Sulawesi': ['Sulawesi Utara', 'Gorontalo', 'Sulawesi Tengah', 'Sulawesi Selatan', 'Sulawesi Tenggara', 'Sulawesi Barat'],
    'Maluku_Papua': ['Papua', 'Papua Barat', 'Papua Barat Daya', 'Papua Selatan', 'Papua Pegunungan', 'Maluku', 'Maluku Utara', 'Papua Tengah'],
    'Bali_Nusa_Tenggara': ['Bali', 'Nusa Tenggara Barat', 'Nusa Tenggara Timur'],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/plot_island/<island_name>')
def plot_island(island_name):
    provinces = islands.get(island_name)
    if not provinces:
        return jsonify({"error": "Invalid island name"}), 400

    filtered_data = df[df['Provinsi'].isin(provinces)]
    grouped_data = filtered_data.groupby(['Tahun', 'Provinsi'])['Timbulan Sampah Tahunan(ton)'].sum().unstack()

    plt.figure(figsize=(14, 8))
    grouped_data.plot(kind='line', marker='o')
    plt.title(f'Total Annual Amount of Waste in {island_name}')
    plt.xlabel('Tahun')
    plt.ylabel('Timbulan Sampah Tahunan(ton)')
    plt.legend(title='Provinsi', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({"plot_url": f"data:image/png;base64,{plot_url}"})

@app.route('/api/plot_province_categories')
def plot_province_categories():
    fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(12, 12), gridspec_kw={'height_ratios': [3, 1]})

    colors = {'GREEN': 'green', 'ORANGE': 'orange', 'RED': 'red'}
    sns.barplot(x='Provinsi', y='Timbulan Sampah Tahunan(ton)', data=avg_annual_waste, palette=colors.values(), hue='Category', ax=ax1)
    ax1.set_title('Kategori Timbulan Sampah Tahunan per Provinsi')
    ax1.set_xlabel('Provinsi')
    ax1.set_ylabel('Rata-Rata Timbulan Sampah Tahunan (ton)')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    ax1.legend(title='Category', loc='upper right')

    province_counts = avg_annual_waste['Category'].value_counts().reindex(['GREEN', 'ORANGE', 'RED'], fill_value=0)
    ax2.bar(province_counts.index, province_counts.values, color=['green', 'orange', 'red'])
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Number of Provinces')
    ax2.set_title('Number of Provinces by Waste Category')
    ax2.grid(True)

    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({"plot_url": f"data:image/png;base64,{plot_url}"})

@app.route('/api/plot_province_counts')
def plot_province_counts():
    province_counts = avg_annual_waste['Category'].value_counts().reindex(['GREEN', 'ORANGE', 'RED'], fill_value=0)

    plt.figure(figsize=(8, 6))
    plt.bar(province_counts.index, province_counts.values, color=['green', 'orange', 'red'])
    plt.xlabel('Category')
    plt.ylabel('Number of Provinces')
    plt.title('Number of Provinces by Waste Category')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({"plot_url": f"data:image/png;base64,{plot_url}"})

if __name__ == '__main__':
    app.run(debug=True)
