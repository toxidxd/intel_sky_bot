import spynner



br = spynner.Browser()
br.load("https://www.ingress.com/intel?ll=45.015035,39.087124&z=13")
br.snapshot().save('file.png')
br.close
