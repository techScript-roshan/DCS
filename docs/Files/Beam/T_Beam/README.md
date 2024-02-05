# T-Beam
-![1](introimg1.jpg)
## Assumptions 
The slab is assumed to act as a compression flange only if: [IS 456 - 2000 Cl 23.1.1]
  1. Web and slab effectively bond together or are cast integrally
  2. If the main reinforcement in the slab or flange is parallel to the beam then the longitudinal reinforcement will be 60% of the main reinforcement, as shown:
     -![2](23.1.11.jpg)
## Analysis and Design
<math>
<p>Three cases to be considered while designing the flanged beam -</p>
  <p>Case 1. Neutral Axis lies within the flange (x<sub>u</sub> &#60; D<sub>f</sub>)</p>
  <p>Case 2. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is uniformly stressed (D<sub>f</sub>/d &#60; 0.2)</p>
  <p>Case 3. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is not uniformly stressed (D<sub>f</sub>/d &#62; 0.2)</p>
 
  -![3](cases31.jpg)
  
<p>To check whether NA lies within the flange or not - </p>
  <p>D<sub>f</sub>/d = (0.0035-0.002)/(0.0038+0.0035)</p>
  <p>D<sub>f</sub>/d = 0.2 </p>
  <p>x<sub>u</sub>/d &#60; D<sub>f</sub>/d &rarr; NA lies within the flange</p>
  <p>x<sub>u</sub>/d &#62; D<sub>f</sub>/d &rarr; NA lies below the flange area</p>
  
  <p>Considering the three cases, checking where NA lies -</p>
  <p>Case 1. Neutral Axis lies within the flange (x<sub>u</sub> &#60; D<sub>f</sub>)</p>
  
  -![4](within11.png)
    <p>M<sub>u,lim</sub> = 0.36f<sub>ck</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>)bf [IS 456 - 2000 ANNEX-G]</p>
  <p>x<sub>u</sub>/d can be calculated from - M<sub>u,lim</sub> = 0.36f<sub>ck</sub>(x<sub>u</sub>/d)(1-0.42(x<sub>u</sub>/d))b<sub>f</sub>d<sup>2</sup></p>
  
  <p>When x<sub>u</sub> = D<sub>f</sub>, replacing x<sub>u</sub> with D<sub>f</sub>:</p>
    <p>M<sub>u.lim</sub> = 0.36f<sub>ck</sub>D<sub>f</sub>(d-0.42D<sub>f</sub>)b<sub>f</sub></p>

  <p>If only a cross-section of the beam is given -</p>
    <p>depth of neutral axis = x<sub>u</sub>/d = 0.87f<sub>y</sub>A<sub>st</sub>/0.36f<sub>ck</sub>b<sub>f</sub>d [IS 456 - 2000 ANNEX-G Cl 38.1 G-1.1]</p>
    <p>or</p>
    <p>xu = 0.87f<sub>y</sub>A<sub>st</sub>/0.36f<sub>ck</sub>b<sub>f</sub></p>

  <p>Case 2. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is uniformly stressed (D<sub>f/</sub>d &#60; 0.2)</p>
    <p>M<sub>u1</sub> = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>)</p>
    <p>M<sub>u2</sub> = 0.45f<sub>ck</sub>D<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)(d-0.5D<sub>f</sub>)</p>
    <p>M<sub>u</sub> = M<sub>u1</sub> + M<sub>u2</sub></p>
       <p>= 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>) + 0.45f<sub>ck</sub>D<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)(d-0.5D<sub>f</sub>) [IS 456 - 2000 ANNEX-G G-2.2]</p>
  <p>Case 3. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is not uniformly stressed (D<sub>f</sub>/d &#62; 0.2)</p>
    <p>y<sub>f</sub> = 0.15x<sub>u</sub> + 0.65D<sub>f</sub> instead of D<sub>f</sub> is to be substituted in - [IS 456 - 2000 ANNEX-G G-2.2.1]</p>
    <p>M<sub>u</sub> = = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>) + 0.45f<sub>ck</sub>y<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)(d-0.5y<sub>f</sub>) </p>
    <p>Note that - y<sub>f</sub> &#60; Df always</p>
    
  -![5](below11.png)
### Design steps for T-Beam
<p>Step 1. Assume the dimensions of T-Beam </p>
<p>d = span/12 to Span/15 </p>
<p>b<sub>w</sub> = 150 mm to 400 mm </p>
    <p>or</p>
     <p>d/2 to d/3</p>
<p>Effective cover to be assumed as 40 to 50 mm</p>

<p>Step 2. Calculate the effective span of the beam (lo)</p>
<p>l<sub>o</sub> being c/c of two supports or between two points of contraflexure (assume width of supports if not given)</p>

<p>Step 3. Find the effective width of flange (b<sub>f</sub>) [IS 456 - 2000 Cl 23.1.2]</p>
<p>In no case should bf be more than b<sub>w</sub> + 1/2(clear distance to the adjacent beams on either side)</p>
<p>b<sub>f</sub> = l<sub>o</sub>/6 + b<sub>w</sub> + 6D<sub>f</sub> </p>
<p>For Isolated T-Beam &rarr;</p>
<p>b<sub>f</sub> = l<sub>o</sub>/((l<sub>o</sub>/b)+4) + b<sub>w</sub></p>

<p>Step 4. Load Calculations</p>
<p>Calculate the self-weight/dead load (W<sub>d</sub>) of the T-Beam</p>
<p>Self-weight of the flange + Self-weight of the web</p>
<p>(Assume superimposed load (W<sub>s</sub>) of not given in the question)</p>
<p>Total Load = Superimposed Load + Self-weight</p>
<p>W<sub>u</sub> = W<sub>s</sub> + W<sub>d</sub></p>
<p>Find the factored design load (factored design UDL per m length of the beam)</p>

