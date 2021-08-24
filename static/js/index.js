let canvas = document.getElementById("drawing");
let ctx = canvas.getContext("2d");

// last known position
let pos = { x: 0, y: 0 };

// new position from mouse event
function setPosition(e) {
	const rect = canvas.getBoundingClientRect();
	pos.x = (e.clientX - rect.left) / ((rect.bottom - rect.top) / canvas.height);
	pos.y = (e.clientY - rect.top) / ((rect.bottom - rect.top) / canvas.height);

	// console.log(`x: ${pos.x}, y: ${pos.y}`);
}

function draw(e) {
	if (e.buttons !== 1) return;

	ctx.beginPath(); // begin

	ctx.lineWidth = 1;
	ctx.lineCap = "square";
	ctx.lineJoin = "square";
	ctx.strokeStyle = "black";

	ctx.moveTo(pos.x, pos.y); // draw from this position (last position)
	setPosition(e); // update position
	ctx.lineTo(pos.x, pos.y); // draw to this position (current position)

	ctx.stroke();
}

function clearCanvas() {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
}

document.addEventListener("mousemove", draw);
document.addEventListener("mousedown", setPosition);
document.addEventListener("mouseenter", setPosition);

const submitButton = document.getElementById("submit");

submitButton.onclick = (e) => {
	e.preventDefault();
	const imgData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);
	const pixels = imgData.data;
	console.log("pixels", pixels);
	let grayscale = [];

	// get lightness of each pixel
	for (let i = 0; i < pixels.length; i += 4) {
		// const lightness = parseInt((pixels[i] + pixels[i + 1] + pixels[i + 2]) / 3);
		grayscale.push(pixels[3] / 255);
	}

	console.log("grayscale", grayscale);

	fetch("/upload", {
		method: "POST",
		headers: {
			Accept: "application/json",
			"Content-Type": "application/json",
		},
		body: JSON.stringify(grayscale),
	}).then((res) => {
		console.log("Request complete! response:", res);
	});
};
