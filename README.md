# T-Beam
-![1](introimg1.jpg)
## Assumptions 
The slab is assumed to act as a compression flange only if: [IS 456 - 2000 Cl 23.1.1]<br>
  1. Web and slab effectively bond together or are cast integrally<br>
  2. If the main reinforcement in the slab or flange is parallel to the beam then the longitudinal reinforcement will be 60% of the main reinforcement, as shown:<br>
     -![2](23.1.11.jpg)<br>
## Analysis and Design
<math>
Three cases to be considered while designing the flanged beam -<br>
  Case 1. Neutral Axis lies within the flange (xu &#60; Df)<br>
  Case 2. Neutral Axis lies below the flange (xu &#62; Df) & flange is uniformly stressed (Df/d &#60; 0.2)<br>
  Case 3. Neutral Axis lies below the flange (xu &#62; Df) & flange is not uniformly stressed (Df/d &#62; 0.2)<br>
  
  -![3](cases31.jpg)<br>
  
To check whether NA lies within the flange or not - <br>
  Df/d = (0.0035-0.002)/(0.0038+0.0035)<br>
  Df/d = 0.2 <br>
  xu/d &#60; Df/d &rarr; NA lies within the flange<br>
  xu/d &#62; Df/d &rarr; NA lies below the flange area<br>
  
  Considering the three cases, checking where NA lies -<br>
  Case 1. Neutral Axis lies within the flange (xu &#60; Df)<br>
  -![4](within.png)<br>
    Mu,lim = 0.36fckxu(d-0.42xu)bf [IS 456 - 2000 ANNEX-G]<br>
  xu/d can be calculated from - Mu,lim = 0.36fck(xu/d)(1-0.42(xu/d))bfd^2<br>
  
  When xu = Df, replacing xu with Df:<br>
    Mu.lim = 0.36fckDf(d-0.42Df)bf<br>

  If only cross-section of the beam is given -<br>
    depth of neutral axis = xu/d = 0.87fyAst/0.36fckbfd [IS 456 - 2000 ANNEX-G Cl 38.1 G-1.1]<br>
    or<br>
    xu = 0.87fyAst/0.36fckbf<br>

  Case 2. Neutral Axis lies below the flange (xu &#62; Df) & flange is uniformly stressed (Df/d &#60; 0.2)<br>
    Mu1 = 0.36fckbwxu(d-0.42xu)<br>
    Mu2 = 0.45fckDf(bf-bw)(d-0.5Df)<br>
    Mu = Mu1 + Mu2<br>
       = 0.36fckbwxu(d-0.42xu) + 0.45fckDf(bf-bw)(d-0.5Df) [IS 456 - 2000 ANNEX-G G-2.2]<br>
  Case 3. Neutral Axis lies below the flange (xu &#62; Df) & flange is not uniformly stressed (Df/d &#62; 0.2)<br>
    yf = 0.15xu + 0.65Df instead of Df is to be substituted in - [IS 456 - 2000 ANNEX-G G-2.2.1]<br>
    Mu = = 0.36fckbwxu(d-0.42xu) + 0.45fckyf(bf-bw)(d-0.5yf) <br>
    Note that - yf &#60; Df always<br>
  -![5](below.png)<br>
### Design steps for T-Beam
Step 1. Assume the dimensions of T-Beam <br>
d = span/12 to Span/15 <br>
bw = 150 mm to 400 mm <br>
    or<br>
     d/2 to d/3<br>
Effective cover to be assumed as 40 to 50 mm<br>

Step 2. Calculate the effective span of the beam (lo)<br>
lo being c/c of two supports or between two points of contraflexure (assume width of supports if not given)<br>

Step 3. Find the effective width of flange (b<sub>f</sub>) [IS 456 - 2000 Cl 23.1.2]<br>
In no case should bf be more than b<sub>w</sub> + 1/2(clear distance to the adjacent beams on either side)<br>
bf = lo/6 + bw + 6Df <br>
For Isolated T-Beam &rarr;<br>
bf = lo/((lo/b)+4) + bw<br>

Step 4. Load Calculations<br>
Calculate the self-weight/dead load (Wd) of the T-Beam<br>
Self-weight of the flange + Self-weight of the web<br>
(Assume superimposed load (Ws) of not given in the question)<br>
Total Load = Superimposed Load + Self-weight<br>
Wu = Ws + Wd<br>
Find the factored design load (factored design UDL per m length of the beam)<br>

Step 5. Calculate factored design moment (Ultimate maximum bending moment Mu)<br>
Mu = Wul^2/8<br>

Step 6. Find the area of reinforcement<br>
Different cases that arrive are -<br>
(a) Assume Df/xu &le; 0.43 and neglect contribution of rib in resisting moment<br>
Calculate Mu,lim<br>
  Mu,lim = 0.45fckDfbf(d-0.5Df)<br>
If Mu &#60; Mu,lim Singly reinforced section is to be designed <br>
If Mu &#62; Mu,lim Doubly reinforced section is to be designed <br>

(b) If Mu &#60; Mu,lim determine ultimate moment of resistance Mu'<br>
  Mu' = 0.36fckbfDf(d-0.42Df) [Assuming xu = Df i.e., considering that the neutral axis coincides with the bottom of the flange]<br>

  If Mu &#60; Mu' then xu &#60; Df<br>
  &there4; Find Ast from the relation:<br>
    Mu = 0.87fyAst[d-(fsAst/fckbf)]<br>

(c) If Mu &#62; Mu' but less than Mu,lim determine ultimate moment of resistance Mu"<br>
  Mu" = 0.36fckbwxu(d-0.42xu) + 0.45fckDf(bf-bw)(d-0.5Df) [Assume Df/x = 0.43]<br>

  If Mu &#62; Mu" then Df/xu &#60; 0.43<br>

  Now determine xu corresponding to Mu for Df/xu &#60; 0.43<br>
    Mu = 0.36fckbwxu(d-0.42xu) + 0.45fckDf(bf-bw)(d-0.5Df)<br>
  Calculate Ast from the known value of xu<br>
    Ast = 0.36fckbwxu + 0.45fckDf(bf-bw)/0.87fy<br>

  If Mu &#60; Mu" then Df/xu &#62; 0.43<br>

  Now determine xu corresponding to Mu by solving the quadratic equation in xu<br>
    Mu = = 0.36fckbwxu(d-0.42xu) + 0.45fckyf(bf-bw)(d-0.5yf)<br>
  Calculate Ast from the known value of xu <br>
    Ast = 0.36fckbwxu + 0.45fckyf(bf-bw)0.87fy<br>

Step 7. Check for Shear and design shear reinforcement if needed.<br>
Step 8. Check for development length <br>
Step 9. Check for deflection to satisfy the limit state of serviceability.<br>
Step 10. Write a summary of the design and draw a neat sketch.<br>

### Example:

Given values:<br>
bf = 1000 mm<br>
Df = 125 mm<br>
bw = 250 mm<br>
D = 400 mm<br>
Area of tensile steel = 5-20&Phi;<br>

d = D - clear cover - &Phi;/2<br>
  = 400 - 25 - 20/2<br>
  = 365 mm<br>
Ast = 5&Pi;(20)^2/4<br>

1. Assuming tensile steel yields:<br>
  xu = 0.87fyAst/0.36fckbf<br>
     = 52.48 mm<br>
  xu &#60; Df, So we can say that NA is within the flange<br>

2. Lever arm depth<br>
   z = (d - 0.42xu)<br>
     = 342.9584 mm<br>

3. Moment of resistance due to concrete failure<br>
   MORc = Mu = Cz = 0.36fckbfxuz = 194.378 KNm<br>

4. Moment of resistance due to steel yield<br>
   MORt = Mu = Tz = 0.87fyAstz = 194.4 KNm<br>

  NA lies within the flange so we can calculate the Moment of resistance either for concrete or steel both.<br>
  
</math>