<p>Step 5. Calculate factored design moment (Ultimate maximum bending moment Mu)</p>
<p>M<sub>u</sub> = W<sub>u</sub>l<sup>2</sup>/8</p>

<p>Step 6. Find the area of reinforcement</p>
<p>Different cases that arrive are -</p>
<p>(a) Assume D<sub>f</sub>/x<sub>u</sub> &le; 0.43 and neglect contribution of rib in resisting moment</p>
<p>Calculate M<sub>u,lim</sub></p>
 <p> M<sub>u,lim</sub> = 0.45f<sub>ck</sub>D<sub>f</sub>b<sub>f</sub>(d-0.5D<sub>f</sub>)</p>
<p>If M<sub>u</sub> &#60; M<sub>u,lim</sub> Singly reinforced section is to be designed </p>
<p>If M<sub>u</sub> &#62; M<sub>u,lim</sub> Doubly reinforced section is to be designed </p>

<p>(b) If M<sub>u</sub> &#60; M<sub>u,lim</sub> determine ultimate moment of resistance M<sub>u</sub>'</p>
 <p> M<sub>u'</sub> = 0.36f<sub>ck</sub>b<sub>f</sub>D<sub>f</sub>(d-0.42D<sub>f</sub>) [Assuming x<sub>u</sub> = D<sub>f</sub> i.e., considering that the neutral axis coincides with the bottom of the flange]</p>

  <p>If M<sub>u</sub> &#60; M<sub>u'</sub> then x<sub>u</sub> &#60; D<sub>f</sub></p>
  <p>&there4; Find A<sub>st</sub> from the relation:</p>
    <p>M<sub>u</sub> = 0.87f<sub>y</sub>A<sub>st</sub>[d-(f<sub>s</sub>A<sub>st</sub>/f<sub>ck</sub>b<sub>f</sub>)]</p>

<p>(c) If M<sub>u</sub> &#62; M<sub>u'</sub> but less than M<sub>u</sub>,lim determine ultimate moment of resistance M<sub>u"</sub></p>
 <p> M<sub>u"</sub> = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>) + 0.45f<sub>ck</sub>D<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)(d-0.5D<sub>f</sub>) [Assume D<sub>f</sub>/x = 0.43]</p>

  <p>If M<sub>u</sub> &#62; M<sub>u"</sub> then D<sub>f</sub>/x<sub>u</sub> &#60; 0.43</p>

  <p>Now determine x<sub>u</sub> corresponding to M<sub>u</sub> for D<sub>f</sub>/x<sub>u</sub> &#60; 0.43</p>
   <p> M<sub>u</sub> = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>) + 0.45f<sub>ck</sub>D<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)(d-0.5D<sub>f</sub>)</p>
  <p>Calculate A<sub>st</sub> from the known value of x<sub>u</sub></p>
    <p>A<sub>st</sub> = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub> + 0.45f<sub>ck</sub>D<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)/0.87f<sub>y</sub></p>

  <p>If M<sub>u</sub> &#60; M<sub>u"</sub> then D<sub>f</sub>/x<sub>u</sub> &#62; 0.43</p>

  <p>Now determine x<sub>u</sub> corresponding to M<sub>u</sub> by solving the quadratic equation in x<sub>u</sub></p>
   <p> M<sub>u</sub> = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub>(d-0.42x<sub>u</sub>) + 0.45f<sub>ck</sub>y<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)(d-0.5y<sub>f</sub>)</p>
  <p>Calculate A<sub>st</sub> from the known value of x<sub>u</sub> </p>
    <p>A<sub>st</sub> = 0.36f<sub>ck</sub>b<sub>w</sub>x<sub>u</sub> + 0.45f<sub>ck</sub>y<sub>f</sub>(b<sub>f</sub>-b<sub>w</sub>)0.87f<sub>y</sub></p>

<p>Step 7. Check for Shear and design shear reinforcement if needed.</p>
<p>Step 8. Check for development length </p>
<p>Step 9. Check for deflection to satisfy the limit state of serviceability.</p>
<p>Step 10. Write a summary of the design and draw a neat sketch.</p>

### Example:

<p>Given values:</p>
<p>bf = 1000 mm</p>
<p>Df = 125 mm</p>
<p>bw = 250 mm</p>
<p>D = 400 mm</p>
<p>Area of tensile steel = 5-20&Phi;</p>

<p>d = D - clear cover - &Phi;/2</p>
  <p>= 400 - 25 - 20/2</p>
 <p> = 365 mm</p>
<p>Ast = 5&Pi;(20)^2/4</p>

<p>1. Assuming tensile steel yields:</p>
 <p> xu = 0.87fyAst/0.36fckbf</p>
    <p> = 52.48 mm</p>
 <p> xu &#60; Df, So we can say that NA is within the flange</p>

<p>2. Lever arm depth</p>
   <p>z = (d - 0.42xu)</p>
     <p>= 342.9584 mm</p>

<p>3. Moment of resistance due to concrete failure</p>
  <p> MORc = Mu = Cz = 0.36fckbfxuz = 194.378 KNm</p>

<p>4. Moment of resistance due to steel yield</p>
 <p>  MORt = Mu = Tz = 0.87fyAstz = 194.4 KNm</p>

 <p> NA lies within the flange so we can calculate the Moment of resistance for both concrete and steel.</p>
  
</math>
Thank you!
