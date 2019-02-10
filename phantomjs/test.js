

var page = require('webpage').create();

page.open('https://www.ingress.com/intel', function() {
    setTimeout(function() {
        document.getEltmentById("button_link").click()
        page.render('ing.png');
        phantom.exit();
    }, 200);
});
