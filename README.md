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
docker run --rm \
       -v ${PWD}:/app \
       -it rosscdh/oc-bs:latest --help
```

### Using

```bash
bs -f example.yml -p NODEPORT=33012  -p NLB_NODE_PORT_ACCOUNTWEB=33012
# save output to a file
bs -f example.yml -p NODEPORT=33012  -p NLB_NODE_PORT_ACCOUNTWEB=33012 -o test.json
```

### Install locally

```bash
python setup.py install
```