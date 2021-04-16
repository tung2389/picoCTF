```
wget https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg
cat cat.jpg | head -n 10
```
Now you see some interesting code. The string 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' may be the key, since it has the word "resource" before it. But this looks like base 64 encoded string. Therefore, we can run the below command to get the flag.
```
echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
```
