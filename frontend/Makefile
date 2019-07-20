all: 
	npm run-script build
	mv ~/vigil/my-app/build ~/vigil/my-app/cf-sample-nginx/public
	cd ~/vigil/my-app/cf-sample-nginx && ~/tmp/cf/cf push securemysoftware .
	echo "Success!"
