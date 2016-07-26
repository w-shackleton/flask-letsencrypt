# flask-letsencrypt
Flask Let's Encrypt library for Google App Engine

flask-letsencrypt provides a page to add Let's Encrypt ACME challenge codes to a flask website.

Usage:

```python
from flask import Flask
from flask_letsencrypt import letsencrypt

app = Flask('app')
letsencrypt(app, 'path/to/template.html')
```
