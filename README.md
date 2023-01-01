[How to Deploy a Flask Application to Render](https://medium.com/python-in-plain-english/how-to-deploy-a-flask-application-to-render-2a70e4d55919)

```shell
git clone git@github.com:lifeparticle/render-flask.git
cd render-flask/
pip install -r requirements.txt
gunicorn app:app --reload
```
