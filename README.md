# Process Statistics   

Acquire stats from a process.     

## Installation   

```  
npm install 
```

## Usage     

The module run an `express` server that listens on port `3000`. 
To run: 
``` 
npm start  
```  


It has two endpoints:  
* `/trace/:pid` : it starts the tracing of a process having a specifc `pid`.   
* `/stop` : it stops the acquisition and writes a `stats.csv` file.   



### Top Explanation
VIRT, RES, SHR and %MEM
These three fields are related with to memory consumption of the processes. 
* “VIRT” is the total amount of memory consumed by a process. This includes the program’s code, the data stored by the process in memory, as well as any regions of memory that have been swapped to the disk. 
* “RES” is the memory consumed by the process in RAM.
* “%MEM” expresses this value as a percentage of the total RAM available. 
* “SHR” is the amount of memory shared with other processes.




## Development   
* [express](https://expressjs.com)  
* [topparser](https://github.com/devalexqt/topparser)


