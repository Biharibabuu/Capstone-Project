const apiPill = document.querySelector("#api-pill");
const modelPill = document.querySelector("#model-pill");
const healthMessage = document.querySelector("#health-message");
const modelState = document.querySelector("#model-state");
const modelDetail = document.querySelector("#model-detail");

function setPill(element, text, kind = "pending") {
  element.textContent = text;
  element.className = "pill pill-" + kind;
}

async function checkApiHealth() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/health", {
      headers: { Accept: "application/json" },
    });
    if (!response.ok) throw new Error("API returned HTTP " + response.status);
    const result = await response.json();

    setPill(apiPill, "API connected", "good");
    healthMessage.textContent = result.message || "API health check completed.";

    if (result.model_loaded && result.status === "ready") {
      setPill(modelPill, "Model artifact detected", "pending");
      modelState.textContent = "Artifact detected; not yet verified";
      modelDetail.textContent =
        "A file is present, but prediction must remain disabled until loading, preprocessing compatibility and evaluation status are verified.";
    } else {
      setPill(modelPill, "Model not trained", "pending");
      modelState.textContent = "Not trained";
      modelDetail.textContent =
        "Complete the data audit, baseline comparison, chronological evaluation and model packaging before enabling forecasts.";
    }
  } catch (error) {
    setPill(apiPill, "API unavailable", "error");
    setPill(modelPill, "Model status unknown", "pending");
    healthMessage.textContent =
      "Start the API with 'uvicorn backend.main:app --reload' from the repository root. " +
      "Details: " + error.message;
  }
}

checkApiHealth();
