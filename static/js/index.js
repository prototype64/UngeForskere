var canvas = document.getElementById('drawing');
var ctx = canvas.getContext('2d');

// last known position
let pos = { x: 0, y: 0 };

// new position from mouse event
function setPosition(e) {
  const rect = canvas.getBoundingClientRect();
  pos.x = (e.clientX - rect.left);
  pos.y = (e.clientY - rect.top);
  
  // console.log(`x: ${pos.x}, y: ${pos.y}`);
}

function draw(e) {
  if (e.buttons !== 1) return;
  
  ctx.beginPath(); // begin
  
  ctx.lineWidth = 5;
  ctx.lineCap = 'square';
  ctx.lineJoin = 'square';
  ctx.strokeStyle = 'black';
  
  ctx.moveTo(pos.x, pos.y); // draw from this position (last position)
  setPosition(e); // update position
  ctx.lineTo(pos.x, pos.y); // draw to this position (current position)
  
  ctx.stroke();
}

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

document.addEventListener('mousemove', draw);
document.addEventListener('mousedown', setPosition);
document.addEventListener('mouseenter', setPosition);
// document.addEventListener('clear', clearCanvas);

// function clearCanvas(whenPressKey) {
//   if (whenPressKey.keyCode == key.C) {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//   }
// }