
resource "aws_instance" "bastion_host" {
  ami                         = var.ami
  instance_type               = "t2.micro"
  key_name                    = var.key_name
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.sgbh.id]
  user_data                   = file("user_data_bastion.sh")
  associate_public_ip_address = true

  tags = {
    Name = "bastionhost"
  }
}

resource "aws_instance" "private_host" {
  ami                    = var.ami
  instance_type          = "t2.micro"
  key_name               = var.key_name
  subnet_id              = aws_subnet.private_subnet.id
  vpc_security_group_ids = [aws_security_group.sgph.id]
  user_data              = file("user_data_private.sh")

  tags = {
    Name = "private_host"
  }
}

resource "aws_ebs_volume" "ebs_volume" {
  availability_zone = aws_instance.private_host.availaility_zone
  size = 1
  tags = {
    Name = "myebs1"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdd"
  volume_id = aws_ebs_volume.ebs_volume.id
  instance_id = aws_instance.private_host.id
  force_detach = true
}


