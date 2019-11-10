# rejustify
```rejustify``` accepts any input string and displays a left and right justified version of the text in the form of array items fitting a given pagewidth.

## Installation
pip3 is the easiest way to install on a host machine.  To install clone / download this repo and from the root run the following command:
```
pip3 install .
```

## Run in a container
<!-- ![python environment](https://imgs.xkcd.com/comics/python_environment_2x.png) -->
If you'd like to run it in a container (and keep your site-packages tidy in the process) run ```docker build``` like so:
```
docker build -t rejustify .
```

Once the container build is finished, you can enter an interactive shell with ```rejustify``` installed:
```
docker run -ti --rm rejustify /bin/ash
```

## Usage
```
~ # rejustify -h
usage: rejustify --pagewidth 20 --text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor congue nibh id aliquam."

justifies given text to a given pagewidth

optional arguments:
  -h, --help         show this help message and exit
  --pagewidth WIDTH  width of page
  --text TEXT        text to justify, must be wrapped in quotes ""
```

## Uninstall
### From localhost (pip3)
Uninstall pip3 package with:
```
pip3 uninstall rejustify
```

### From Docker
Remove the image:
```
docker rmi rejustify
```
