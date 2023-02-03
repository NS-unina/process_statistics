const topparser=require("topparser")
const fs = require('fs')
const { format } = require('@fast-csv/format');



// const csv = "unix_epoch, pid, virt, res, cpu, mem, command"
let csvFile; 
let stream;


const getName = (command = '') => {
    let date_ob = new Date();

    // current date
    // adjust 0 before single digit date
    let date = ("0" + date_ob.getDate()).slice(-2);

    // current month
    let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);

    // current year
    let year = date_ob.getFullYear();

    // current hours
    let hours = date_ob.getHours();

    // current minutes
    let minutes = date_ob.getMinutes();

    // current seconds
    let seconds = date_ob.getSeconds();

    // prints date & time in YYYY-MM-DD HH:MM:SS format
    return (command ? command + "-" : "") + year + "-" + month + "-" + date + "_" + hours + "-" + minutes + "-" + seconds;

}

exports.start = (pid, command = '') => {
        let CSV_FILE = `stats_${getName(command)}.csv`
        csvFile = fs.createWriteStream(CSV_FILE);
        stream = format({ headers: true })
        stream.pipe(csvFile);
        topparser.start();
        topparser.on("data", data=>{
            let processes = data.processes[0];
            let proc = processes.filter((p) => p.pid == pid);
            proc = proc[0];
            if (proc) {
                let data = {
                    unix_epoch : Date.now(),
                    the_pid : proc.pid,
                    virt : proc.virt,
                    res : proc.res,
                    cpu : proc.cpu,
                    mem : proc.mem,
                    command : proc.command,
                }
                stream.write(data);

            }
            
            // console.log(Date.now())
            
        })

        //if some error happens
        topparser.on("error",error=>{
            console.log(error)
        })

        //if topparser exit
        topparser.on("close",code=>{
            console.log("Close")
            stream.end();
        })



}


exports.stop = () => {
    topparser.stop();
}