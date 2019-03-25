# Deepin gmux backlight fix
This is a fix for the problem desripbed here:
https://bbs.deepin.org/forum.php?mod=viewthread&tid=141241

I did the test under Deepin 15.9.2 only with the intel_backlight.

#install 

## From the deb:
you will find the deb-file in the folder 'noarch'
```bash
sudo dpkg -i noarch/*.deb
```

## From the sources:
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

