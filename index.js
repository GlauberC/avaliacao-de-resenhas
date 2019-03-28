app = require('./controller/app')
const routerPython = require('./controller/python')

app.get('/', (req, res) => {
    res.render('index')
})


app.use('/python', routerPython)
const PORT = process.env.PORT || 3000
app.listen(PORT, () => console.log(`Servidor rodando em localhost:${PORT}`))

