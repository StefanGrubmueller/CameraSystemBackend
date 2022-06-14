// Requiring module
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;
app.use(cors());

// Configuring body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Handling GET request
app.post('/time-lapse', (req, res) => {
	res.send(req.body);
	res.end()
})

app.post('/time-lapse/cancel', (req, res) => {
	res.send(req.body);
	res.end()
})

app.post('/bulb', (req, res) => {
	res.send(req.body);
	res.end()
})

app.post('/bulb/cancel', (req, res) => {
	res.send(req.body);
	res.end()
})

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`));