# T-Beam
-![1](Flanged1.jpg)
-![1.1](introimg1.jpg)
## Assumptions 

<p>Following are the assumptions made in the theory of Simple Bending: </p>
<p>1. The material of the beam is homogenous and isotropic. </p>
<p>2. The beam is initially straight, and all the longitudinal fibers bend in circular arcs with a common center of curvature. </p>
<p>3. Members have symmetric cross-sections and are subjected to bending in the plane of symmetry. </p>
<p>4. The beam is subjected to pure bending and the effect of shear is neglected. </p>


<p>The following assumptions are relevant in the computation of the ultimate flexural strength of reinforced concrete sections: [IS: 456- 2000 Clause 38.1]</p>
<p>1) Plane sections normal to the axis remain plane after bending. (strain at any point on the cross-section is directly proportional to its distance from the neutral axis)</p>
<p>2) The maximum strain in concrete at the extreme compression fiber is assumed as 0.003 in flexure</p>
<p>3) The relationship between the compressive stress distribution in concrete and the strain in concrete may be assumed to be rectangle, trapezoid, parabola, or any other shape which results in strength prediction in substantial agreement with the test results. The recommended stress-strain curve is shown below which shows the characteristic and design strength curves.</p>

-![1.2](curves1.jpg) 
<p>4) Tensile strength of concrete is ignored.</p>
<p>5) The stresses in the reinforcement are obtained from the stress-strain curves shown below. For design purposes, the partial safety factor Y<sub>m</sub> equal to 1.15 is applied to compute the design strength.</p>

-![1.3](stress_strain.jpg) 
<p>6) The maximum strain in the tension reinforcement in the section at the collapse limit state shall be not less than $$[\frac{f_y}{1.15E_s}+0.002] = [\frac{0.87f_y}{E_s}+0.002]$$</p>
   
The slab is assumed to act as a compression flange only if: [IS 456 - 2000 Cl 23.1.1]
  1. Web and slab effectively bond together or are cast integrally
  2. If the main reinforcement in the slab or flange is parallel to the beam then the longitudinal reinforcement will be 60% of the main reinforcement, as shown:
     -![2](23.1.11.jpg)
     -![2.1](iscode.png)
