<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
    
<script type="text/javascript"
        src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

# Design of Two-Way Slabs Using Moment Coefficient Method (IS 456:2000)

## Introduction
Two-way slabs are slabs supported on all four edges where bending occurs in both directions (longitudinal and transverse). This contrasts with one-way slabs supported on two opposite edges, bending primarily in one direction.

Two-way slabs are common in building floors and roofs where load distribution occurs in two directions due to similar support conditions on all edges. Design of two-way slabs includes determining moments in both directions using moment coefficients from IS 456:2000 Table 26 and designing reinforcement accordingly.

***

## Fundamental Concepts

- **Slab:** A structural element with thickness small compared to its lateral dimensions, subjected mostly to bending.
- **Two-way slab:** Slab supported on four edges where load is carried in both directions.
- **Aspect ratio (l_x / l_y):** Ratio of longer span to shorter span (both spans defined as clear distance between supports plus effective depth).
- Concrete minimum grade: M20 (f_ck=20 MPa), as per user requirement.
- Steel grade: Fe415 or Fe500 as per prevalent practice.

***

## Assumptions for Design

- Slab behaves as a thin, elastic plate on four edges with simple supports or fixed edges.
- Load distribution modeled using coefficients based on boundary conditions (Tables and charts from IS 456:2000).
- Limit state design philosophy applied: Ultimate Limit State (ULS) for strength and Serviceability Limit State (SLS) for deflection, cracking.

***

## Step 1: Identify Dimensions and Loads

- Define the effective spans: $$l_x$$ and $$l_y$$, where $$l_x \geq l_y$$.
- $$l_x$$ is longer span, $$l_y$$ is shorter span.
- Effective depth, $$d$$, initially assumed or calculated iteratively.
- Calculate design loads (dead load + imposed/live load) per IS 875.
- Convert loads to design loads using load factors for ULS.

***

## Step 2: Determine Moments Using Moment Coefficient Method

### Moment Coefficients (IS 456:2000 Table 26)

Moments for slabs on four edges are obtained from coefficients $$ \alpha_x $$ and $$ \alpha_y $$ for moments about shorter and longer spans respectively.

For uniformly distributed load $$w_u$$:

- Bending moment about shorter span per unit width:

  $$
  M_x = \alpha_x w_u l_x^2
  $$

- Bending moment about longer span per unit width:

  $$
  M_y = \alpha_y w_u l_x^2
  $$

_Table 26 gives $$\alpha_x$$ and $$\alpha_y$$ based on slab aspect ratio and edge conditions._

***

### Edge Conditions Covered (As per IS 456:2000 Table 26)

- All edges simply supported (S-S-S-S)
- Two opposite edges fixed, two edges simply supported (F-F-S-S)
- One edge fixed, the remaining three simply supported (F-S-S-S)
- All four edges fixed (F-F-F-F)

Diagram showing different supports on slab edges:

```
Edge Key:
F = Fixed support
S = Simply Supported
```

| Condition  | Edge 1 | Edge 2 | Edge 3 | Edge 4 |
|------------|---------|---------|---------|---------|
| S-S-S-S    | S       | S       | S       | S       |
| F-F-S-S    | F       | F       | S       | S       |
| F-S-S-S    | F       | S       | S       | S       |
| F-F-F-F    | F       | F       | F       | F       |


