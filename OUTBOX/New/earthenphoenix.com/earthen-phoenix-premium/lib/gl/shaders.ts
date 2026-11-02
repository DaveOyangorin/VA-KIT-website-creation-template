/**
 * Shaders for the living photograph (components/three/LivingPhoto.tsx).
 * One photo surface, one particle layer, plus constellation lines and tarot cards for the readings page.
 * Every effect is defined in plane space: uv 0..1 across the hero, y up. Mode numbers follow MODE in LivingPhoto.
 */

const COMMON = /* glsl */ `
uniform float uT, uMode, uAsp;
uniform vec3 uP[4];
bool M(float m) { return abs(uMode - m) < .5; }
vec2 A(vec2 d) { return d * vec2(uAsp, 1.); }
float G(vec2 d, float r) { return exp(-dot(d, d) / (r * r)); }
float h21(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float vnoise(vec2 p) {
  vec2 i = floor(p), f = fract(p); f = f * f * (3. - 2. * f);
  return mix(mix(h21(i), h21(i + vec2(1., 0.)), f.x), mix(h21(i + vec2(0., 1.)), h21(i + vec2(1., 1.)), f.x), f.y);
}
float fbm(vec2 p) { float a = .5, s = 0.; for (int i = 0; i < 4; i++) { s += a * vnoise(p); p *= 2.03; a *= .5; } return s; }
const vec3 SAF = vec3(.949, .702, .239), TAN = vec3(.918, .482, .2), POP = vec3(.824, .267, .184), CAC = vec3(.369, .204, .137);
const vec3 FOR = vec3(.243, .42, .227), ROSE = vec3(.922, .663, .561), MEAD = vec3(.725, .796, .651), CHALK = vec3(1., .992, .976);
`;

/* How the surface moves for each session (height toward the viewer). */
const DISP = /* glsl */ `
float disp(vec2 uv) {
  float z = 0.;
  if (M(0.)) {            // reiki: warmth lifts the surface under the hands, rings spread out
    for (int i = 0; i < 2; i++) { vec2 d = A(uv - uP[i].xy); float r = length(d);
      z += .05 * uP[i].z * G(d, .2) + .007 * uP[i].z * sin(r * 38. - uT * 2.4) * exp(-r * 5.); }
  } else if (M(1.)) {     // swedish: one long gliding wave, and oil drops rippling where they land
    float x = uv.x - (uP[0].x + (uv.y - .5) * .3); z += .035 * exp(-x * x / .006);
    vec2 d = A(uv - uP[1].xy); float r = length(d), a = uP[1].z;
    z += .012 * sin(r * 60. - a * 10.) * exp(-a * 1.6) * exp(-r * 8.);
  } else if (M(2.)) {     // lymph: a slow tide, and the node at the collarbone pulsing
    z += .03 * (fbm(uv * 3. + vec2(uT * .05, 0.)) - .5) + .03 * uP[0].z * G(A(uv - uP[0].xy), .07);
  } else if (M(3.)) {     // deep tissue: slow pressure sinking into the muscle
    for (int i = 0; i < 3; i++) z -= .09 * uP[i].z * G(A(uv - uP[i].xy), .11);
  } else if (M(4.)) {     // thai: palms pressing on a beat
    for (int i = 0; i < 2; i++) z -= .06 * exp(-uP[i].z * 3.) * G(A(uv - uP[i].xy), .12);
  } else if (M(5.)) {     // sarga: each footstep presses in and ripples out
    for (int i = 0; i < 4; i++) { vec2 d = A(uv - uP[i].xy); float r = length(d), a = uP[i].z;
      z += step(0., a) * (-.05 * exp(-a * 4.) * G(d, .07) + .012 * sin(r * 45. - a * 9.) * exp(-a * 1.2) * exp(-r * 6.)); }
  } else if (M(7.)) {     // yoga: the whole picture breathes
    z += .07 * uP[0].z * exp(-dot(A(uv - .5), A(uv - .5)) * 1.5);
  }
  return z;
}
`;

