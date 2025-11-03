async function checkInteractions() {
  const prescriptions = document.getElementById("prescriptions").value.split(",");
  const supplements = document.getElementById("supplements").value.split(",");
  const response = await fetch("http://localhost:5000/interactions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      prescriptions: prescriptions.map(s => s.trim()),
      supplements: supplements.map(s => s.trim())
    })
  });
  const data = await response.json();
  document.getElementById("results").innerText = JSON.stringify(data, null, 2);
}