```svg
<svg width="1090" height="1850" viewBox="0 0 1090 1850" xmlns="http://www.w3.org/2000/svg">

<style> .slab { fill: #888; opacity: 0.85; } .fixed { stroke: #D32F2F; stroke-width: 12; } .simply { stroke: #388E3C; stroke-width: 12; } .label { font-family: 'Arial', sans-serif; font-size: 28px; font-weight: bold; fill: #222; text-anchor: middle; } .desc { font-family: 'Arial', sans-serif; font-size: 20px; fill: #333; text-anchor: middle; } .case { font-family: 'Arial', sans-serif; font-size: 30px; fill: #222; font-weight:bold; text-anchor: middle; } </style> <!-- One slab unit: lx=220, ly=400, depth=11 --> <!-- Cases arranged in 3 rows of 3 --> <!-- Case 1 --> <g transform="translate(30,45)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="simply" x1="0" y1="0" x2="220" y2="0" /> <line class="simply" x1="220" y1="0" x2="220" y2="400"/> <line class="simply" x1="220" y1="400" x2="0" y2="400"/> <line class="simply" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >S</text> <text class="label" x="110" y="390" >S</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">S</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">S</text> <text class="case" x="110" y="440">Case 1</text> <text class="desc" x="110" y="470">All edges simply supported</text> </g> <!-- Case 2 --> <g transform="translate(300,45)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="fixed" x1="0" y1="0" x2="220" y2="0" /> <line class="fixed" x1="220" y1="0" x2="220" y2="400"/> <line class="simply" x1="220" y1="400" x2="0" y2="400"/> <line class="simply" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >C</text> <text class="label" x="110" y="390" >S</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">S</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">C</text> <text class="case" x="110" y="440">Case 2</text> <text class="desc" x="110" y="470">Edges 1 & 4 continuous, 2 & 3 simply supported</text> </g> <!-- Case 3 --> <g transform="translate(570,45)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="simply" x1="0" y1="0" x2="220" y2="0" /> <line class="fixed" x1="220" y1="0" x2="220" y2="400"/> <line class="simply" x1="220" y1="400" x2="0" y2="400"/> <line class="fixed" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >S</text> <text class="label" x="110" y="390" >S</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">C</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">C</text> <text class="case" x="110" y="440">Case 3</text> <text class="desc" x="110" y="470">Edges 2 & 4 continuous, 1 & 3 simply supported</text> </g> <!-- Case 4 --> <g transform="translate(840,45)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="simply" x1="0" y1="0" x2="220" y2="0" /> <line class="simply" x1="220" y1="0" x2="220" y2="400"/> <line class="fixed" x1="220" y1="400" x2="0" y2="400"/> <line class="fixed" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >S</text> <text class="label" x="110" y="390" >C</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">C</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">S</text> <text class="case" x="110" y="440">Case 4</text> <text class="desc" x="110" y="470">Edges 3 & 4 continuous, 1 & 2 simply supported</text> </g> <!-- Case 5 --> <g transform="translate(30,640)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="fixed" x1="0" y1="0" x2="220" y2="0" /> <line class="simply" x1="220" y1="0" x2="220" y2="400"/> <line class="simply" x1="220" y1="400" x2="0" y2="400"/> <line class="simply" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >C</text> <text class="label" x="110" y="390" >S</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">S</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">S</text> <text class="case" x="110" y="440">Case 5</text> <text class="desc" x="110" y="470">Edge 1 continuous, 2, 3 & 4 simply supported</text> </g> <!-- Case 6 --> <g transform="translate(300,640)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="fixed" x1="0" y1="0" x2="220" y2="0" /> <line class="fixed" x1="220" y1="0" x2="220" y2="400"/> <line class="simply" x1="220" y1="400" x2="0" y2="400"/> <line class="simply" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >C</text> <text class="label" x="110" y="390" >S</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">S</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">C</text> <text class="case" x="110" y="440">Case 6</text> <text class="desc" x="110" y="470">Edges 1 & 2 continuous, 3 & 4 simply supported</text> </g> <!-- Case 7 --> <g transform="translate(570,640)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="simply" x1="0" y1="0" x2="220" y2="0" /> <line class="fixed" x1="220" y1="0" x2="220" y2="400"/> <line class="simply" x1="220" y1="400" x2="0" y2="400"/> <line class="simply" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >S</text> <text class="label" x="110" y="390" >S</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">S</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">C</text> <text class="case" x="110" y="440">Case 7</text> <text class="desc" x="110" y="470">Edge 2 continuous, 1, 3 & 4 simply supported</text> </g> <!-- Case 8 --> <g transform="translate(840,640)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="fixed" x1="0" y1="0" x2="220" y2="0" /> <line class="fixed" x1="220" y1="0" x2="220" y2="400"/> <line class="fixed" x1="220" y1="400" x2="0" y2="400"/> <line class="fixed" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >C</text> <text class="label" x="110" y="390" >C</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">C</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">C</text> <text class="case" x="110" y="440">Case 8</text> <text class="desc" x="110" y="470">All edges continuous</text> </g> <!-- Case 9 --> <g transform="translate(430,1230)"> <rect class="slab" x="0" y="0" width="220" height="400" rx="10" /> <line class="simply" x1="0" y1="0" x2="220" y2="0" /> <line class="fixed" x1="220" y1="0" x2="220" y2="400"/> <line class="fixed" x1="220" y1="400" x2="0" y2="400"/> <line class="fixed" x1="0" y1="400" x2="0" y2="0" /> <text class="label" x="110" y="30" >S</text> <text class="label" x="110" y="390" >C</text> <text class="label" x="13" y="200" transform="rotate(-90 13 200)">C</text> <text class="label" x="207" y="200" transform="rotate(-90 207 200)">C</text> <text class="case" x="110" y="440">Case 9</text> <text class="desc" x="110" y="470">Edges 2, 3 & 4 continuous,<tspan x="110" y="495">Edge 1 simply supported</tspan></text> </g> </svg> ```

***

## Step 3: Design Moments at ULS

- Use factored load $$w_u = 1.5 \times (\text{dead load} + \text{live load})$$.
- Calculate $$M_x$$ and $$M_y$$ using coefficients.
- For given $$M_x, M_y$$, find maximum positive (mid-span) and negative moments (near supports) as per coefficients.
- Select critical moments to design the reinforcement.

***

## Step 4: Design of Reinforcement (Flexure)

- Use limit state design formulas for reinforced concrete flexure:

$$
M_u = 0.87 f_y A_s d (1 - \frac{A_s f_y}{f_{ck} b d})
$$

where,
- $$M_u$$ = factored moment (Nmm),
- $$f_y$$ = steel yield strength (N/mm²),
- $$A_s$$ = area of tensile reinforcement (mm²),
- $$f_{ck}$$ = characteristic compressive strength of concrete,
- $$b$$ = breadth (width per meter strip, b=1000 mm for slabs),
- $$d$$ = effective depth (mm).

