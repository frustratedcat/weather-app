"use strict";

async function getWeather(location) {
  try {
    const response = await fetch(
      `https://api.weatherapi.com/v1/current.json?key=da59594fa69049739a5180255242601&q=${location}`,
    );
    response.json().then(function (response) {
      const outputContainer = document.getElementById("output-container");

      while (outputContainer.childElementCount > 0) {
        outputContainer.removeChild(outputContainer.firstChild);
      }

      for (const [key, value] of Object.entries(response)) {
        for (const [innerKey, innerValue] of Object.entries(value)) {
          if (innerKey === "condition") {
            for (const [conditionKey, conditionValue] of Object.entries(
              innerValue,
            )) {
              if (conditionKey === "text") {
                console.log(conditionValue);
              }
            }
          }
          outputContainer.append(createTableRows(innerKey, innerValue));
        }
      }
      cleanUpData();
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

function cleanUpData() {
  const outputContainer = document.getElementById("output-container");
  let outputContainerChildren = outputContainer.children;
  console.log(outputContainerChildren.length);
  for (let i = 0; i < outputContainerChildren.length; i++) {
    if (outputContainerChildren[i].firstChild.textContent === "name") {
      outputContainerChildren[i].firstChild.textContent = "Name";
    } else if (outputContainerChildren[i].firstChild.textContent === "region") {
      outputContainerChildren[i].firstChild.textContent = "Region";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "country"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Country";
    } else if (outputContainerChildren[i].firstChild.textContent === "lat") {
      outputContainerChildren[i].firstChild.textContent = "Latitude";
    } else if (outputContainerChildren[i].firstChild.textContent === "lon") {
      outputContainerChildren[i].firstChild.textContent = "Longitude";
    } else if (outputContainerChildren[i].firstChild.textContent === "tz_id") {
      outputContainerChildren[i].firstChild.textContent = "Time Zone";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "localtime_epoch"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Local Time Epoch";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "localtime"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Local Time";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "last_updated_epoch"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Last Updated Epoch";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "last_updated"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Last Updated";
    } else if (outputContainerChildren[i].firstChild.textContent === "temp_c") {
      outputContainerChildren[i].firstChild.textContent = "Temperature Celsius";
    } else if (outputContainerChildren[i].firstChild.textContent === "temp_f") {
      outputContainerChildren[i].firstChild.textContent =
        "Temperature Fahrenheit";
    } else if (outputContainerChildren[i].firstChild.textContent === "is_day") {
      outputContainerChildren[i].firstChild.textContent = "Is Day";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "condition"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Condition";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "wind_mph"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Wind MPH";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "wind_kph"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Wind KPH";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "wind_degree"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Wind Degree";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "wind_dir"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Wind Direction";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "pressure_mb"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Pressure mb";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "pressure_in"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Pressure in";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "precip_mm"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Precip mm";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "precip_in"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Precip in";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "humidity"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Humidity";
    } else if (outputContainerChildren[i].firstChild.textContent === "cloud") {
      outputContainerChildren[i].firstChild.textContent = "Cloud";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "feelslike_c"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Feels Like Celsius";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "feelslike_f"
    ) {
      outputContainerChildren[i].firstChild.textContent =
        "Feels Like Fahrenheit";
    } else if (outputContainerChildren[i].firstChild.textContent === "vis_km") {
      outputContainerChildren[i].firstChild.textContent = "Vision km";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "vis_miles"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Vision miles";
    } else if (outputContainerChildren[i].firstChild.textContent === "uv") {
      outputContainerChildren[i].firstChild.textContent = "UV Index";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "gust_mph"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Gust MPH";
    } else if (
      outputContainerChildren[i].firstChild.textContent === "gust_kph"
    ) {
      outputContainerChildren[i].firstChild.textContent = "Gust KPH";
    }
  }
}
