var moveSlider = function(slider, direction) {
    var value = slider.value;
    var circle = document.getElementById("target");
    var coord = "c" + direction;
    circle.setAttributeNS(null, coord, value * 5);
}

function getTransformVector(name){
}


function makeDraggable(evt) {

  var svg = evt.target;

  svg.addEventListener('mousedown', startDrag);
  svg.addEventListener('mousemove', drag);
  svg.addEventListener('mouseup', endDrag);
  svg.addEventListener('mouseleave', endDrag);

  svg.addEventListener('wheel', rot);

  var selectedElement = false;

  //
  var scale = getTransformVector("maze_scale");
  var rotation = getTransformVector("maze_rotate");
  var translation = getTransformVector("maze_translate");

  function rot(evt){
    //todo Implement rotation
    console.log(evt.deltaY);
  }

  var selectedElement, offset;

  function startDrag(evt) {
    if (evt.target.classList.contains('draggable')) {

      //"translate(${x},${y}) rotation(${angle} ${cx}, ${cy})"

      //var transmat = evt.target.attributes.transform.value.match(/\d+\s?/g)
      //console.log(evt.target.attributes.transform.value.match(/\d+\s?/g));
      //Array(5) [ "0 ", "0", "30 ", "8 ", "10" ]

      selectedElement = evt.target;
      offset = getMousePosition(evt);

      offset.x -= parseFloat(selectedElement.attributes.cx.value);
      offset.y -= parseFloat(selectedElement.attributes.cy.value);
    }
  }

function coordinateSubstitution(X, Y){
	  // map the coordinates to the marker space
	  var marker = document.getElementById("marker")

	  var radius = Math.sqrt(Math.pow(X, 2) + Math.pow(Y, 2));
	  var theta = Math.atan2(Y, X);

	  var mx = Math.cos(theta) * radius //* -Math.sign(X);
	  var my = Math.sin(theta) * radius //* -Math.sign(Y);

	  marker.setAttributeNS(null, "cx", -mx);
    marker.setAttributeNS(null, "cy", -my);

	    //print out the x,y
    document.getElementById("transx").textContent = `org${X.toPrecision(3)}, ${Y.toPrecision(3)}`
	  document.getElementById("transy").textContent = `map${mx.toPrecision(3)}, ${my.toPrecision(3)}`
	  document.getElementById("theta").textContent = `${theta.toPrecision(3)}`


}


  function drag(evt) {
    if (selectedElement) {
      evt.preventDefault();
      var coord = getMousePosition(evt);

      selectedElement.setAttributeNS(null, "cx", coord.x - offset.x);
      selectedElement.setAttributeNS(null, "cy", coord.y - offset.y);

	    coordinateSubstitution(coord.x - offset.x, coord.y - offset.y)
    }
  }

  function endDrag(evt) {
    selectedElement = null;
  }


  function getMousePosition(evt) {
    var CTM = svg.getScreenCTM();
    return {
      x: (evt.clientX - CTM.e) / CTM.a,
      y: (evt.clientY - CTM.f) / CTM.d
    };
  }

}
