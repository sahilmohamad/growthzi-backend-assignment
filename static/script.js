const API_BASE = "http://127.0.0.1:5000/api";

// Resume Upload
document.getElementById("resumeForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("resumeFile");
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch(`${API_BASE}/portfolio`, {
    method: "POST",
    body: formData
  });
  const data = await res.json();
  document.getElementById("resumeResult").textContent = JSON.stringify(data, null, 2);
});

// Translation
document.getElementById("translateForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = document.getElementById("translateText").value;
  const lang = document.getElementById("translateLang").value;

  const res = await fetch(`${API_BASE}/translate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, lang })
  });
  const data = await res.json();
  document.getElementById("translateResult").textContent = JSON.stringify(data, null, 2);
});

// Pricing
document.getElementById("pricingForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const country = document.getElementById("countryCode").value;

  const res = await fetch(`${API_BASE}/pricing?country=${country}`);
  const data = await res.json();
  document.getElementById("pricingResult").textContent = JSON.stringify(data, null, 2);
});
