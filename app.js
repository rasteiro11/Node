var app = require('./config/server');

var rotaNoticia = require('./app/routes/noticias')(app);
//rotaNoticia(app);

var rotaHome = require('./app/routes/home')(app);
//rotaHome(app);

var rotaFormInclusaoNoticia = require('./app/routes/formulario_inclusao_noticia')(app);
//rotaFormInclusaoNoticia(app);


app.listen(3000, function() {
	console.log('server is ON');
});