Calculate $$A_s$$, ensure minimum steel as per IS 456 Clause 26.5 (for slabs, usually 0.15% of gross cross-section area).

***

## Step 5: Check Shear (One-Way Shear and Two-Way Punching Shear)

- Calculate critical shear force at a distance $$d$$ from support.
- Design shear strength $$ \tau_c $$ from IS 456 Table 19 and Clause 40.
- If required, provide shear reinforcement.

***

## Step 6: Check Bond and Development Length

- Calculate development length $$l_d$$ as per IS 456 clauses.
- Ensure sufficient anchorage for reinforcement.

***

## Step 7: Serviceability Checks

### Deflection

- Calculate span/depth ratio limits as per IS 456 Table 7.
- Compute estimated deflection; ensure it is within limits for crack control and serviceability.

### Crack Width

- Minimum reinforcement provided as per IS 456 Clause 26.5 for crack width control.
- Check spacing, size, and cover of reinforcement using SP 34 guidelines.

***

## Step 8: Detailing of Reinforcement

- As per IS 456 Clause 26 and SP 34.
- Provide bottom reinforcement spanning the slab length in both directions.
- Place top reinforcement near supports where negative bending moments exist.
- Maintain minimum cover of 20-25 mm for slabs.
- Distribution bars (secondary bars) to be minimum 0.15% of cross-section.
- Anchorage and lap lengths per IS 456 Clause 26.2.

***

## Solved Examples

### Example 1: Two-Way Slab with All Edges Simply Supported (S-S-S-S)

**Given:**

- Span $$l_x = 5\,m$$, $$l_y = 4\,m$$
- Thickness $$h=150\,mm$$
- Live load = 3 kN/m², Dead load (Self weight) = $$24 \times 0.15 = 3.6\,kN/m^2$$
- Concrete grade M20, Steel Fe415

**Find:** Moments $$M_x$$, $$M_y$$, design reinforcement area $$A_s$$ for slab per meter width.

*Solution:*

1. Calculate total load:

$$
w = 3 + 3.6 = 6.6\,kN/m^2
$$

Factored load:

$$
w_u = 1.5 \times 6.6 = 9.9\,kN/m^2
$$

2. Aspect ratio:

$$
\frac{l_x}{l_y} = \frac{5}{4} = 1.25
$$

3. From IS 456 Table 26 for S-S-S-S slab with aspect ratio 1.25,

$$
\alpha_x = 0.053, \quad \alpha_y = 0.063
$$

4. Calculate moments per meter width:

$$
M_x = 0.053 \times 9.9 \times 5^2 = 0.053 \times 9.9 \times 25 = 13.122\,kNm
$$

$$
M_y = 0.063 \times 9.9 \times 25 = 15.593\,kNm
$$

Convert $$kNm$$ to $$Nmm$$:

$$
M_x = 13.122 \times 10^6\,Nmm,\quad M_y = 15.593 \times 10^6\,Nmm
$$

5. Assume effective depth $$d = 130\,mm$$ (cover + bar diameter approx. 20 mm + 16 mm bar diameter + tolerance).

6. Designing for $$M_y$$ (critical moment):

$$
A_s = \frac{M}{0.87 f_y d \left(1 - \frac{f_y A_s}{f_{ck} b d}\right)} \quad \rightarrow \text{Iterative solution}
$$

For initial approximation (neglect term in bracket denominator):

$$
A_s = \frac{M}{0.87 f_y d} = \frac{15.593 \times 10^6}{0.87 \times 415 \times 130} = 333.3\,mm^2
$$

7. Check minimum steel (IS 456 Clause 26.5):

$$
\text{Minimum } A_s = 0.15\% \times b \times d = 0.0015 \times 1000 \times 130 = 195\,mm^2
$$

Thus, provide $$A_s = 334\,mm^2$$ >= minimum steel.

***

The full design includes shear, bond, deflection, crack width checks and detailing based on IS codes.

***

## Summary

| Design Step                 | Reference Clause          | Notes                                          |
|----------------------------|--------------------------|------------------------------------------------|
| Load calculation            | IS 875                   | Dead + Live, factor 1.5 for ULS                |
| Moment coefficients         | IS 456 Table 26          | Based on aspect ratio and edge conditions      |
| Flexural design             | IS 456 Clause 39, 40     | Design $$A_s$$ for moments                      |
| Minimum steel               | IS 456 Clause 26.5       | Min steel for flexure; 0.15% for slabs         |
| Shear                      | IS 456 Clause 40         | Shear strength, shear reinforcement if needed |
| Bond and development length | IS 456 Clause 26.2       | Provide proper anchorage                         |
| Deflection                  | IS 456 Clause 23         | Limits on span/depth ratio                       |
| Crack width/spacing         | IS 456 Clause 26.5, SP 34| Control crack width through reinforcement       |
| Detailing                   | IS 456 Clause 26, SP 34  | Cover, bar spacing, anchorage                    |

***
