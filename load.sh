#!/bin/bash
set -e

echo "python gen.py"
python gen.py


echo "Dropping data"
mysql -uroot test -e "delete from episode"
mysql -uroot test -e "delete from tv_series"

for f in $(ls sql/*)
do
 echo "Processing $f"
 mysql -uroot test < $f
done
