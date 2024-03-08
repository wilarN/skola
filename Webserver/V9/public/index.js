const express = require('express');
const morgan = require('morgan');
const fs = require("fs");
const bodyParser = require('body-parser');

let portNumber = 3000;
let app = express();

// Use body parser
app.use(bodyParser.urlencoded({ extended: false }));

app.use(express.static(__dirname, + "/public"));

// Create logstream
var accessLogStream = fs.createWriteStream(__dirname + 'access.log', { flags: 'a' })

app.use(morgan(
    "combined",
    {stream: accessLogStream}
));

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

app.post("/login", (req, res) => {
    const username = req.body.usr;
    const password = req.body.pass;

    if(username === "william" && password === "Vincent"){
        res.redirect("/wooo.html")
    }else{
        res.redirect("/?error=wrong-credentials");
    }
});

// 404 page
app.use((req, res, next) => {
    res.status(404).send('404: Page not found');
});

app.listen(3000, () => {
    console.log(`Server is running on port ${portNumber}`);
    console.log(`http://localhost:${portNumber}/`);
});