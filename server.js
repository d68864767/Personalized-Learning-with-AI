```javascript
// server.js

// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const { Client } = require('pg');

// Import PythonShell for running Python scripts
const { PythonShell } = require('python-shell');

// Import config
const config = require('./config.py');

// Create Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files from the React app
app.use(express.static(path.join(__dirname, config.UI_DIR)));

// Database connection
const client = new Client({
    host: config.DATABASE_CONFIG.host,
    user: config.DATABASE_CONFIG.user,
    password: config.DATABASE_CONFIG.password,
    database: config.DATABASE_CONFIG.dbname,
    port: config.DATABASE_CONFIG.port
});

client.connect();

// Routes
app.get('/api', (req, res) => {
    res.json({ message: 'Welcome to AI-Adaptive Tutor API!' });
});

app.post('/api/assess', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: './',
        args: [req.body.userInput]
    };

    PythonShell.run('ml_model.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        res.json({ message: 'Assessment completed!', results: results });
    });
});

app.post('/api/interact', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: './',
        args: [req.body.userInput]
    };

    PythonShell.run('nlp_model.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        res.json({ message: 'Interaction completed!', results: results });
    });
});

// Start server
app.listen(config.SERVER_CONFIG.port, () => {
    console.log(`Server is running on port ${config.SERVER_CONFIG.port}.`);
});
```
