"""Original drawings for stgeorgeconcreteleveling.com (the live site has no photos of its own).
gauge(): the trip-hazard lip gauge (two slabs, one dropping; a caliper reads the lip; the reading is matched to the 2010 ADA
Standards change-in-level rules, 303.2-303.4). surface(kind): a small isometric drawing of each surface the client levels,
with one slab dropped and a foam bead under it."""


def gauge():
    return '''<div class="gauge" data-gauge>
<svg class="g-svg" viewBox="0 0 640 300" role="img" aria-label="Two concrete slabs; drag to change how far one has sunk and see which ADA change-in-level rule applies">
<defs><pattern id="gs-soil" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="3" cy="4" r="1.3" class="sdot"/><circle cx="10" cy="11" r="1" class="sdot"/></pattern></defs>
<rect x="0" y="190" width="640" height="110" class="soil"/><rect x="0" y="190" width="640" height="110" fill="url(#gs-soil)"/>
<rect x="20" y="140" width="300" height="50" class="slab"/>
<g class="drop"><rect x="320" y="140" width="300" height="50" class="slab s2"/><path class="void" d="M320 190 h300 v0 z"/></g>
<g class="cal"><path class="cal-arm" d="M300 108 h60"/><path class="cal-jaw a" d="M310 108 v32"/><path class="cal-jaw b" d="M350 108 v32"/></g>
<text x="20" y="128" class="tg">HIGH SLAB</text><text x="520" y="128" class="tg">SUNKEN SLAB</text>
</svg>
<div class="g-read"><div class="g-num"><span data-in>0</span><small>inch lip</small></div><div class="g-rule"><b data-rule>Level</b><span data-ref>No change in level.</span></div></div>
<input class="g-range" type="range" min="0" max="16" step="1" value="6" aria-label="Lip height in sixteenths of an inch, from 0 to 1 inch">
<div class="g-scale" aria-hidden="true"><span style="--at:0%">0</span><span style="--at:25%">1/4&Prime;</span><span style="--at:50%">1/2&Prime;</span><span style="--at:75%">3/4&Prime;</span><span style="--at:100%">1&Prime;</span></div>
</div>'''


SURF = {
    "driveway": '<path class="ln" d="M150 70 h120 v60 h-120z M160 80 h100 M160 92 h100 M160 104 h100 M160 116 h100"/>',
    "sidewalk": '<path class="ln" d="M40 165 l40 -20 M120 205 l40 -20"/>',
    "patio": '<path class="ln" d="M175 120 v-22 h22 v22 M186 98 v-10 M220 128 v-14 h18 v14"/>',
    "garage": '<path class="ln" d="M60 60 l140 -40 l140 40 M60 60 v80 M340 60 v80"/>',
    "pool": '<path class="water" d="M210 170 l70 -35 l60 30 l-70 35z"/>',
    "steps": '<path class="ln" d="M170 120 h70 v-14 h-70z M180 106 h60 v-14 h-60z"/>',
    "porch": '<path class="ln" d="M150 60 v70 M290 60 v70 M140 60 h160"/>',
    "slab": "",
}


def surface(kind="slab"):
    extra = SURF.get(kind, "")
    return f'''<svg class="surf" viewBox="0 0 400 260" aria-hidden="true">
<path class="s-top" d="M40 150 L200 70 L280 110 L120 190Z"/><path class="s-side" d="M40 150 L120 190 L120 204 L40 164Z"/><path class="s-side2" d="M120 190 L280 110 L280 124 L120 204Z"/>
<g class="sunk"><path class="s-top" d="M200 210 L280 170 L360 210 L280 250Z" transform="translate(0,-8)"/><path class="foam" d="M215 212 q30 18 60 10 q30 -6 60 4 q-30 22 -60 18 q-34 -4 -60 -32z"/></g>
<path class="s-top s3" d="M120 190 L280 110 L360 150 L200 230Z"/>
{extra}</svg>'''
