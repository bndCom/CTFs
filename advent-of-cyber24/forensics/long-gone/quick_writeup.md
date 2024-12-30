- convert the vmdk file to raw image: `qemu-img convert -f vmdk -O raw vm_disk_image.img image.raw`
- mount the image: 
```sh
sudo losetup -fP ~/sharedVM/win10/image.raw
sudo mount /dev/loop0p2 /mnt/part2
```
- retrieve the file `flag_game.zip` from `osboxes/.local/share/Trash/files/`, crack it using john

`csd{5An7a5_N3W_Gam3_5uCk2}`
