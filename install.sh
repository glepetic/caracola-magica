directory="$HOME/Caracola Magica"
script="caracola_magica.py"
aliases_file="$HOME/.bash_aliases"

echo "Reconfiguring script"

# Clean old files
rm -rf "$directory"

# Create directory for caracola script
mkdir "$directory"
cp $script "$directory"

# Check existence of alias file, create it if needed
if test -f "$aliases_file"; then
  echo 'Aliases file already existed.'
else
  touch "$aliases_file"
fi

caracola_alias="alias caracola='python $script'"

# Check for caracola alias in
alias_already_added=$(cat "$aliases_file" | grep "$caracola_alias")

if [ -z "$alias_already_added" ]
then
      echo "$caracola_alias" >> "$aliases_file"
else
      echo "Caracola alias was already previously configured."
fi

