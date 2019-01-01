

Java script to add

```js
var svg = document.getElementsByTagName('svg')[0];

var newElement = document.createElementNS("http://www.w3.org/2000/svg", 'path'); //Create a path in SVG's namespace
newElement.setAttribute("d","M 0 0 L 10 10"); //Set path's data
newElement.style.stroke = "#000"; //Set stroke colour
newElement.style.strokeWidth = "5px"; //Set stroke width
svg.appendChild(newElement);
```
```html
<g id="maze"
   transform="matrix(-0.05,1,1,0.05,0,0)">
  <circle
     r="5.0999999"
     cx="0"
     cy="0"
     fill="#007bff"
      />
  <path
     d="m 5,0 a 5,5 0 0 1 -2.5,4.330127 5,5 0 0 1 -5,0 L 0,0 Z"
     class="zoneA"
     style="fill:#aaffaacc" />
  <path
     d="M -2.5,4.330127 A 5,5 0 0 1 -5,1.7948967e-8 5,5 0 0 1 -2.5,-4.330127 L 0,0 Z"
     class="zoneB"
     style="fill:#aaaaffcc" />
  <path
     d="m -2.5,-4.330127 a 5,5 0 0 1 5,0 A 5,5 0 0 1 5,0 H 0 Z"
     class="zoneC"
     id="path8"
     style="fill:#ffaaaacc" />
  <circle
     r="2"
     cx="0"
     cy="0"
     fill="#007bff"
     />
</g>
```

```js
function gen_maze(svg){
  var  svgns = "http://www.w3.org/2000/svg";
  var  xlinkns = "http://www.w3.org/1999/xlink";

  var maze = document.createElementNS(svgns, "g");
  var zone = document.createElementNS(svgns, "path");
  var zoneA = document.createElementNS(svgns, "use");
  var zoneB = document.createElementNS(svgns, "use");
  var zoneC = document.createElementNS(svgns, "use");
  var base = document.createElementNS(svgns, "circle");
  var middle = document.createElementNS(svgns, "circle");

  zone.setAttribute("d", "m 5,0 a 5,5 0 0 1 -2.5,4.330127 5,5 0 0 1 -5,0 L 0,0 Z")
  zone.setAttribute("id", "zone")

  base.setAttribute("r", "5.15");
  middle.setAttribute("r", "1.5");

  zoneA.setAttributeNS(xlinkns, "href", "#zone");
  zoneB.setAttributeNS(xlinkns, "href", "#zone");
  zoneC.setAttributeNS(xlinkns, "href", "#zone");

  zoneB.setAttribute("transform", "rotate(120)");
  zoneC.setAttribute("transform", "rotate(240)");

  zoneA.setAttribute("class", "zone zone-A");
  zoneB.setAttribute("class", "zone zone-B");
  zoneC.setAttribute("class", "zone zone-C");

  base.setAttribute("class", "mazewall")
  middle.setAttribute("class", "mazewall")

  maze.setAttribute("transform", "matrix(0,1,1,0,0,0)");

  maze.appendChild(base);
  maze.appendChild(zoneA);
  maze.appendChild(zoneB);
  maze.appendChild(zoneC);
  maze.appendChild(middle);

  svg.appendChild(maze);
}

```
