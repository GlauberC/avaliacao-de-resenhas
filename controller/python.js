const express = require("express")
const router = express.Router()

var {PythonShell} = require('python-shell')

var options = {
    mode: 'text',
    encoding: 'utf8',
    pythonOptions: ['-u'],
    scriptPath: './python',
    pythonPath: '/home/glauberc/anaconda3/bin/python3'

};

router.get('/', (req, res) => {
    options.args = [req.body.resenha]
    var test = new PythonShell('predict.py', options);
    test.on('message', function(message){
        res.send(message)
    })
})
module.exports = router