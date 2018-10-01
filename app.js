const express = require('express')
const lite = require('sqlite3')
const app = express()

const port = 8080

const db = new lite.Database('measurements.db')

const sql = 'SELECT * FROM measurement ORDER BY created_at DESC LIMIT 20'

app.get('/', (req, res) => {
    db.all(sql, [], (err, rows) => {
        if (err) {
            throw err;
        }
        res.send(rows);
    })
});

app.listen(port, () => console.log(`Simple example app listening on port ${port}!`))