export const PHOTO_VS = /* glsl */ `
precision highp float;
attribute vec2 aPos;
uniform mat4 uPV, uM;
uniform vec2 uSize;
uniform float uBend, uRelief;
uniform sampler2D uTex;
uniform vec4 uCover;
varying vec2 vUv;
varying float vShade, vZ;
${COMMON}
${DISP}
float H(vec2 uv) {
  float z = disp(uv);
#ifdef VTF
  // soft relief from brightness, blurred so hard edges (a ridge against the sky) never tear
  vec3 b = vec3(0.);
  for (int i = 0; i < 9; i++) {
    vec2 o = vec2(mod(float(i), 3.) - 1., floor(float(i) / 3.) - 1.) * .035;
    b += texture2D(uTex, uCover.zw + clamp(uv + o, 0., 1.) * uCover.xy).rgb;
  }
  z += uRelief * (dot(b / 9., vec3(.3, .59, .11)) - .5);
#endif
  return z;
}
void main() {
  vUv = aPos;
  float e = 1. / 96.;
  float z = H(aPos), zx = H(aPos + vec2(e, 0.)), zy = H(aPos + vec2(0., e));
  vec3 n = normalize(vec3(-(zx - z) / (e * uSize.x), -(zy - z) / (e * uSize.y), 1.));
  vShade = dot(n, normalize(vec3(-.4, .5, .8)));
  vZ = z;
  float xb = (aPos.x - .5) * 2.;
  gl_Position = uPV * uM * vec4((aPos - .5) * uSize, z + uBend * xb * xb, 1.);
}
`;

export const PHOTO_FS = /* glsl */ `
precision highp float;
uniform sampler2D uTex;
uniform vec4 uCover;
uniform vec2 uLens;
varying vec2 vUv;
varying float vShade, vZ;
${COMMON}
vec3 screen(vec3 a, vec3 b) { return 1. - (1. - a) * (1. - b); }
void main() {
  vec2 uv = vUv, off = vec2(0.);
  if (M(1.)) { float x = uv.x - (uP[0].x + (uv.y - .5) * .3); off.x -= .1 * x * exp(-x * x / .006); }
  if (M(5.) || M(1.) || M(0.)) off += vec2(vZ) * vec2(.18, .12);
  if (M(9.)) {             // herbalism: steam rising off the remedy
    float m = smoothstep(.3, .75, uv.y) * smoothstep(.35, .6, uv.x);
    off += m * .005 * vec2(fbm(uv * 6. + vec2(0., -uT * .6)) - .5, fbm(uv * 5. + vec2(3., -uT * .5)) - .5);
  }
  vec3 c = texture2D(uTex, uCover.zw + clamp(uv + off, 0., 1.) * uCover.xy).rgb;
  c *= 1. + (vShade - .77) * 2.;

  if (M(0.)) {
    vec3 glow = vec3(0.);
    for (int i = 0; i < 2; i++) { vec2 d = A(uv - uP[i].xy); float r = length(d);
      glow += SAF * (.5 * G(d, .2) + .18 * smoothstep(.6, 1., sin(r * 38. - uT * 2.4)) * exp(-r * 6.)) * uP[i].z; }
    c = screen(c * .9, glow);
  } else if (M(1.)) {
    float x = uv.x - (uP[0].x + (uv.y - .5) * .3);
    c = screen(c, (ROSE * .5 + CHALK * .25) * exp(-x * x / .003) * .7);
  } else if (M(2.)) {
    float r = length(A(uv - uP[0].xy));
    c = screen(c * .92, TAN * (.45 * uP[0].z * exp(-r * r / .01) + .2 * smoothstep(.01, 0., abs(r - .05 - uP[0].z * .04))));
  } else if (M(3.)) {
    for (int i = 0; i < 3; i++) { float r = length(A(uv - uP[i].xy));
      c = screen(c, POP * uP[i].z * .35 * smoothstep(.012, 0., abs(r - .14 * (1. - uP[i].z) - .05))); }
  } else if (M(4.)) {
    for (int i = 0; i < 2; i++) { float r = length(A(uv - uP[i].xy)), a = uP[i].z;
      c = screen(c, (i == 0 ? SAF : MEAD) * exp(-a * 2.) * .5 * smoothstep(.015, 0., abs(r - a * .3))); }
  } else if (M(5.)) {
    for (int i = 0; i < 4; i++) { float r = length(A(uv - uP[i].xy)), a = uP[i].z;
      c = screen(c, TAN * step(0., a) * exp(-a * 1.5) * .35 * smoothstep(.012, 0., abs(r - a * .22))); }
  } else if (M(6.)) {      // zen mountain: mist drifting through the valley, the sun rising, light on the water
    float m = fbm(vec2(uv.x * 3. - uT * .035, uv.y * 7. + uT * .01));
    float band = smoothstep(.2, .45, uv.y) * smoothstep(.85, .5, uv.y);
    c = mix(c, CHALK * .96, smoothstep(.45, .8, m) * band * .55);
    c = screen(c, SAF * .55 * G(A(uv - uP[0].xy), .22));
    float sp = pow(vnoise(vec2(uv.x * 90. - uT * 2., uv.y * 24.)), 14.) * smoothstep(.32, .05, uv.y);
    c += CHALK * sp * 1.4;
  } else if (M(7.)) {
    c *= .88 + .16 * uP[0].z;
  } else if (M(8.)) {      // readings: the room goes to night; the lens shows it as it is
    float l = dot(c, vec3(.3, .59, .11));
    vec3 night = mix(vec3(.025, .03, .07), vec3(.17, .12, .2), l) + c * smoothstep(.55, .92, l) * 1.2;
    night += mix(POP, TAN, fbm(uv * 3. + uT * .02)) * .12 * smoothstep(.45, .8, fbm(uv * 2.5 - uT * .015));
    float r = length(A(uv - uLens));
    c = mix(night, c * 1.05, smoothstep(.2, .15, r));
    c += SAF * .7 * exp(-pow((r - .175) / .004, 2.));
  } else if (M(9.)) {
    c = screen(c, SAF * .18 * G(A(uv - vec2(.55, .55)), .35));
  }
  c *= mix(1., smoothstep(1.25, .25, length((uv - .5) * vec2(1., 1.2))), .4);
  gl_FragColor = vec4(c, 1.);
}
`;

