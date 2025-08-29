// Function to read values from inputs and trigger the solver
function solveQuadraticFromInputs() {
  // Get values from the input fields
  let a = parseFloat(document.getElementById("a").value);
  let b = parseFloat(document.getElementById("b").value);
  let c = parseFloat(document.getElementById("c").value);

  // Check for valid numbers
  if (isNaN(a) || isNaN(b) || isNaN(c)) {
    document.getElementById("result").innerHTML = "Please enter valid numbers for all coefficients.";
    return;
  }

  // Call the main solver function with the user's input
  solveQuadratic(a, b, c);
}

// Function to solve a quadratic equation
function solveQuadratic(a, b, c) {
  // Input: Display the coefficients
  function displayCoefficients(a, b, c) {
    document.getElementById("result").innerHTML = `Solving the equation: ${a}x² + ${b}x + ${c} = 0`;
  }

  // Processing: Calculate the roots
  function calculateRoots(a, b, c) {
    let result = {};
    let discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
      let root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
      let root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
      result.message = "The roots are real and distinct.";
      result.root1 = root1.toFixed(2);
      result.root2 = root2.toFixed(2);
    } else if (discriminant === 0) {
      let root = -b / (2 * a);
      result.message = "The roots are real and equal.";
      result.root1 = root.toFixed(2);
      result.root2 = root.toFixed(2); // Same for both roots
    } else {
      let realPart = (-b / (2 * a)).toFixed(2);
      let imaginaryPart = (Math.sqrt(-discriminant) / (2 * a)).toFixed(2);
      result.message = "The roots are complex and distinct.";
      result.root1 = `${realPart} + ${imaginaryPart}i`;
      result.root2 = `${realPart} - ${imaginaryPart}i`;
    }
    return result;
  }

  // Output: Display the results
  function displayResults(roots) {
    document.getElementById("result").innerHTML += `<br>${roots.message}<br>Root 1: ${roots.root1}<br>Root 2: ${roots.root2}`;
  }

  // Main execution flow
  displayCoefficients(a, b, c);
  let roots = calculateRoots(a, b, c);
  displayResults(roots);
}
