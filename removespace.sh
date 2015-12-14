find . -depth -name '* *' \
| while read f ; do
echo mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)"
mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)"
done
