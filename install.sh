directory="$HOME/Caracola_Magica"
src_dir="src"
resources_dir="resources"
script="$src_dir/caracola_magica.py"
aliases_file="$HOME/.bash_aliases"

echo "Reconfiguring script folders"

# Clean old files
rm -rf "$directory"

# Create directory for caracola script
mkdir "$directory"
cp -r $src_dir "$directory"
cp -r $resources_dir "$directory"

# Check existence of alias file, create it if needed
if test -f "$aliases_file"; then
  echo 'Aliases file already existed.'
else
  touch "$aliases_file"
fi

caracola_alias="alias caracola='python3 $directory/$script'"

# Check for caracola alias in
alias_already_added=$(cat "$aliases_file" | grep "$caracola_alias")

if [ -z "$alias_already_added" ]
then
      echo "$caracola_alias" >> "$aliases_file"
else
      echo "Caracola alias was already previously configured."
fi

