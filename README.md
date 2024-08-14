create empty folder
```
mkdir mycustomdeploy
cd mycustomdeploy
```

create custom local repository
```
git init
```

link external complex repository into our local repository
```
git remote add -f origin https://github.com/MarcelSuleiman/presentation
```

enable sparse checkout
```
git config core.sparseCheckout true
```

add folders `folder_name/` or files `file_name` in to scope
```
echo "common/" >> .git/info/sparse-checkout
echo "http_check/" >> .git/info/sparse-checkout
```

download cherry-picked folders and (or) files
```
git pull origin main
```

add additional folder (file)
```
echo "dns_check/" >> .git/info/sparse-checkout
```

apply changed scope
```
git sparse-checkout reapply
```

```
# git sparse-checkout disable
# git config core.sparseCheckout false
```