export const POINTS_VS = /* glsl */ `
precision highp float;
attribute vec4 aS;
uniform mat4 uPV, uM;
uniform vec2 uSize;
uniform float uPx;
varying vec4 vC;
varying float vK, vR;
${COMMON}
vec3 L(vec2 uv, float z) { return vec3((uv - .5) * uSize, z); }
vec2 circ(float a, float r) { return vec2(cos(a) / uAsp, sin(a)) * r; }
vec3 P(float i) { return i < .5 ? uP[0] : i < 1.5 ? uP[1] : i < 2.5 ? uP[2] : uP[3]; }
float h(float n) { return fract(sin(n * 91.345) * 47453.21); }
void main() {
  vec3 p = vec3(0.); float s = .02, k = 0.; vec4 c = vec4(SAF, 1.); vR = 0.;
  float t = uT;
  if (M(0.)) {
    vec3 hd = aS.x < .5 ? uP[0] : uP[1]; float life = fract(t * .1 * (.6 + aS.y) + aS.z);
    p = L(hd.xy + vec2((aS.w - .5) * .16 + sin(life * 6. + aS.x * 20.) * .02, life * .4 - .05), life * .25);
    s = .012 + .02 * aS.y; c = vec4(mix(SAF, CHALK, aS.w), sin(life * 3.1416) * .9 * hd.z);
  } else if (M(1.)) {
    float y = aS.y; p = L(vec2(uP[0].x + (y - .5) * .3 + (aS.z - .5) * .05, y), .05);
    s = .012 + .02 * aS.w; c = vec4(mix(ROSE, CHALK, .6), pow(sin(t * 3. + aS.w * 30.) * .5 + .5, 4.));
  } else if (M(2.)) {
    float j = floor(aS.x * 9.);
    vec2 a = vec2(h(j) * .5 + .45, h(j + 7.) * .55 + .05), b = uP[0].xy;
    vec2 cp = mix(a, b, .5) + vec2(-.12, .08) * (h(j + 3.) - .4);
    float u = fract(t * .06 * (.8 + h(j + 5.) * .4) + aS.y);
    vec2 q = (1. - u) * (1. - u) * a + 2. * u * (1. - u) * cp + u * u * b;
    p = L(q + (aS.z - .5) * .012, .04);
    s = .01 + .01 * aS.w; c = vec4(mix(TAN, CHALK, aS.w * .7), smoothstep(0., .1, u) * smoothstep(1., .85, u));
  } else if (M(3.)) {
    float i = floor(aS.z * 3.); vec3 q = P(i); float f = fract(t * .35 + aS.y);
    p = L(q.xy + circ(aS.x * 6.2832, .02 + f * .16), .05 + f * .1);
    s = .012; c = vec4(mix(POP, CHALK, .35), (1. - f) * q.z * .8);
  } else if (M(4.) || M(5.)) {
    float n = M(4.) ? 2. : 4.; float i = floor(aS.z * n); vec3 q = P(i); float a = q.z;
    p = L(q.xy + circ(aS.x * 6.2832, .02 + a * .28 * (.7 + aS.y * .6)), a * .25);
    s = .012; c = vec4(M(4.) ? (i < .5 ? SAF : MEAD) : mix(TAN, SAF, aS.w), step(0., a) * exp(-a * 2.2) * .9);
  } else if (M(6.)) {
    p = L(vec2(fract(aS.x + t * .008 * (.5 + aS.y)), .12 + aS.y * .55 + sin(t * .5 + aS.z * 20.) * .02), aS.w * .6);
    s = .01 + .012 * aS.z; c = vec4(mix(SAF, CHALK, aS.w), .35 + .45 * pow(sin(t * 1.3 + aS.x * 50.) * .5 + .5, 2.));
  } else if (M(7.)) {
    float b = uP[0].z, ring = aS.w < .3 ? .6 : 1.;
    float a = aS.x * 6.2832 + t * .05 * (aS.z - .5);
    p = L(uP[0].xy + circ(a, ring * ((.15 + .09 * b) + (aS.y - .5) * .03)), sin(a * 3. + t * .7) * .06);
    s = .011 + .01 * aS.z; c = vec4(mix(SAF, TAN, aS.z), .45 + .45 * b);
  } else if (M(8.)) {
    k = 1.;
    if (aS.w > 1.5) {       // the stars of a constellation
      p = L(aS.xy, .06); s = .03; c = vec4(mix(SAF, CHALK, .5), .9);
    } else if (aS.w < .72) { // the night sky, slowly turning
      vec3 q = vec3((aS.x - .5) * uSize.x * 1.3, (aS.y - .5) * uSize.y * 1.3, -1.2 + aS.z * 2.);
      float r = t * .012; p = vec3(q.x * cos(r) - q.z * sin(r), q.y, q.x * sin(r) + q.z * cos(r));
      s = .006 + .014 * pow(h(aS.x * 99.), 3.);
      c = vec4(mix(CHALK, SAF, step(.82, h(aS.y * 51.))), .35 + .65 * pow(sin(t * (1. + aS.w * 3.) + aS.x * 40.) * .5 + .5, 3.));
    } else {                 // the zodiac wheel: two rings and twelve markers, tilted in space and turning
      float big = step(.9, aS.y);
      float a = (big > .5 ? floor(aS.x * 12.) / 12. : aS.x) * 6.2832 + t * .06;
      float R = (aS.z < .5 ? 1. : .84) * uP[3].z;
      vec3 q = vec3(cos(a) * R, sin(a) * R, 0.);
      q = vec3(q.x, q.y * cos(1.08), q.y * sin(1.08));
      q = vec3(q.x * cos(-.28) - q.y * sin(-.28), q.x * sin(-.28) + q.y * cos(-.28), q.z);
      p = L(uP[3].xy, .1) + q;
      s = big > .5 ? .05 : .009; c = vec4(big > .5 ? SAF : mix(SAF, CHALK, .5), big > .5 ? .95 : .55);
    }
  } else if (M(9.)) {
    k = 2.;
    p = L(vec2(aS.x + sin(t * .6 + aS.y * 20.) * .05, 1.1 - fract(t * .045 * (.6 + aS.z) + aS.w) * 1.25), aS.y * .5);
    vR = t * (aS.z - .5) * 2. + aS.x * 6.;
    s = .06 + .06 * aS.z; c = vec4(aS.y < .45 ? FOR : aS.y < .8 ? MEAD : SAF, .95);
  }
  gl_Position = uPV * uM * vec4(p, 1.);
  gl_PointSize = max(1., s * uPx / gl_Position.w);
  vC = c; vK = k;
}
`;

