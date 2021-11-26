document.addEventListener('DOMContentLoaded', function () {

    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    let coord = { x: 200, y: 200 };

    document.addEventListener("mousedown", start);
    document.addEventListener("mouseup", stop);

    function start(event) {
        document.addEventListener("mousemove", draw);
        reposition(event);
    }
    function reposition(event) {
        coord.x = event.clientX - canvas.offsetLeft;
        coord.y = event.clientY - canvas.offsetTop;
    }
    function stop() {
        document.removeEventListener("mousemove", draw);
    }
    function draw(event) {
        ctx.beginPath();
        ctx.lineWidth = 1;
        ctx.lineCap = 'round';
        ctx.strokeStyle = '#000';
        ctx.moveTo(coord.x, coord.y);
        reposition(event);
        ctx.lineTo(coord.x, coord.y);
        ctx.stroke()
    }
})