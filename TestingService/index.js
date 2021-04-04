const express = require('express');
var app = express();
var testURL = require('./TestURL').testDashboard;

app.use(express.urlencoded());
app.use(express.json());


function onServerListening() {
    console.log('Server Started ');
}

/*
    Requests
    {
        "Timeout" : "",
        "URL" : "",
        "ScreenShot" : "Path" 
    }

    Response
    { 
        Metrics/Error

    }
*/
app.post('/testURL', async function (req, res) {

   
    console.log(req.body);
    let TimeOut = req.body['TimeOut'];
    let URL = req.body['URL'];

    console.log(TimeOut, URL);
    let resp = await testURL(TimeOut , URL);
    res.send(resp);
});




var server = app.listen(3000, '127.0.0.1', onServerListening);