export const POINTS_FS = /* glsl */ `
precision mediump float;
varying vec4 vC;
varying float vK, vR;
void main() {
  vec2 p = gl_PointCoord * 2. - 1.;
  float d = length(p);
  if (vK < .5) { float a = smoothstep(1., 0., d); a *= a; gl_FragColor = vec4(vC.rgb * a * vC.a, 0.); return; }
  if (vK < 1.5) {
    float a = pow(max(0., 1. - d), 3.) + .45 * smoothstep(.1, 0., abs(p.x)) * smoothstep(1., 0., abs(p.y))
            + .45 * smoothstep(.1, 0., abs(p.y)) * smoothstep(1., 0., abs(p.x));
    gl_FragColor = vec4(vC.rgb * a * vC.a, 0.); return;
  }
  float cs = cos(vR), sn = sin(vR);
  vec2 q = vec2(cs * p.x - sn * p.y, sn * p.x + cs * p.y);
  float lf = max(length(q - vec2(.6, 0.)), length(q + vec2(.6, 0.))) - .95;
  float a = smoothstep(.04, -.04, lf) * vC.a;
  vec3 col = vC.rgb * (1. - .3 * smoothstep(.05, 0., abs(q.x)) * step(abs(q.y), .7)) * (.85 + .3 * q.y);
  gl_FragColor = vec4(col * a, a);
}
`;

