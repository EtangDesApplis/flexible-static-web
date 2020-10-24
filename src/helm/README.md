# Install direct cluster as dev
```
helm install chefphan . --set back.url="http://myk3s.com:32020" -n chefphan
```

# Install to prod
```
helm install chefphan . --set back.url="https://chefphan.com/back" -n chefphan
```