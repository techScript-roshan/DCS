function calculateCircle() {
  let r = parseFloat(document.getElementById("radius").value);

  if (isNaN(r) || r <= 0) {
    document.getElementById("circleResult").innerHTML = "⚠️ Please enter a valid positive radius.";
    return;
  }

  let area = Math.PI * r * r;
  let circumference = 2 * Math.PI * r;

  document.getElementById("circleResult").innerHTML =
    `For radius r = ${r}:<br>` +
    `Area = ${area.toFixed(2)} mm²<br>` +
    `Circumference = ${circumference.toFixed(2)} mm`;
}
