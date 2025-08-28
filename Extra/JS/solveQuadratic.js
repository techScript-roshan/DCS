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
      result.root1 = root1;
      result.root2 = root2;
    } else if (discriminant === 0) {
      let root = -b / (2 * a);
      result.message = "The roots are real and equal.";
      result.root1 = root;
      result.root2 = root; // Same for both roots
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

// Ensure this script is linked in your Jekyll layout file, e.g., in _layouts/default.html
// <script src="/path/to/solver.js"></script>
