# API

## get datasets
```
GET: /datasets

reply:
{
datasets:[d1,d2,d3]
}
```

## get samples
```
GET: /samples
{
datasets:[d1,d3]
}

reply:
{
samples:[path1,path2,path3]
}
```

## upload
```
POST: /upload
{
file:.???
}

reply:
{
poster:.png
src:.glb
}
```


## search sample
```
GET: /search_sample
{
query:path,
datasets:[d1,d3]
modalities:['pt','vx','mv']
}

reply:
{
results:[uuid1,uuid2,uuid3]
}
```

## search file
```
GET: /search_file
{
file:f
datasets:[d1,d3]
modality:['pt','vx','mv']
}

reply:
{
results:[uuid1,uuid2,uuid3]
}
```