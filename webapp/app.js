
const express = require('express')
const fs = require('fs')
const path = require('path')
const morgan = require('morgan')
const lite = require('sqlite3')
const app = express()

// create a write stream (in append mode)
var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
// setup the logger
app.use(morgan('combined', { stream: accessLogStream }))
app.use(express.static('public'))

const port = 8080

const db = new lite.Database('../measurements.db')

const sql = "SELECT temperature, pressure, humidity, co2ppm, datetime(created_at,'localtime') as created_at FROM measurement ORDER BY created_at DESC LIMIT 300"

app.get('/measurements', (req, res) => {
    db.all(sql, [], (err, rows) => {
        if (err) {
            throw err;
        }
        res.send(rows.reverse());
    })
});

app.listen(port, '::', () => console.log(`VinoMon app listening on port ${port}!`))
