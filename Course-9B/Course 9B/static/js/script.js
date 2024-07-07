document.addEventListener('DOMContentLoaded', function () {
    function fetchAndDisplayIslandPlot(islandName) {
        fetch(`/api/plot_island/${islandName}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                } else {
                    const img = document.getElementById('islandPlot');
                    img.src = data.plot_url;
                }
            });
    }

    function fetchAndDisplayProvinceCategoriesPlot() {
        fetch(`/api/plot_province_categories`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                } else {
                    const img = document.getElementById('provinceCategoriesPlot');
                    img.src = data.plot_url;
                }
            });
    }

    function fetchAndDisplayProvinceCountsPlot() {
        fetch(`/api/plot_province_counts`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                } else {
                    const img = document.getElementById('provinceCountsPlot');
                    img.src = data.plot_url;
                }
            });
    }

    fetchAndDisplayProvinceCategoriesPlot();
    fetchAndDisplayProvinceCountsPlot();

    document.getElementById('jawaButton').addEventListener('click', () => fetchAndDisplayIslandPlot('Jawa'));
    document.getElementById('sumatraButton').addEventListener('click', () => fetchAndDisplayIslandPlot('Sumatra'));
    document.getElementById('kalimantanButton').addEventListener('click', () => fetchAndDisplayIslandPlot('Kalimantan'));
    document.getElementById('sulawesiButton').addEventListener('click', () => fetchAndDisplayIslandPlot('Sulawesi'));
    document.getElementById('malukuPapuaButton').addEventListener('click', () => fetchAndDisplayIslandPlot('Maluku_Papua'));
    document.getElementById('baliNusaTenggaraButton').addEventListener('click', () => fetchAndDisplayIslandPlot('Bali_Nusa_Tenggara'));
});
