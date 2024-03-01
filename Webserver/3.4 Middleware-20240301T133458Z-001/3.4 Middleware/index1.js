import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";
import BodyParser from "body-parser";

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = express();
const port = 3000;

app.use(BodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.post("/submit", (req, res) => {
  const streetName = req.body.street;
  const petName = req.body.pet;

  const bandName = `${streetName} ${petName}`;

  res.send(`Your band name is ${bandName}`);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
