const express = require("express");
const bodyParser = require("body-parser");
const proc_stat= require('./proc_stat')


  
const app = express();
  
app.use(bodyParser.urlencoded({
    extended: true
}));
  

app.listen(3000, function() {
    console.log("Server started on port 3000");
});

let trace_on = false;


app.get("/trace/:pid", (req, res) => {
    if (req.params && req.params.pid && parseInt(req.params.pid)) {
        console.log("Start tracing")
        let pid = req.params.pid;
        trace_on = true;
        proc_stat.start(pid);
    }
        
    res.send("OK");
})

app.get("/stop", (req, res) => {
    console.log("Stop tracing");
    if (trace_on) {
        proc_stat.stop();
        res.send("Stopped")
        trace_on = false;

    } else {
        res.send("no tracing");
    }
})