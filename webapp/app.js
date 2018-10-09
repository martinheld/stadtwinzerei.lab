const express = require('express');
const fs = require('fs');
const path = require('path');
const morgan = require('morgan');
const { Client } = require('pg');
const app = express();

// create a write stream (in append mode)
var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), {
  flags: 'a'
});
// setup the logger
app.use(morgan('combined', { stream: accessLogStream }));
app.use(express.static('public'));

const client = new Client({
  connectionString: process.env.DATABASE_URL,
  ssl: true
});
client.connect();

const port = process.env.PORT || 8080;

const sql = "SELECT temperature, pressure, humidity, co2ppm, created_at::TIMESTAMP AT TIME ZONE 'UTC+2' as created_at FROM measurement ORDER BY created_at DESC LIMIT 600;";

app.get('/measurements', (req, res) => {
    client.query({ text: sql}, (err, resp) => {
    if (err) {
      console.log(err.stack);
    } else {
      res.send(resp.rows.reverse());
    }
  });
});

app.listen(port, '::', () =>
  console.log(`VinoMon app listening on port ${port}!`)
);
