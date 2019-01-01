// Generates the maze objects
function gen_maze(svg){
  var  svgns = "http://www.w3.org/2000/svg";
  var  xlinkns = "http://www.w3.org/1999/xlink";

  var maze = document.createElementNS(svgns, "g");
  var zoneA = document.createElementNS(svgns, "path");
  var zoneB = document.createElementNS(svgns, "path");
  var zoneC = document.createElementNS(svgns, "path");
  var base = document.createElementNS(svgns, "circle");
  var middle = document.createElementNS(svgns, "circle");

  zoneA.setAttribute("d", "m 5,0 a 5,5 0 0 1 -2.5,4.330127 5,5 0 0 1 -5,0 L 0,0 Z")
  zoneB.setAttribute("d", "M -2.5,4.330127 A 5,5 0 0 1 -5,1.7948967e-8 5,5 0 0 1 -2.5,-4.330127 L 0,0 Z")
  zoneC.setAttribute("d", "m -2.5,-4.330127 a 5,5 0 0 1 5,0 A 5,5 0 0 1 5,0 H 0 Z")

  base.setAttribute("r", "5.15");
  middle.setAttribute("r", "1.5");

  zoneA.setAttribute("class", "zone zone-A");
  zoneB.setAttribute("class", "zone zone-B");
  zoneC.setAttribute("class", "zone zone-C");

  base.setAttribute("class", "mazewall")
  middle.setAttribute("class", "mazeempty")

  maze.setAttribute("transform", "matrix(0,1,1,0,0,0)");
  maze.setAttribute("class", "maze");

  maze.appendChild(base);
  maze.appendChild(zoneA);
  maze.appendChild(zoneB);
  maze.appendChild(zoneC);
  maze.appendChild(middle);

  svg.appendChild(maze);
  console.log(svg);
}



// [svg0, svg1]
var svgs = document.getElementsByTagName('svg');
for (var i = 0; i < svgs.length; i++){
  gen_maze(svgs[i]);

}
