const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname, "public")));
console.log(__dirname);
app.get("/", function(req, res) {
  res.sendFile(path.join(__dirname + "/public/", "index.html"));
});

app.get("/contact", function(req, res) {
  res.sendFile(path.join(__dirname + "/public/", "contact.html"));
  res.send("Contact page!");
});
app.get("/about", function(req, res) {
  res.sendFile(path.join(__dirname + "/public/", "about.html"));
  res.send("About page!");
});



app.listen(port, () => {
  console.log(`Server running on port ${port}.`);
  console.log(`http://localhost:${port}`);
});
