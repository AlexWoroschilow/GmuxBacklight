# Deepin gmux backlight fix
This is a fix for the problem described here:
https://bbs.deepin.org/forum.php?mod=viewthread&tid=141241

I did the test under Deepin 15.9.2 only with the intel_backlight.
 

## Install from the pre-built deb-package:
you will find the deb-file in the folder 'noarch'
```bash
sudo dpkg -i noarch/*.deb
```

## Install from the sources:
You will need the rpm and alien to build the .deb and .rpm packages:
```bash
sudo apt-get install rpm alien
```
Now you can run the make script:
```bash
make
```
Install the packages:
```bash
sudo dpkg -i noarch/*.deb
```

