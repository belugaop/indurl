if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PrinceStarLord/FLASHLINK-v2.git /FLASHLINK-v2
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /FLASHLINK-v2
fi
cd /FLASHLINK-v2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m main
