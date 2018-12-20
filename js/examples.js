(function() {
    var canvas1 = InteractiveSVG.create('example1', 300, 300);
    var A = canvas1.addPoint({ x: 120, y: 20 });
    var B = canvas1.addPoint({ x: 70, y: 280 });
    var C = canvas1.addPoint({ x: 60, y: 100 });
    var D = canvas1.addPoint({ x: 270, y: 250 });
    var L1 = canvas1.addLine({ p1: A, p2: B });
    var L2 = canvas1.addLine({ p1: C, p2: D });

    // Make point E dependent on lines L1 and L2
    canvas1.addPoint({
        r: 4, static: true, class: 'point generated-point'
    }).addDependency(
        [L1, L2],
        function(L1, L2) {
            var intersection = lineLineIntersection(L1, L2);
            if (intersection) {
                L1.$element.attr("class", "line highlight-line");
                L2.$element.attr("class", "line highlight-line");
                return {cx: intersection.x, cy: intersection.y, visibility: 'visible'};
            } else {
                L1.$element.attr("class", "line controllable-line");
                L2.$element.attr("class", "line controllable-line");
                return { visibility: 'hidden' };
            }
        }
    );
})();

(function() {
    var svg = InteractiveSVG.create('point-example', 200, 200);
    svg.addPoint({x: 100, y: 80});
    svg.addPoint({x: 60, y: 100, static: true});
    svg.addStaticPoint({x: 140, y: 100});
})();

(function() {
    var svg = InteractiveSVG.create('point-example2', 200, 200);
    var A = svg.addPoint({ x: 80, y: 100 });
    svg.addPoint({ label: 'B', x: 120, y: 100 });
    A.update({r: 20});
    svg.elements.B.$element.addClass("highlight-point");
})();

// Line example
(function() {
    var svg = InteractiveSVG.create('line-example', 200, 160);
    var A = svg.addPoint({ x: 40, y: 60 });
    svg.addPoint({ label: 'B', x: 160, y: 60 });
    svg.addLine({p1: A, p2: 'B'});
    svg.addLine({p1: A, p2: {x: 40, y: 140}});
    svg.addLine({x1: 160, y1: 140, p2: 'B'});
    svg.addLine({x1: 30, y1: 150, x2: 170, y2: 150});
    svg.addLine([A, {x: 100, y: 15}, 'B'])
})();

// Circle example
(function() {
    var svg = InteractiveSVG.create('circle-example', 200, 200);
    var A = svg.addPoint({ x: 50, y: 50 });
    var B = svg.addPoint({ x: 80, y: 50 });
    svg.addCircle({ center: A, r: B });
    svg.addCircle({ center: {x: 150, y: 50}, r: 30 });
    svg.addCircle({ cx: 50, cy: 150, r: 30 });

    svg.addPoint({ label: 'C', x: 120, y: 150 });
    svg.addCircle({ cx: 150, cy: 150, r: 'C' });
})();

// Bezier example
(function() {
    var svg = InteractiveSVG.create('bezier-example', 240, 200);
    var A = svg.addPoint({ x: 40, y: 160 });
    svg.addPoint({ label: 'B', x: 120, y: 25 });
    svg.addBezier({ p1: A, p2: 'B', p3: { x: 200, y: 160 } });
    svg.addBezier([A, {x: 25, y: 50}, {x: 175, y: 100}, 'B' ]);
})();

(function() {
    var svg = InteractiveSVG.create('dependent-point-example', 200, 200);
    var A = svg.addPoint({ x: 100, y: 20 });
    var B = svg.addPoint({ x: 160, y: 160 });
    svg.addStaticPoint({
        x: 160, y: 20, class: 'generated-point'
    }).addDependency(
        [A, B],
        function(A, B) {
            return { cx: A.x, cy: B.y };
        }
    );
})();
