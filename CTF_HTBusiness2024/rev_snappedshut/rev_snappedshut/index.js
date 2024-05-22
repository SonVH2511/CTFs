const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const port = 3000;
const db = new sqlite3.Database(':memory:');
db.serialize(() => {
    db.run('CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY, secret TEXT)');
});
app.use(bodyParser.json());

app.post('/secret', (req, res) => {
  const secret = req.body.secret;
  if (!secret) {
    return res.status(400).json({ error: 'Secret parameter is missing' });
  }
  db.run("INSERT INTO secrets (secret) VALUES (?)", [secret], err => {
    if (err) {
        return res.status(500).json({ error: 'Failed to store secret' })
    }
    return res.json({ success: `Stored secret "${secret}"` });
  });
});

app.get('/secret', (req, res) => {
  db.all("SELECT secret FROM secrets", (err, rows) => {
    if (err) {
      return res.status(500).json({ error: 'Failed to retrieve secrets' });
    }
    const secrets = rows.map(row => row.secret);
    return res.json({ secrets });
  });
});

app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});

