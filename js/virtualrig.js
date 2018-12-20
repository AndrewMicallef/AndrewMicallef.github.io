var moveSlider = function(slider, direction) {
    var value = slider.value;
    var circle = document.getElementById("target");
    var coord = "c" + direction;
    circle.setAttributeNS(null, coord, value * 5);
}


function makeDraggable(evt) {
  var svg = evt.target;

  svg.addEventListener('mousedown', startDrag);
  svg.addEventListener('mousemove', drag);
  svg.addEventListener('mouseup', endDrag);
  svg.addEventListener('mouseleave', endDrag);

  svg.addEventListener('wheel', rot);

  var selectedElement = false;

function rot(evt){
  //todo Implement rotation
  console.log(evt.deltaY);
}

  var selectedElement, offset;

  function startDrag(evt) {
    if (evt.target.classList.contains('draggable')) {
      console.log(evt.target.attributes.transform);

      selectedElement = evt.target;
      offset = getMousePosition(evt);
      offset.x -= parseFloat(selectedElement.getAttributeNS(null, "x"));
      offset.y -= parseFloat(selectedElement.getAttributeNS(null, "y"));
    }
  }



  function drag(evt) {
    if (selectedElement) {
      evt.preventDefault();
      var coord = getMousePosition(evt);

      selectedElement.setAttributeNS(null, "x", coord.x - offset.x);
      selectedElement.setAttributeNS(null, "y", coord.y - offset.y);

      console.log(coord.x);
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