export const LINES_VS = /* glsl */ `
precision highp float;
attribute vec3 aL;
uniform mat4 uPV, uM;
uniform vec2 uSize;
varying float vO;
void main() { vO = aL.z; gl_Position = uPV * uM * vec4((aL.xy - .5) * uSize, .06, 1.); }
`;

export const LINES_FS = /* glsl */ `
precision mediump float;
uniform float uProg, uFade;
varying float vO;
void main() { float a = smoothstep(vO - .002, vO, uProg) * uFade * .55; gl_FragColor = vec4(vec3(1., .86, .6) * a, 0.); }
`;

export const CARD_VS = /* glsl */ `
precision highp float;
attribute vec2 aQ;
uniform mat4 uPV, uM, uC;
varying vec2 vQ;
void main() { vQ = aQ; gl_Position = uPV * uM * uC * vec4(aQ * vec2(.62, 1.), 0., 1.); }
`;

export const CARD_FS = /* glsl */ `
precision highp float;
uniform float uSym, uA, uLit;
varying vec2 vQ;
const vec3 SAF = vec3(.949, .702, .239), TAN = vec3(.918, .482, .2), POP = vec3(.824, .267, .184), CAC = vec3(.369, .204, .137), CHALK = vec3(1., .992, .976);
float star5(vec2 p, float r, float rf) {
  const vec2 k1 = vec2(.809017, -.587785), k2 = vec2(-k1.x, k1.y);
  p.x = abs(p.x); p -= 2. * max(dot(k1, p), 0.) * k1; p -= 2. * max(dot(k2, p), 0.) * k2; p.x = abs(p.x); p.y -= r;
  vec2 ba = rf * vec2(-k1.y, k1.x) - vec2(0., 1.);
  float hh = clamp(dot(p, ba) / dot(ba, ba), 0., r);
  return length(p - ba * hh) * sign(p.y * ba.x - p.x * ba.y);
}
void main() {
  vec2 p = vQ * 2.; p.x *= .62;
  vec2 q = abs(p) - vec2(.62, 1.) + .09;
  float box = length(max(q, 0.)) + min(max(q.x, q.y), 0.) - .09;
  if (box > 0.) discard;
  float aa = .012;
  vec3 col;
  if (gl_FrontFacing) {
    col = mix(CHALK, vec3(.98, .93, .86), smoothstep(-1., 1., p.y));
    col = mix(col, CAC, smoothstep(aa, 0., abs(box + .07)) * .85);
    vec2 s = p - vec2(0., .06);
    float r = length(s);
    if (uSym < .5) {
      float a = atan(s.y, s.x);
      float ray = smoothstep(.06, .02, abs(fract(a / 6.2832 * 12.) - .5) * r * 6.) * step(.27, r) * smoothstep(.46, .44, r);
      col = mix(col, TAN, max(smoothstep(.2 + aa, .2, r), ray));
    } else if (uSym < 1.5) {
      float m = smoothstep(.3 + aa, .3, r) * smoothstep(.25, .25 + aa, length(s - vec2(.14, .07)));
      col = mix(col, CAC, m);
    } else {
      col = mix(col, POP, smoothstep(aa, -aa, star5(s, .34, .45)));
    }
    float dots = 0.;
    for (int i = -1; i <= 1; i++) dots += smoothstep(.035, .02, length(p - vec2(float(i) * .14, -.72)));
    col = mix(col, CAC, dots * .7);
  } else {
    col = CAC;
    float lat = smoothstep(.03, 0., abs(fract((p.x + p.y) * 3.) - .5) * .35) + smoothstep(.03, 0., abs(fract((p.x - p.y) * 3.) - .5) * .35);
    col = mix(col, SAF, min(1., lat) * .22);
    col = mix(col, SAF, smoothstep(aa, 0., abs(length(p) - .26)) * .9);
    col = mix(col, SAF, smoothstep(aa, 0., abs(box + .07)) * .9);
  }
  col *= uLit;
  float edge = smoothstep(0., -aa, box);
  gl_FragColor = vec4(col * edge * uA, edge * uA);
}
`;
