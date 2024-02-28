const express = require('express');

let portNumber = 3000;
let app = express();

app.use(express.static(__dirname, + "/public"));

// Upon any get, log ip
app.use((req, res, next) => {
    // Time
    console.log("["+ Date.now() + '] Connection at ip ' + req.ip);
    next();
});

// Upon leaving, log ip
app.use((req, res, next) => {
    req.on('close', () => {
        console.log('Connection: ' + req.ip + ' closed...');
    });
    next();
});

// home page
app.get('/', (req, res) => {
    console.log('Connection: ' + req.ip + ' moved to home page...');
    res.sendFile(__dirname + '/index.html');
});

// womp page
app.get('/womp', (req, res) => {
    res.sendFile(__dirname + '/womp.html');
    console.log('Connection: ' + req.ip + ' moved to womp page...');
});

// 404 page
app.use((req, res, next) => {
    res.status(404).send('404: Page not found');
});

app.listen(3000, () => {
    console.log(`Server is running on port ${portNumber}`);
    console.log(`http://localhost:${portNumber}/`);
});