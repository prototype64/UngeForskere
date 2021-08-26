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

const result = document.getElementById("result");
const submitButton = document.getElementById("submit");

submitButton.onclick = (e) => {
	e.preventDefault();
	const imgData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);
	const pixels = imgData.data;
	let grayscale = [];

	// get lightness of each pixel
	for (let i = 0; i < pixels.length; i += 4) {
		// const lightness = parseInt((pixels[i] + pixels[i + 1] + pixels[i + 2]) / 3);
		// grayscale.push(lightness);
		grayscale.push(pixels[i + 3] / 255);
	}

	fetch("/predict", {
		method: "POST",
		headers: {
			Accept: "application/json",
			"Content-Type": "application/json",
		},
		body: JSON.stringify(grayscale),
	}).then((res) =>
		res.json().then((data) => {
			const predictions = data.predictions;
			const highestValue = Math.max(...predictions);
			const mostLikely = predictions.indexOf(highestValue);
			console.log(Math.max(...predictions));

			result.textContent = `${mostLikely} (certainty: ${
				Math.round((highestValue * 100 + Number.EPSILON) * 100) / 100
			}%)`;
			for (var i = 0; i < predictions; i++) {
				let row_data = rows[i];
                let row = statistics.insertRow();
                let cell2 = row.insertCell(1);
                cell2.innerText = row_data[1];
			}
		})
	);
};
