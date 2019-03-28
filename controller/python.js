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

router.post('/', (req, res) => {
    options.args = [req.body.resenha]
    var test = new PythonShell('predict.py', options);
    
    test.on('message', message => {
        var resp = message == '[1]'? 'positiva':"negativa"
        res.render('avaliacao', {resp: resp})
    })
})
module.exports = router