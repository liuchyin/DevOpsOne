import os
os.system('ls')
os.system('sudo apt-get update -y && sudo apt-get install htop -y && sudo apt-get install tmux -y && sudo apt-get install vim -y')
os.system('sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev -y')
os.system('git clone git://github.com/sstephenson/rbenv.git .rbenv')
os.system('echo export PATH="$HOME/.rbenv/bin:$PATH" >> ~/.bashrc')
os.system('echo export PATH="$HOME/.rbenv/bin:$PATH" >> ~/.bash_profile')
os.system('echo eval "$(rbenv init -)" >> ~/.bashrc')
os.system('echo eval "$(rbenv init -)" >> ~/.bash_profile')
os.system('exec $SHELL')
os.system('git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build')
os.system('echo export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH" >> ~/.bashrc')
os.system('echo export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH" >> ~/.bash_profile')
os.system('exec $SHELL')
os.system('. .bashrc')
os.system('. .bash_profile')
os.system('git clone https://github.com/sstephenson/rbenv-gem-rehash.git ~/.rbenv/plugins/rbenv-gem-rehash')
os.system('rbenv install 2.2.3')
os.system('rbenv global 2.2.3')
os.system('ruby -v')
