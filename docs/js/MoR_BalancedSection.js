function calculateMoR() {
  const fck = parseFloat(document.getElementById("fck").value);
  const b = parseFloat(document.getElementById("b").value);
  const d = parseFloat(document.getElementById("d").value);
  const fy = parseFloat(document.getElementById("fy").value);

  if (isNaN(fck) || isNaN(b) || isNaN(d) || isNaN(fy)) {
    document.getElementById("result").innerHTML = "<p style='color:red'>Please enter all values</p>";
    return;
  }

  // xu,max / d ratio
  let ratio;
  if (fy === 250) ratio = 0.53;
  else if (fy === 415) ratio = 0.48;
  else if (fy === 500) ratio = 0.46;

  const xu_max = ratio * d;

  // Formula: Mu,lim = 0.36 fck b xu,max (d - 0.42 xu,max)
  let Mor = 0.36 * fck * b * xu_max * (d - 0.42 * xu_max);

  // Convert to kN-m (since N-mm → divide by 10^6)
  Mor = Mor / 1e6;

  document.getElementById("result").innerHTML =
    `<p><b>Limiting Neutral Axis Depth (xu,max):</b> ${xu_max.toFixed(2)} mm</p>
     <p><b>Moment of Resistance (MoR):</b> ${Mor.toFixed(2)} kN-m</p>`;
}
