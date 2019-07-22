#!bin/bash
for i in {0..5555}
do
  FILE=/home/phamhung/Downloads/handle-image/images/$i.png
  if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist"
  fi
done
