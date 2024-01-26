"use strict";

async function getWeather(location) {
  try {
    const response = await fetch(
      `https://api.weatherapi.com/v1/current.json?key=da59594fa69049739a5180255242601&q=${location}`,
    );
    response.json().then(function (response) {
      console.log(response);
      const outputContainer = document.getElementById("output-container");

      while (outputContainer.childElementCount > 0) {
        console.log(outputContainer.childElementCount);
        outputContainer.removeChild(outputContainer.firstChild);
      }

      for (const [key, value] of Object.entries(response)) {
        console.log(key, value);
        for (const [innerKey, innerValue] of Object.entries(value)) {
          console.log(innerKey, innerValue);
          outputContainer.append(createTableRows(innerKey, innerValue));
        }
      }
    });
  } catch (err) {
    console.error(err);
  }
}

function getLocation() {
  const locationText = document.getElementById("location-text");
  const submitFormBtn = document.getElementById("submit-form-btn");

  submitFormBtn.addEventListener("click", (e) => {
    e.preventDefault();
    let location = locationText.value;
    console.log(location);
    getWeather(location);
  });
}

getLocation();

function createTableRows(textKey, textValue) {
  const tableRow = document.createElement("tr");
  tableRow.classList.add("table-row");
  tableRow.append(createTableData(textKey));
  tableRow.append(createTableData(textValue));
  return tableRow;
}

function createTableData(text) {
  const tableData = document.createElement("td");
  tableData.classList.add("table-data");
  tableData.textContent = text;
  return tableData;
}
