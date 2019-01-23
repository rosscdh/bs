# Openshift BS

```
oc process -p NODE_PORT=2343
```

will output a `${NODE_PORT}` that.. is a..... STRING. Which will throw a "not an iInt error when running for the 2nd time against the remote Openshift Server

This project will use jinja to sanely let you process and convert yaml without the BS.

### Install using docker

```bash
make build
make shell
# or
docker pull rosscdh/oc-bs:latest
docker run --rm \
       -v ${PWD}:/src \
       -it rosscdh/oc-bs:latest --help
```

### Using

Now you have access to all of jinja2 powerful filters as well as some base64 encode/decode built for openshift secrets

http://jinja.pocoo.org/docs/2.10/templates/

Simply output `{{ variabels | filter }}` in your yaml files.

```bash
docker run --rm \
       -v ${PWD}/example.yml:/src/example.yml \
       -it rosscdh/oc-bs:latest -f /src/example.yaml -p NODEPORT=33012  -p NLB_NODE_PORT_ACCOUNTWEB=33012
```

```bash
bs -f example.yml -p NODEPORT=33012  -p NLB_NODE_PORT_ACCOUNTWEB=33012
# save output to a file
bs -f example.yml -p NODEPORT=33012  -p NLB_NODE_PORT_ACCOUNTWEB=33012 -o test.json
```

### Install locally

```bash
python setup.py install
```

### TODO

* allow a `-c path/to/context.yaml` for loading in secrets and context variables so you dont have to pass `-p KEY=VALUE in which is kinda ugly`
