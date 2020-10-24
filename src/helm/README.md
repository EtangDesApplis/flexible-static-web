# Install direct cluster as dev
```
helm install chefphan . --set back.url="http://myk3s.com:32020" -n chefphan
```

# Install to prod
```
helm install chefphan . \
--set back.url="https://chefphan.com/back" \
--set client.url="https://chefphan.com/client" \
--set admin.url="https://chefphan.com/admin" \
-n chefphan
```