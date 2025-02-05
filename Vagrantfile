Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"  # Use Ubuntu 18.04


  # configure bridge networking
  config.vm.network "public_network", bridge: "eno1"
  # Provisioning script to install Flask and set up the application
  config.vm.provision "shell", inline: <<-SHELL
    # Update and install Python and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install Flask
    pip3 install Flask

    # Run the Flask app
    nohup python3 /vagrant/flask_app/app.py > /vagrant/flask_app/flask.log 2>&1 &
  SHELL

  # Forward port 5000 to the host machine
  # config.vm.network "forwarded_port", guest: 5000, host: 5000
end

