(function() {
    var svg = InteractiveSVG.create('testing',);
    svg.addPoint({x: 100, y: 100});
    svg.addPoint({x: 100, y: 100, static: true});
    svg.addStaticPoint({x: 140, y: 100});
})();
