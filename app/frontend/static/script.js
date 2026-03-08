"use strict";


async function showApi() {
  const output = document.getElementById("output")
  try {
    const response = await fetch("http://127.0.0.1:8000/api/all_cubes")
    if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`)
    const data = await response.json()
    output.textContent = JSON.stringify(data, null, 2)
    console.log("API-Antwort:", JSON.stringify(data, null, 2))
  } catch (err) {
    output.textContent = "Fehler: " + err.message
    console.error("Fetch-Fehler:", err)
  }
}





