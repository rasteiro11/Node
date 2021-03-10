var http = require('http');

var server = http.createServer( function(req, res){
	var categoria = req.url;

	if (categoria == '/tecnologia') {
		res.end("<html><body>Noticias de tecnologia</body></html>")
	} else if (categoria == '/moda') {
		res.end("<html><body>Noticias de moda</body></html>")
	} else if (categoria == '/beleza') {
		res.end("<html><body>Noticias de beleza</body></html>")
	} else {
		res.end("<html><body>Portal de noticias</body></html>")
	}

});

server.listen(3000);