## Analysis and Design
<math>
<p>Three cases to be considered while designing the flanged beam -</p>
  <p>Case 1. Neutral Axis lies within the flange (x<sub>u</sub> &#60; D<sub>f</sub>)</p>
  <p>Case 2. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is uniformly stressed (D<sub>f</sub>/d &#60; 0.2)</p>
  <p>Case 3. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is not uniformly stressed (D<sub>f</sub>/d &#62; 0.2)</p>
 
  -![3](cases31.jpg)
  
<p>To check whether NA lies within the flange or not - </p>
  <p>$$\frac{D_f}{d} = \frac{0.0035-0.002}{0.0038+0.0035}$$</p>
  <p>D<sub>f</sub>/d = 0.2 </p>
  <p>x<sub>u</sub>/d &#60; D<sub>f</sub>/d &rarr; NA lies within the flange</p>
  <p>x<sub>u</sub>/d &#62; D<sub>f</sub>/d &rarr; NA lies below the flange area</p>
  
  <p>Considering the three cases, checking where NA lies -</p>
  <p>Case 1. Neutral Axis lies within the flange (x<sub>u</sub> &#60; D<sub>f</sub>)</p>
  
  -![4](within11.png)

  <p>$$M_{u,lim} = 0.36f_{ck}x_u(d-0.42x_u)b_f$$ [IS 456 - 2000 ANNEX-G]</p>
  <p>x<sub>u</sub>/d can be calculated from - $$M_{u,lim} = 0.36f_{ck}(\frac{x_u}{d})(1-0.42(\frac{x_u}{d}))b_fd^2$$</p>
  
  <p>When x<sub>u</sub> = D<sub>f</sub>, replacing x<sub>u</sub> with D<sub>f</sub>:</p>
    <p>$$M_{u.lim} = 0.36f_{ck}D_f(d-0.42D_f)b_f$$</p>

  <p>If only a cross-section of the beam is given -</p>
    <p>depth of neutral axis = $$\frac{x_u}{d} = \frac{0.87f_yA_{st}}{0.36f_{ck}b_fd}$$ [IS 456 - 2000 ANNEX-G Cl 38.1 G-1.1]</p>
    <p>or</p>
    <p>$$x_u = \frac{0.87f_yA_{st}}{0.36f_{ck}b_f}$$</p>

  <p>Case 2. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is uniformly stressed (D<sub>f/</sub>d &#60; 0.2)</p>
    <p>$$M_{u1} = 0.36f_{ck}b_wx_u(d-0.42x_u)$$</p>
    <p>$$M_{u2} = 0.45f_{ck}D_f(b_f-b_w)(d-0.5D_f)$$</p>
    <p>$$M_u = M_{u1} + M_{u2}$$</p>
       <p>$$M_u = 0.36f_{ck}b_wx_u(d-0.42x_u) + 0.45f_{ck}D_f(b_f-b_w)(d-0.5D_f)$$ [IS 456 - 2000 ANNEX-G G-2.2]</p>
       
  <p>Case 3. Neutral Axis lies below the flange (x<sub>u</sub> &#62; D<sub>f</sub>) & flange is not uniformly stressed (D<sub>f</sub>/d &#62; 0.2)</p>
    <p>$$y_f = 0.15x_u + 0.65D_f$$ instead of D<sub>f</sub> is to be substituted in - [IS 456 - 2000 ANNEX-G G-2.2.1]</p>
    <p>$$M_u = 0.36f_{ck}b_wx_u(d-0.42x_u) + 0.45f_{ck}y_f(b_f-b_w)(d-0.5y_f)$$ </p>
    <p>Note that - y<sub>f</sub> &#60; Df always</p>
    
  -![5](below11.png)
  
### Design steps for T-Beam

<p>Step 1. Assume the dimensions of T-Beam </p>
<p>effective depth (d) = span/12 to Span/15 </p>
<p>b<sub>w</sub> = 150 mm to 400 mm </p>
    <p>or</p>
     <p>d/2 to d/3</p>
<p>Effective cover to be assumed as 40 to 50 mm</p>
<p>Overall depth (D) = effective depth (d) + clear cover</p>

<p>Step 2. Calculate the effective span of the beam (l<sub>o</sub>)</p>
<p>It will be the least value of:</p>
<p>1. Centre to centre of bearings</p>
<p>2. Clear span + effective depth</p>
<p>l<sub>o</sub> being c/c of two supports or between two points of contraflexure (assume width of supports if not given)</p>

<p>Step 3. Find the effective width of flange (b<sub>f</sub>) [IS 456 - 2000 Cl 23.1.2]</p>
<p>In no case should b<sub>f</sub> be more than b<sub>w</sub> + 1/2(clear distance to the adjacent beams on either side)</p>
<p>$$b_f = \frac{l_o}{6} + b_w + 6D_f$$ </p>
<p>For Isolated T-Beam &rarr;</p>
<p>$$b_f = \frac{l_o}{((\frac{l_o}{b})+4)} + b_w$$</p>

<p>Step 4. Load Calculations</p>
<p>Calculate the self-weight/dead load (W<sub>d</sub>) of the T-Beam</p>
<p>Self-weight of the flange + Self-weight of the web</p>
<p>(Assume superimposed load (W<sub>s</sub>) of not given in the question)</p>
<p>Total Load = Superimposed Load + Self-weight</p>
<p>W<sub>u</sub> = W<sub>s</sub> + W<sub>d</sub></p>
<p>Find the factored design load (factored design UDL per m length of the beam)</p>

<p>Step 5. Calculate factored design moment (Ultimate maximum bending moment Mu) and Shear Force</p>
<p>$$M_u = \frac{W_ul^2}{8}$$</p>
<p>$$V_u = \frac{W_ul}{2}$$</p>

<p>Step 6. Find the area of reinforcement</p>
<p>Different cases that arrive are -</p>
<p>(a) Assume D<sub>f</sub>/x<sub>u</sub> &le; 0.43</p>
<p>Calculate M<sub>u,lim</sub></p>
 <p> $$M_{u,lim} = 0.45f_ckD_fb_f(d-0.5D_f)$$</p>
<p>If M<sub>u</sub> &#60; M<sub>u,lim</sub> Singly reinforced section is to be designed </p>
<p>If M<sub>u</sub> &#62; M<sub>u,lim</sub> Doubly reinforced section is to be designed </p>

<p>(b) If M<sub>u</sub> &#60; M<sub>u,lim</sub> determine ultimate moment of resistance M<sub>u</sub>'</p>
 <p> $$M_u^{'} = 0.36f_{ck}b_fD_f(d-0.42D_f)$$ [Assuming x<sub>u</sub> = D<sub>f</sub> i.e., considering that the neutral axis coincides with the bottom of the flange]</p>

  <p>If M<sub>u</sub> &#60; M<sub>u'</sub> then x<sub>u</sub> &#60; D<sub>f</sub></p>
  <p>&there4; Find A<sub>st</sub> from the relation:</p>
    <p>$$M_u = 0.87f_yA_{st}[d-(\frac{f_yA_{st}}{f_{ck}b_f})]$$</p>

<p>(c) If M<sub>u</sub> &#62; M<sub>u'</sub> but less than M<sub>u</sub>,lim determine ultimate moment of resistance M<sub>u"</sub></p>
 <p> $$M_u^" = 0.36f_{ck}b_wx_u(d-0.42x_u) + 0.45f_{ck}D_f(b_f-b_w)(d-0.5D_f)$$ [Assume D<sub>f</sub>/x = 0.43]</p>

  <p>If M<sub>u</sub> &#62; M<sub>u"</sub> then D<sub>f</sub>/x<sub>u</sub> &#60; 0.43</p>

  <p>Now determine x<sub>u</sub> corresponding to M<sub>u</sub> for D<sub>f</sub>/x<sub>u</sub> &#60; 0.43</p>
   <p> $$M_u = 0.36f_{ck}b_wx_u(d-0.42x_u) + 0.45f_{ck}D_f(b_f-b_w)(d-0.5D_f)$$</p>
  <p>Calculate A<sub>st</sub> from the known value of x<sub>u</sub></p>
    <p>$$A_st = \frac{0.36f_{ck}b_wx_u + 0.45f_{ck}y_f(b_f-b_w)}{0.87f_y}$$</p>

  <p>If M<sub>u</sub> &#60; M<sub>u"</sub> then D<sub>f</sub>/x<sub>u</sub> &#62; 0.43</p>

  <p>Now determine x<sub>u</sub> corresponding to M<sub>u</sub> by solving the quadratic equation in x<sub>u</sub></p>
   <p>$$M_u = 0.36f_{ck}b_wx_u(d-0.42x_u) + 0.45f_{ck}y_f(b_f-b_w)(d-0.5y_f)$$</p>
  <p>Calculate A<sub>st</sub> from the known value of x<sub>u</sub> </p>
    <p>$$A_st = \frac{0.36f_{ck}b_wx_u + 0.45f_{ck}y_f(b_f-b_w)}{0.87f_y}$$</p>

<p>Step 7. Check for shear and design shear reinforcement if needed.</p>
<p>Nominal Shear Stress $$&Tau;_v = [\frac{V_u}{b_wd}]$$</p>
<p>$$p_t = [\frac{100A_{st}}{b_wd}]$$</p>
<p>Calculate &Tau;<sub>c</sub> (shear stress in concrete) corresponding to the value of &Tau;<sub>v</sub>
<p>If &Tau;<sub>c</sub> &#62; &Tau;<sub>v</sub> then there is no need to design shear reinforcement.</p>

<p>Step 8. Check for development length </p>
<p>Step 9. Check for deflection to satisfy the limit state of serviceability.</p>
<p>Step 10. Write a summary of the design and draw a neat sketch.</p>

### Example:

<p>Given values:</p>
<p>b<sub>f</sub> = 1000 mm</p>
<p>D<sub>f</sub> = 125 mm</p>
<p>b<sub>w</sub> = 250 mm</p>
<p>D = 400 mm</p>
<p>Area of tensile steel = 5-20&Phi;</p>

<p>d = D - clear cover - &Phi;/2</p>
  <p>= 400 - 25 - 20/2</p>
 <p> = 365 mm</p>
<p>$$Ast = \frac{5\Pi(20)^2}{4}$$</p>

<p>1. Assuming tensile steel yields:</p>
 <p> $$x_u = \frac{0.87f_yA_{st}}{0.36f_{ck}b_f}$$</p>
    <p> $$= 52.48 mm$$</p>
 <p>x<sub>u</sub> &#60; D<sub>f</sub>, So we can say that NA is within the flange</p>

<p>2. Lever arm depth</p>
   <p>$$z = (d - 0.42x_u)$$</p>
     <p>$$= 342.9584 mm$$</p>

<p>3. Moment of resistance due to concrete failure</p>
  <p>$$MOR_c = M_u = Cz = 0.36f_{ck}b_fx_uz = 194.378 KNm$$</p>

<p>4. Moment of resistance due to steel yield</p>
 <p>$$MOR_t = M_u = Tz = 0.87f_yA_{st}z = 194.4 KNm$$</p>

 <p> NA lies within the flange so we can calculate the Moment of resistance for both concrete and steel.</p>
</math>
Thank you!
