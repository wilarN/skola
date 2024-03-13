const express = require('express');
const app = express();
const path = require('path');

const port = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const date = new Date();
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let day_offset = date.getDay()

function getAdvice() {
    if (day_offset == 0 || day_offset == 6) {
        return "It's weekend! Take a break and enjoy your day!";
    } else {
        return "What a wonderful workday it is today! Keep up the good work and stay positive!";
    }
}

app.get('/', (req, res) => {
    res.render('index',
        {
            dayPlaceholder: days[day_offset],
            advicePlaceholder: getAdvice()
        });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
