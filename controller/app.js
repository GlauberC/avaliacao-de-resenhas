const express = require('express')

const bodyParser = require('body-parser')
const path = require("path")
const handlebars = require('express-handlebars')

const app = express()


    // Body Parser
    app.use(bodyParser.urlencoded({extended: true}))
    app.use(bodyParser.json())

    // Handlebars
    app.engine('handlebars', handlebars({defaultLayout: 'main'}))
    app.set('view engine', 'handlebars');

module.exports = app