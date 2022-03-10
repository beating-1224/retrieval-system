# API

## get datasets
```
GET: /datasets
```

## get sample uuid
```
POST: /samples
{
datasets:[d1,d3]
}

reply:
{
samples:[uuid1,uuid2,uuid3]
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

## edit pool dataset
```
POST: /edit_pool_dataset
{
id: d1
action:add(delete)
}
```

## edit pool modality
```
POST: /edit_pool_modality
{
id: pc(vx/mv)
action:add(delete)
}
```

## search sample
```
POST: /search_sample
{
query:uuid
}

reply:
{
results:[uuid1,uuid2,uuid3]
}
```

## search file
```
GET: /search_file

reply:
{
results:[uuid1,uuid2,uuid3]
}
```