echo on
echo 'Creating Admin Tables'

cd /Users/val/xdev/xServers/api_logic_server
export PYTHONPATH="/Users/val/xdev/xServers/api_logic_server"
source venv/bin/activate
cd ui/basic_web_app
export FLASK_APP=app
flask fab create-admin --username=admin --firstname="AdminFirst" --lastname=AdminLast --email=admin@apilogicserver.com --password=p
