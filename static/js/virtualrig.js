var moveSlider = function(slider, direction) {
    var value = slider.value;
    var circle = document.getElementById("target");
    var coord = "c" + direction;
    circle.setAttributeNS(null, coord, value * 5);
}

function getTransformVector(name){

  var element = document.getElementById(name);
  return element.attributes.transform.value.match(/\d+\s?/g).map(parseFloat);
}


function makeDraggable(evt) {
  var svg = evt.target;
  console.log(evt);
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
      //offset.x -= parseFloat(transmat[0]);
      //offset.y -= parseFloat(transmat[0]);
    }
  }



  function drag(evt) {
    if (selectedElement) {
      evt.preventDefault();
      var coord = getMousePosition(evt);

      selectedElement.setAttributeNS(null, "x", coord.x - offset.x);
      selectedElement.setAttributeNS(null, "y", coord.y - offset.y);

      //print out the x,y
      svg.getElementById("transout").textContent = `x${coord.x.toPrecision(3)}\ny${coord.y.toPrecision(3)}`

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



// Client Side Javascript to receive numbers.
$(document).ready(function(){
    // start up the SocketIO connection to the server - the namespace 'test' is also included here if necessary
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    // this is a callback that triggers when the "my response" event is emitted by the server.
    socket.on('my response', function(msg) {
        $('#log').append('<p>Received: ' + msg.data + '</p>');
    });
    //example of triggering an event on click of a form submit button
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
});
