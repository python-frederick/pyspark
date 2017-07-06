# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "paulovn/spark-base64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "8024"
  end
  
  #config.vm.provision "shell",
  #  inline: "sudo yum install docker -y; sudo service docker start; sudo docker run -d -p 5432:5432 postgres"
end
