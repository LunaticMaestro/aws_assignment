# aws_assignment
My work demonstrating 


# Developement Instructions

```SH
apt update
apt upgrade
apt install zip
```

## Environment 1 [For Agent 1, 2, 3]

### Create Env
```SH
python -m venv sb-env-1
pip install -r sb-env-1-req.txt --platform=manylinux2014_x86_64 --only-binary=:all: --target ./sb-env-1/lib/python3.11/site-packages
```

### Create Layer zip

```SH
mkdir -p python
cp -r sb-env-1/lib python/
zip -r sb-env-1.zip python
rm -rf python
```



## Environment 2
```SH
python -m venv sb-env-2
pip install -r sb-env-2-req.txt --platform=manylinux2014_x86_64 --only-binary=:all: --target ./sb-env-2/lib/python3.11/site-packages
```

### Create Layer zip

```SH
mkdir -p python
cp -r sb-env-1/lib python/
```

**Delete the `test` folder from `.../matplotlib...` to reduce size before repacking
```
zip -r sb-env-1.zip python
rm -rf python
```

