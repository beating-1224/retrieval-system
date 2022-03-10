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

## edit pool dataset
```
POST: /edit_pool_dataset
{
datasets:[d1,d3]
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