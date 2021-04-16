Firstly let's look at the source code of the website http://mercury.picoctf.net:45028/ 
```html
<!doctype html>
<html>
<head>
    <title>Blue</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<style>body {background-color: blue;}</style>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red"/>
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue"/>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
```
Since we can use two methods GET and POST in the form, we may try other methods. The title is "GET aHEAD", so if we try to send a HEAD request to http://mercury.picoctf.net:45028/index.php and look at the header, we will get the flag.

### Flag
```
picoCTF{r3j3ct_th3_du4l1ty_775f2530}
```

