const {app,BrowserWindow} = require('electron');

function createWindow(){
    //creates the browser window
    let win = new BrowserWindow({
        width: 800, //width of the window
        height: 600, //height of the window
        webPreferences:{
            nodeIntegration: true //integrate Node.JS
        }
    })

    //load the app's index.html
    win.loadFile('index.html')
}

app.on('ready',createWindow) //load the window. on() being a method of BrowserWindow