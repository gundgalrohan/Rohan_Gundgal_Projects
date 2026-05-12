document.addEventListener("DOMContentLoaded", function () {
    const symptomInput = document.getElementById("symptomInput");
    const checkboxContainer = document.getElementById("checkboxContainer");
    const detectButton = document.getElementById("detectButton");
    const resultsDiv = document.getElementById("results");
    const dropdownButton = document.getElementById("dropdownButton");
    const dropdownContent = document.getElementById("dropdownContent");

    let symptomsData = {};
    let precautionData = {};
    let allSymptoms = new Set();
    let selectedSymptoms = new Set();

    // Load symptoms data
    fetch("symptoms_data.json")
        .then((response) => response.json())
        .then((data) => {
            symptomsData = data;

            // Collect all unique symptoms
            Object.values(symptomsData).forEach((disorder) => {
                disorder.symptoms.forEach((symptom) => allSymptoms.add(symptom));
            });

            displaySymptomsTable(Array.from(allSymptoms));

            symptomInput.addEventListener("input", filterSymptoms);
        })
        .catch((error) => {
            console.error("Error loading symptoms data:", error);
        });

    // Load precaution and care data
    fetch("precaution_data.json")
        .then((response) => response.json())
        .then((data) => {
            precautionData = data;
        })
        .catch((error) => {
            console.error("Error loading precaution data:", error);
        });

    function filterSymptoms() {
        const searchQuery = symptomInput.value.toLowerCase();
        const filteredSymptoms = Array.from(allSymptoms).filter((symptom) =>
            symptom.toLowerCase().includes(searchQuery)
        );

        if (filteredSymptoms.length > 0) {
            dropdownContent.style.display = "block";
        } else {
            dropdownContent.style.display = "none";
        }

        displaySymptomsTable(filteredSymptoms);
    }

    function capitalizeFirstLetter(symptom) {
        return symptom.charAt(0).toUpperCase() + symptom.slice(1).toLowerCase();
    }

    function displaySymptomsTable(symptoms) {
        checkboxContainer.innerHTML = '';
        const maxRows = 10;
        const totalColumns = 5;

        for (let i = 0; i < maxRows; i++) {
            const row = document.createElement("tr");

            for (let j = 0; j < totalColumns; j++) {
                const cell = document.createElement("td");
                const symptomIndex = i * totalColumns + j;

                if (symptomIndex < symptoms.length) {
                    const symptom = symptoms[symptomIndex];
                    cell.innerHTML = ` 
                        <label>
                          <input type="checkbox" name="symptoms" value="${symptom}" 
                                 ${selectedSymptoms.has(symptom) ? 'checked' : ''}> ${capitalizeFirstLetter(symptom)}
                        </label>
                    `;

                    cell.querySelector('input').addEventListener('change', function () {
                        if (this.checked) {
                            selectedSymptoms.add(symptom);
                        } else {
                            selectedSymptoms.delete(symptom);
                        }
                    });
                }

                row.appendChild(cell);
            }
            checkboxContainer.appendChild(row);
        }
    }

    function detectDisorder() {
        if (selectedSymptoms.size === 0) {
            alert("Please select at least one symptom.");
            return;
        }

        const matches = {};

        // Check all disorders against selected symptoms
        for (const disorder in symptomsData) {
            const disorderSymptoms = symptomsData[disorder].symptoms;
            let matchCount = 0;

            selectedSymptoms.forEach((userSymptom) => {
                if (disorderSymptoms.includes(userSymptom)) {
                    matchCount++;
                }
            });

            const percentage = (matchCount / disorderSymptoms.length) * 100;
            if (percentage > 0) {
                matches[disorder] = percentage;
            }
        }

        const sortedMatches = Object.entries(matches).sort((a, b) => b[1] - a[1]);

        if (sortedMatches.length > 0) {
            const topDisease = sortedMatches[0][0];
            const matchListHTML = sortedMatches
                .map(([disorder, percent]) => `<li>${disorder} — ${percent.toFixed(2)}%</li>`)
                .join("");

            let precautionHTML = "";
            if (precautionData[topDisease]) {
                const precautionList = precautionData[topDisease].precautions
                    .map((item) => `<li>${item}</li>`).join("");
                const careList = precautionData[topDisease].care
                    .map((item) => `<li>${item}</li>`).join("");

                precautionHTML = ` 
                    <div id="precautionCare">
                        <h3>Precaution for <em>${topDisease}</em>:</h3>
                        <ul>${precautionList}</ul>
                        <h3>Care Tips for <em>${topDisease}</em>:</h3>
                        <ul>${careList}</ul>
                    </div>
                `;
            }

            resultsDiv.innerHTML = `
                <h2>Possible Matches:</h2>
                <ul>${matchListHTML}</ul>
                ${precautionHTML}
            `;
        } else {
            resultsDiv.innerHTML = "<p class='no-matches'>No matches found.</p>";
        }
    }

    detectButton.addEventListener("click", detectDisorder);

    dropdownButton.addEventListener("click", function () {
        dropdownContent.style.display = dropdownContent.style.display === "block" ? "none" : "block";
    });

    window.addEventListener("click", function (event) {
        if (!event.target.matches('.dropdown-button') && !event.target.closest('.dropdown-content')) {
            dropdownContent.style.display = "none";
        }
    });
});