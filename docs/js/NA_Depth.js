function calculateNeutralAxis() {
  let fy = parseFloat(document.getElementById("fy").value);
  let Ast = parseFloat(document.getElementById("Ast").value);
  let fck = parseFloat(document.getElementById("fck").value);
  let b = parseFloat(document.getElementById("b").value);

  if (isNaN(fy) || isNaN(Ast) || isNaN(fck) || isNaN(b) || fy <= 0 || Ast <= 0 || fck <= 0 || b <= 0) {
    document.getElementById("neutralAxisResult").innerHTML = "⚠️ Please enter valid positive values.";
    return;
  }

  let xu = (0.87 * fy * Ast) / (0.36 * fck * b);

  document.getElementById("neutralAxisResult").innerHTML =
    `Calculated Neutral Axis Depth (x<sub>u</sub>) = <b>${xu.toFixed(2)} mm</b>`;
}
